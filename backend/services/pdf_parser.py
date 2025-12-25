import re
import unicodedata
import pdfplumber


def extract_text_from_pdf(path_to_file):
    with pdfplumber.open(path_to_file)as pdf:
      page = pdf.pages[0]
      data = page.extract_text() or ""

    data= data.lower()
    data = re.sub(r"\s+", " ", data).strip()
    data = unicodedata.normalize('NFKD', data)
    data= u"".join([c for c in data if not unicodedata.combining(c)])
    return data