# app for pdf-merge and image-to-pdf with minimalistic theme
import streamlit as st
import pikepdf
from PIL import Image

# --- Page setup ---
st.set_page_config(page_title="PDF Worker", page_icon="📄", layout="centered")

# --- Custom minimalistic style ---
st.markdown(
    """
    <style>
    /* Overall background and font */
    body {
        background-color: #fafafa;
        font-family: 'Inter', sans-serif;
    }
    /* Headings */
    h1, h2, h3 {
        color: #333333;
        font-weight: 600;
    }
    /* Buttons */
    .stButton>button {
        background-color: #333333;
        color: white;
        border-radius: 6px;
        padding: 0.5em 1.2em;
        font-weight: 500;
    }
    .stButton>button:hover {
        background-color: #555555;
    }
    /* File uploader */
    .stFileUploader {
        border: 1px solid #dddddd;
        border-radius: 6px;
        padding: 0.5em;
        background-color: #ffffff;
    }
    /* Footer */
    footer {
        visibility: hidden;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- App content ---
st.title("PDF Worker")

st.header("📄 PDF Merger")
uploaded_files = st.file_uploader(
    "Upload PDFs to merge",
    type="pdf",
    accept_multiple_files=True
)

if st.button("Merge PDFs"):
    if uploaded_files:
        merged = pikepdf.Pdf.new()
        for f in uploaded_files:
            pdf = pikepdf.Pdf.open(f)
            merged.pages.extend(pdf.pages)
        merged.save("merged.pdf")
        st.success("Merged successfully!")
        st.download_button("Download merged PDF", open("merged.pdf", "rb"), "merged.pdf")
    else:
        st.warning("Please upload at least one PDF.")

st.header("🖼️ Image to PDF Converter")
image_files = st.file_uploader(
    "Upload images to convert",
    type=["jpg", "jpeg", "png"],
    accept_multiple_files=True
)

if st.button("Convert Images to PDF"):
    if image_files:
        images = [Image.open(img).convert("RGB") for img in image_files]
        images[0].save("images.pdf", save_all=True, append_images=images[1:])
        st.success("Images converted successfully!")
        st.download_button("Download PDF", open("images.pdf", "rb"), "images.pdf")
    else:
        st.warning("Please upload at least one image.")

# --- Developer credit ---
st.markdown(
    """
    ---
    <p style='text-align:center; color:#555555;'>
    Developed by <b>Prabhat Baskota</b> · © 2026 · Built with Streamlit, PikePDF & Pillow
    </p>
    """,
    unsafe_allow_html=True
)
