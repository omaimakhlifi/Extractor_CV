import streamlit as st
import requests

st.title("Application d’Extraction Automatique de CV")
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    st.success("File uploaded!")
    if st.button("Extract"):
        files = {"file": (uploaded_file.name, uploaded_file.getvalue())}
        r = requests.post("http://127.0.0.1:8000/api/v1/upload-cv", files=files)
        
        if r.status_code == 200:
            st.success("Extraction successful!")
            #st.code(r.json())
            st.text_input( "first name", value=r.json().get("nom", ""))
            st.text_input( "last name", value=r.json().get("prenom", ""))
            st.text_input( "email", value=r.json().get("email", ""))
            st.text_input( "phone", value=r.json().get("phone", ""))
            st.text_input( "degree", value=r.json().get("diplome_principal", ""))
            st.download_button("Download extracted data", r.content, file_name="cv.pdf", mime=None)
        else:
            st.error(f"Error: {r.status_code}")
            st.write(r.text)
