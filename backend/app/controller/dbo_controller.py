from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.dependencies import get_db
from pydantic import BaseModel
from typing import List

from app.service.document_service import DocumentService

router = APIRouter()

@router.get('/dbo/doc/{id}')
def get_doc_by_id(id: int, db: Session = Depends(get_db)):
    document_service = DocumentService(db)
    doc = document_service.get_doc_by_id(id)
    if not doc:
        raise HTTPException(status_code=404, detail="Document not found")
    return doc

@router.get('/dbo/user/{user_id}/documents')
def get_all_users_documents():
    pass

@router.delete('/dbo/documents/{doc_id}')
def delete_document_by_id():
    pass