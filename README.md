# Multimodal AI Chatbot

A beginner-friendly Multimodal AI Chatbot that can understand text, images, process PDFs with RAG (Retrieval-Augmented Generation), search the web, and provide emotional assistance. 

## Features
- **Phase 1: Basic Chat (Completed)** - Text chat powered by Google Gemini, storing conversations in PostgreSQL (or SQLite fallback).
- **Phase 2: Multimodal Input (Completed)** - Voice dictation via Web Speech API, Image and File upload support via Gemini's multi-part generation.
- **Phase 3:** RAG Pipeline *(Pending)*
- **Phase 4:** Web Search Integration *(Pending)*
- **Phase 5:** Text-to-Speech Output *(Pending)*
- **Phase 6:** Emotional Assistant & Guardrails *(Pending)*

## Tech Stack
- **Frontend:** Vanilla HTML, CSS (Glassmorphism design), and JS
- **Backend:** Python + FastAPI
- **Database:** PostgreSQL (with SQLAlchemy)
- **AI Model:** Google Gemini API (`gemini-1.5-flash`)

## Architecture
```text
User
 ↓
Frontend (HTML/JS/CSS)
 ↓
FastAPI Backend
 ↓
 ├── AI Model (Gemini)
 ├── PostgreSQL (Conversations & Messages)
```

## Installation

1. **Clone/download project**
2. **Create virtual environment**
   ```powershell
   python -m venv venv
   .\venv\Scripts\activate
   ```
3. **Install requirements**
   ```powershell
   cd backend
   pip install -r requirements.txt
   ```
4. **Configure Environment Variables**
   Rename `backend/.env.example` to `backend/.env` and add your Gemini API Key.
   *(By default, it uses SQLite if PostgreSQL is not provided, making it easy to test Phase 1 immediately).*
5. **Start FastAPI**
   ```powershell
   cd backend
   uvicorn app.main:app --reload
   ```
6. **Open application**
   Open your browser and navigate to `http://127.0.0.1:8000/`. You should see the beautiful Chatbot interface!

## API Endpoints
| Method | Endpoint                | Purpose         |
| ------ | ----------------------- | --------------- |
| POST   | `/api/chat`             | Text chat       |
| GET    | `/api/conversations`    | List conversations |
| GET    | `/api/conversations/{id}` | Get conversation details |
| DELETE | `/api/conversations/{id}` | Delete conversation |
| GET    | `/api/health`           | Health check    |
Multimodal AI Chatbot

A beginner-friendly AI chatbot web application with a separate Python backend and HTML, CSS, and JavaScript frontend. The project is designed to support conversational interaction and can be extended with document handling, conversation history, and AI-powered responses.

Project Description

This project is a web-based AI chatbot that provides a simple interface for users to communicate with an AI system.

Main Features

💬 Chat interface for sending user questions

🤖 AI-powered response system

📄 Document-related functionality

🗂️ Conversation and message handling

🌐 Separate frontend and backend structure

🎨 HTML, CSS and JavaScript frontend

🐍 Python backend

🔐 Environment-variable based configuration for API credentials

🧩 Modular backend structure with APIs, models, schemas and services

Technology Stack

Frontend: HTML, CSS, JavaScript

Backend: Python

Database: SQLite/local database support

AI: Configured through the API/model provider used by the project

Version Control: Git and GitHub

Project Structure

Chatbot/
│
├── backend/
│   ├── app/
│   │   ├── api/
│   │   │   ├── chat.py
│   │   │   ├── conversations.py
│   │   │   └── documents.py
│   │   │
│   │   ├── models/
│   │   │   ├── conversation.py
│   │   │   ├── database.py
│   │   │   ├── document.py
│   │   │   └── message.py
│   │   │
│   │   ├── schemas/
│   │   └── services/
│   │
│   └── main.py
│
├── frontend/
│   ├── index.html
│   ├── script.js
│   └── style.css
│
├── uploads/              # Only project-required sample files
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md

__pycache__, .pyc files, virtual-environment folders, .env, and other local/generated files should not be committed to GitHub.

Requirements

Before running the project, install:

Python 3.10+ (or the Python version required by your installed dependencies)

Git

A modern web browser

Required API credentials/model access, if the configured AI provider requires them

Installation

1. Clone the repository

git clone YOUR_GITHUB_REPOSITORY_URL
cd Chatbot

Replace YOUR_GITHUB_REPOSITORY_URL with the URL of this GitHub repository.

2. Create a virtual environment

Windows:

python -m venv venv

Activate it:

venv\Scripts\activate

macOS/Linux:

python3 -m venv venv
source venv/bin/activate

3. Install dependencies

pip install -r requirements.txt

Environment Variables

The project uses environment variables so that API keys and other secrets are not stored directly in the source code.

Create a .env file in the location expected by the backend.

Use .env.example as the template.

Example:

API_KEY=your_api_key_here

If the project uses a specific provider token, replace the variable with the variable name required by the backend.

Important Security Rule

Never upload .env to GitHub.

Do not publish:

API keys

Access tokens

Passwords

Private credentials

Only .env.example with placeholder values should be committed.

Running the Backend

Open a terminal in the backend directory and activate the virtual environment.

Then run the project's Python entry point.

For a project whose entry point is main.py:

python main.py

If main.py is inside the app package, use the command specified by the project's backend configuration, for example:

python -m app.main

After starting the backend, the terminal will show the local address/port where the application is running.

Example:

http://127.0.0.1:8000

or

http://127.0.0.1:5000

Use the address shown in your terminal.

Opening the Frontend

If the backend serves the frontend automatically, open the local URL shown by the backend.

If the frontend is served separately, open:

frontend/index.html

in a browser or use a local development server such as VS Code Live Server.

How the Project Works

The basic flow is:

User
  ↓
Frontend (HTML/CSS/JavaScript)
  ↓
Backend API
  ↓
Chat / Document / Conversation Services
  ↓
AI Model / API
  ↓
Backend
  ↓
Frontend
  ↓
AI Response

Chat Flow

The user enters a question in the chatbot.

JavaScript sends the request to the backend API.

The backend receives and processes the request.

The configured AI service/model generates a response.

The backend sends the response back to the frontend.

The frontend displays the response in the chat interface.

Backend Modules

api/

Contains API routes/endpoints related to:

Chat

Conversations

Documents

models/

Contains the application's data/database models, including:

Conversations

Messages

Documents

Database configuration

schemas/

Contains data structures used for validating or transferring information between the frontend and backend.

services/

Contains reusable application logic and AI/service-related functionality.

main.py

Acts as the main backend entry point and starts/configures the application.

Frontend Files

index.html

Contains the main chatbot webpage and user interface.

style.css

Contains the visual styling of the chatbot.

script.js

Handles frontend interaction, sending requests to the backend and displaying responses.

Troubleshooting

Chatbot UI opens but does not respond

Check:

The backend terminal is still running.

The frontend is using the correct backend URL.

The required API key/token exists in .env.

The variable name in .env exactly matches the name expected by the backend.

All packages from requirements.txt are installed.

Check the browser Developer Tools Console for frontend errors.

Check the backend terminal for API or Python errors.

ModuleNotFoundError

Run:

pip install -r requirements.txt

Make sure the virtual environment is activated.

API authentication error

Check the API credential in .env. Do not put the real credential inside Python files or GitHub.

Port already in use

If the configured port is already being used, stop the previous server or change the application's port according to its backend configuration.

GitHub Safety

The following should NOT be uploaded:

.env
venv/
VENV/
Include/
Lib/
__pycache__/
*.pyc
pyvenv.env

The following are safe project files to commit:

backend/
frontend/
.gitignore
.env.example
requirements.txt
README.md

Upload uploads/ only when it contains intentional project/demo files required by the application.

Future Improvements

Possible future improvements include:

Better error handling

More AI model options

Persistent conversation history

More document formats

Authentication

Improved UI/UX

Deployment to a cloud platform

Better multimodal input/output support

Author

Developed as an academic/learning project to explore AI chatbot development, frontend-backend integration, API usage, and GitHub-based project management.

License

This project is intended for educational and academic use.