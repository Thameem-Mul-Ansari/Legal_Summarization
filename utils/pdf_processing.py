import io
import fitz
from PIL import Image
import streamlit as st

def display_pdf_content(uploaded_file):
    pdf_file = io.BytesIO(uploaded_file.read())
    doc = fitz.open(stream=pdf_file, filetype="pdf")
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        pix = page.get_pixmap()
        img = Image.open(io.BytesIO(pix.tobytes()))
        st.image(img, caption=f"Page {page_num + 1}", use_container_width=True)
