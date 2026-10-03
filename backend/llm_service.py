import os
from typing import List, Optional
from huggingface_hub import InferenceClient

class LLMService:
    def __init__(self):
        # We allow configuring the model via environment variable. 
        # Defaulting to a lightweight conversational model for text, or the user's choice.
        # Note: 'microsoft/Phi-4-multimodal-instruct' via serverless API might have limitations,
        # so we abstract it. For standard text, we can use a popular instruct model.
        self.model_name = os.getenv("MODEL_NAME", "Qwen/Qwen2.5-72B-Instruct")
        self.hf_token = os.getenv("HF_TOKEN")
        
        if self.hf_token:
            # Bypass the auto-router for non-standard Hugging Face tokens
            if not self.hf_token.startswith("hf_"):
                base_url = f"https://api-inference.huggingface.co/models/{self.model_name}"
                self.client = InferenceClient(base_url=base_url, token=self.hf_token)
            else:
                self.client = InferenceClient(model=self.model_name, token=self.hf_token)
        else:
            self.client = None

    def generate_response(self, text: str, image_bytes: Optional[bytes] = None, history: List[dict] = None) -> str:
        """
        Abstracted method for generating a response.
        History should be a list of dicts: [{"role": "user", "content": "..."}]
        """
        if not self.client:
            return ("Error: HF_TOKEN is not configured. Please add your Hugging Face token "
                    "to the .env file to use open-source models.")

        messages = history if history else []
        
        # In a fully local setup with transformers, we would process image_bytes here.
        # Since the HuggingFace serverless API for standard models often expects text,
        # we will handle text natively, and add a placeholder for image processing if supported.
        content = text
        if image_bytes:
            content += "\n[System: User attached an image. Image processing requires a dedicated Vision-Language Model endpoint.]"

        messages.append({"role": "user", "content": content})

        try:
            # Call HuggingFace Inference API
            response = self.client.chat_completion(messages=messages, max_tokens=512)
            return response.choices[0].message.content
        except Exception as e:
            return f"AI Error: {str(e)}"

# Singleton instance
llm_service = LLMService()
