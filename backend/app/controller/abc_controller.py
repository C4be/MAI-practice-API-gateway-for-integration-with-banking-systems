from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from typing import List

from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import StreamingResponse
from bson import ObjectId
from app.core.dependencies import mongo_db, mongo_fs
import io
import os
import asyncio
import aiofiles 

router = APIRouter()

# Загружаем файл в MongoDB (GridFS)
@router.post("/abc/upload-from-disk/")
async def upload_file_from_disk(file_path: str):

    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="Файл не найден на сервере")

    filename = os.path.basename(file_path)

    # Читаем файл асинхронно
    async with aiofiles.open(file_path, "rb") as f:
        file_data = await f.read()

    # ✅ Асинхронная загрузка в GridFS
    file_id = await mongo_fs.upload_from_stream(filename, io.BytesIO(file_data))

    return {"file_id": str(file_id), "filename": filename}



# 📌 Получение файла по ID
@router.get("/abc/download/{file_id}")
async def download_file(file_id: str):
    file_id = ObjectId(file_id)
    grid_out = await mongo_fs.open_download_stream(file_id)
    
    if not grid_out:
        raise HTTPException(status_code=404, detail="Файл не найден")

    return StreamingResponse(grid_out, media_type="application/octet-stream", headers={"Content-Disposition": f"attachment; filename={grid_out.filename}"})