# app for pdf-merge and image-to-pdf with animated reactive background
import streamlit as st
import pikepdf
from PIL import Image

st.set_page_config(page_title="PDF Worker", page_icon="📄", layout="centered")

# --- Animated gradient + gentle mouse movement ---
st.markdown(
    """
    <style>
    @keyframes gradientShift {
        0% {background-position: 0% 50%;}
        50% {background-position: 100% 50%;}
        100% {background-position: 0% 50%;}
    }

    body {
        background: linear-gradient(-45deg, #f8f9fa, #e9ecef, #f1f3f5, #dee2e6);
        background-size: 400% 400%;
        animation: gradientShift 20s ease infinite;
        font-family: 'Inter', sans-serif;
        color: #333333;
        transition: background-position 0.2s ease;
    }

    h1, h2 {
        color: #222222;
        font-weight: 600;
    }

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

    .stFileUploader {
        border: 1px solid #dddddd;
        border-radius: 6px;
        padding: 0.5em;
        background-color: #ffffff;
    }
    </style>

    <script>
    document.addEventListener('mousemove', function(e) {
        const x = e.clientX / window.innerWidth;
        const y = e.clientY / window.innerHeight;
        document.body.style.backgroundPosition = `${x*100}% ${y*100}%`;
    });
    </script>
    """,
    unsafe_allow_html=True
)

# --- App content ---
st.title("PDF Worker")

st.header("📄 PDF Merger")
uploaded_files = st.file_uploader("Upload PDFs to merge", type="pdf", accept_multiple_files=True)

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
image_files = st.file_uploader("Upload images to convert", type=["jpg", "jpeg", "png"], accept_multiple_files=True)

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
