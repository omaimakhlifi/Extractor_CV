import os
import tempfile
from fastapi import FastAPI, File, HTTPException, UploadFile
from backend.services.docx_parser import extract_text_from_docx
from backend.services.extractor import extract_cv_data
from backend.services.pdf_parser import extract_text_from_pdf


app = FastAPI()

pdf_mime="application/pdf"
docs_mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"

@app.post("/api/v1/upload-cv")
async def upload_cv(file: UploadFile = File(...)):
    file2store = await file.read()
    filename=file.filename
    content_type=file.content_type

    is_pdf= filename.endswith(".pdf") or content_type==pdf_mime
    is_docx= filename.endswith(".docx") or  content_type==docs_mime 

    if not (is_pdf or is_docx):
        raise HTTPException(
            status_code=400,
            detail="Unsupported file type. Please upload a PDF or DOCX file."
        )
    tmp_path = None
    try:
        suffix = ".pdf" if is_pdf else ".docx"
        with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
            tmp_path = tmp.name
            tmp.write(file2store)
        if is_pdf:
            extracted_text = extract_text_from_pdf(tmp_path)
            file_type = "pdf"
        else:
            extracted_text = extract_text_from_docx(tmp_path)
            file_type = "docx"

        return extract_cv_data(extracted_text)

    finally:
        if tmp_path and os.path.exists(tmp_path):
            os.remove(tmp_path)