from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session
from sqlalchemy import text
from typing import List
import os

from ..models.database import get_db, engine
from ..models.document import Document, DocumentChunk
from ..schemas.document import DocumentResponse

router = APIRouter()

# Try to create vector extension if using postgres
if "postgres" in str(engine.url):
    try:
        with engine.connect() as conn:
            conn.execute(text("CREATE EXTENSION IF NOT EXISTS vector"))
            conn.commit()
    except Exception as e:
        print(f"Warning: Could not create vector extension automatically. {e}")


@router.post("/upload", response_model=DocumentResponse)
async def upload_document(file: UploadFile = File(...), db: Session = Depends(get_db)):
    if not file.filename.endswith(('.pdf', '.txt', '.docx')):
        raise HTTPException(status_code=400, detail="Unsupported file format. Use PDF, TXT, or DOCX.")

    # Save Document Metadata
    db_doc = Document(
        filename=file.filename,
        file_type=file.content_type or "application/octet-stream",
        status="uploaded"
    )
    db.add(db_doc)
    db.commit()
    db.refresh(db_doc)

    # Save File Locally
    upload_dir = os.path.join(os.path.dirname(__file__), "../../uploads")
    os.makedirs(upload_dir, exist_ok=True)
    file_path = os.path.join(upload_dir, f"{db_doc.id}_{file.filename}")
    
    file_bytes = await file.read()
    with open(file_path, "wb") as f:
        f.write(file_bytes)

    # Note: Processing (Extraction, Chunking, Embeddings) happens in Phase 4.
    # For now, we just store it successfully.
    
    return db_doc

@router.get("", response_model=List[DocumentResponse])
def get_documents(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    docs = db.query(Document).order_by(Document.created_at.desc()).offset(skip).limit(limit).all()
    return docs

@router.get("/{document_id}", response_model=DocumentResponse)
def get_document(document_id: str, db: Session = Depends(get_db)):
    doc = db.query(Document).filter(Document.id == document_id).first()
    if not doc:
        raise HTTPException(status_code=404, detail="Document not found")
    return doc

@router.delete("/{document_id}")
def delete_document(document_id: str, db: Session = Depends(get_db)):
    doc = db.query(Document).filter(Document.id == document_id).first()
    if not doc:
        raise HTTPException(status_code=404, detail="Document not found")
    
    # Delete file from local storage
    upload_dir = os.path.join(os.path.dirname(__file__), "../../uploads")
    file_path = os.path.join(upload_dir, f"{doc.id}_{doc.filename}")
    if os.path.exists(file_path):
        os.remove(file_path)

    # Delete from DB (cascade handles chunks)
    db.delete(doc)
    db.commit()
    
    return {"message": "Document deleted successfully"}
