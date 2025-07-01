# app.py
import streamlit as st
from PIL import Image
import easyocr
import numpy as np

# OCR Reader
reader = easyocr.Reader(['en'])

# Streamlit UI
st.set_page_config(page_title="OCR App", layout="centered")
st.title("📄 OCR Image to Text")

uploaded_file = st.file_uploader("Image upload karein", type=["png", "jpg", "jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image")

    st.subheader("Extracted Text:")
    result = reader.readtext(np.array(image), detail=0)
    text = "\n".join(result)
    st.code(text)

    st.download_button("Download Text", text.encode(), file_name="output.txt")
