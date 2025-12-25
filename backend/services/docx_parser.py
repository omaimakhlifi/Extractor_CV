import re
import unicodedata
from docx import Document



def extract_text_from_docx(path_to_file):
   
    docs_object=open(path_to_file, "rb")
    
    document_reader = Document(docs_object)
    data= " "
    for para in document_reader.paragraphs:

        data+=para.text+"\n"
    data=data.lower()
    data = re.sub(r"\s+", " ", data).strip()
    data = unicodedata.normalize('NFKD', data)
    data = data.encode("ascii", "ignore").decode("utf-8")
    data= u"".join([c for c in data if not unicodedata.combining(c)])

    return data

