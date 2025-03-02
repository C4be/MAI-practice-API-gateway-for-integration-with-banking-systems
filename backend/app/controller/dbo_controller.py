from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from app.core.dependencies import get_db
from pydantic import BaseModel
from typing import List
from app.dto.fio_request import FIORequest
from app.service.document_service import DocumentService
from app.core.logger import setup_logger
import shutil

# Настроенный логгер
logger = setup_logger()

router = APIRouter()

@router.get('/dbo/doc/{id}')
def get_doc_by_id(id: int, db: Session = Depends(get_db)):
    logger.warning("Жопа")
    document_service = DocumentService(db)
    doc = document_service.get_doc_by_id(id)
    if not doc:
        raise HTTPException(status_code=404, detail="Document not found")
    return doc

@router.get('/dbo/find/user/documents/all')
def get_all_user_documents(fio_request: FIORequest, db: Session = Depends(get_db)):
    # Доступ к данным из тела запроса через объект fio_request
    first_name = fio_request.first_name
    last_name = fio_request.last_name
    middle_name = fio_request.middle_name
    logger.warning("Жопа")
    logger.warning(f'{first_name} {last_name} {middle_name}')
    
    document_service = DocumentService(db)
    docs = document_service.get_documents_by_FIO(first_name, last_name, middle_name)
    
    if not docs:
        raise HTTPException(status_code=404, detail="Documents not found")
    return docs
    
@router.post('/dbo/load_document')
def load_document(file: UploadFile = File(...)):
    file_location = f'app/resources/files/{file.filename}'
    
    # Сохраняем файл
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    # Возвращаем ответ с подтверждением
    return JSONResponse(content={"message": f"File '{file.filename}' saved at '{file_location}'"})