from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from typing import List

router = APIRouter()

@router.get('/dbo/user/test')
def get_all_users_documents():
    return "Hello"

@router.get('/dbo/user/{user_id}/documents')
def get_all_users_documents():
    pass

@router.delete('/dbo/documents/{doc_id}')
def delete_document_by_id():
    pass