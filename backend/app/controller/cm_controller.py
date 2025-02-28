from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from typing import List

router = APIRouter()

@router.get('api/v1/cm/')
def get_all_users_documents():
    pass

@router.delete('/api/v1/cm/')
def delete_document_by_id():
    pass