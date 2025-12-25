# Extractor_CV
Installation: 
 pip install streamlit fastapi uvicorn pydantic pdfplumber python-docx spacy
Lancement local:
 Backend:
   python -m uvicorn backend.main:app --reload
 Frontend:
  streamlit run app.py
  
Lancement Docker:
 backend:
   docker build -f docker/Dockerfile.backend -t cv-extractor-backend .
   docker run -p 8000:8000 cv-extractor-backend
 frontend:
   docker build -f docker/Dockerfile.frontend -t cv-extractor-frontend .
   docker run -p 8501:8501 cv-extractor-frontend



exemples d’API: 
 
<p align="center">
  <img src="images/upload.png" width="700" alt="Installation and run">
</p>
<p align="center">
  <img src="images/display.png" width="700" alt="Installation and run">
</p>
<p align="center">
  <img src="images/download.png" width="700" alt="Installation and run">
</p>
 
      
