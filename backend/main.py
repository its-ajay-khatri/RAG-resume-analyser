import os
import shutil

from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware

from pdf_loader import load_pdf
from image_loader import load_image
from rag_pipeline import run_rag_pipeline


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.post("/analyze-resume")
async def analyze_resume(file: UploadFile = File(...)):

    file_path = f"{UPLOAD_FOLDER}/{file.filename}"                           #save uploaded file to uploads for further vector embaddings and analysis

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    if file.filename.endswith(".pdf"):                                       #if type pdf, prefer this
        text = load_pdf(file_path)

    elif file.filename.endswith((".png", ".jpg", ".jpeg")):                  #if type image, prefer this
        text = load_image(file_path)

    else:
        return {"error": "Unsupported file format"}

    result = run_rag_pipeline(text)                                         #pass the pdf/image loaded text to the RAG pipeline and print the result

    return {"result": result}