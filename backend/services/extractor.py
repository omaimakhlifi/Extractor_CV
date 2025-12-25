import re
import spacy

from backend.models.cv_result import CvResult

pattern_email = r"\b[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"
pattern_phone = r"\+336\d{8}\b"
degree_keywords = [
    "bachelor",
    "master",
    "doctorate",
    "licence",
    "ingénieur",
    "diplôme",
    "phd",
    "mba",
    "M.S.",
    "B.S.",

]
DEGREE_PATTERNS = [
    r"\b(master|mba|m\.s\.?|msc)\s+(en\s+)?(?P<field>[A-Za-zÀ-ÿ\s]+)",
    r"\b(bachelor|b\.s\.?|licence)\s+(en\s+)?(?P<field>[A-Za-zÀ-ÿ\s]+)",
    r"\b(phd|doctorat|doctorate)\s+(en\s+)?(?P<field>[A-Za-zÀ-ÿ\s]+)",
    r"\b(ingénieur|ingenieur)\s+(en\s+)?(?P<field>[A-Za-zÀ-ÿ\s]+)",
]
nlp = spacy.load("fr_core_news_sm")

def extract_email(text: str) -> str | None:
    match = re.search(pattern_email, text)
    if match:
        return match.group(0)
    return None
def extract_phone(text: str) -> str | None:
    match = re.search(pattern_phone, text)
    if match:
        return match.group(0)
    return None
def extract_name(text):
    doc = nlp(text)
    for ent in doc.ents:
        if ent.label_ == "PER":
            return ent.text
    return None
def extract_degree(text: str):
    for line in text.split("\n"):
        for pattern in DEGREE_PATTERNS:
            match = re.search(pattern, line, re.IGNORECASE)
            if match:
                degree = match.group(0).capitalize()
                field = match.group("field").strip()
                return f"{degree} {field}"

    return None

def extract_cv_data(text: str) -> dict:
    email = extract_email(text)
    phone = extract_phone(text)
    name = extract_name(text)
    diplome_principal = extract_degree(text)

    
    return CvResult(
        nom=name or "",   
        prenom=None,
        email=email or "",
        telephone=phone or "",
        diplome_principal= diplome_principal or "",
    )

        

