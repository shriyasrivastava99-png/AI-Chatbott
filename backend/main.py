from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import os

from app.api import chat, conversations, documents
from app.models.database import engine, Base
# Import all models to ensure they are registered before create_all
from app.models.conversation import Conversation
from app.models.message import Message
from app.models.document import Document, DocumentChunk

# Create tables
Base.metadata.create_all(bind=engine)



app = FastAPI(title="Multimodal AI Chatbot")

# Setup CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/health")
def health_check():
    return {"status": "healthy"}

app.include_router(chat.router, prefix="/api/chat", tags=["chat"])
app.include_router(conversations.router, prefix="/api/conversations", tags=["conversations"])
app.include_router(documents.router, prefix="/api/documents", tags=["documents"])



# Mount the frontend directory so FastAPI serves the HTML/JS/CSS directly
# It serves index.html by default at /
frontend_path = os.path.join(os.path.dirname(__file__), "../../frontend")
if os.path.exists(frontend_path):
    app.mount("/", StaticFiles(directory=frontend_path, html=True), name="frontend")
