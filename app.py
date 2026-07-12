# app for pdf-merge and image-to-pdf
import streamlit as st
import pikepdf
from PIL import Image

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

# 🖼️ Image to PDF converter
st.header("🖼️ Image to PDF Converter")
image_files = st.file_uploader(
    "Upload images to convert",
    type=["jpg", "jpeg", "png"],
    accept_multiple_files=True
)

if st.button("Convert Images to PDF"):
    if image_files:
        images = []
        for img in image_files:
            image = Image.open(img).convert("RGB")
            images.append(image)
        images[0].save("images.pdf", save_all=True, append_images=images[1:])
        st.success("Images converted successfully!")
        st.download_button("Download PDF", open("images.pdf", "rb"), "images.pdf")
    else:
        st.warning("Please upload at least one image.")

# Developer credit
st.markdown(
    """
    ---
    **Developed by [Prabhat Baskota](https://github.com/prabhatbaskota)**  
    © 2026 | Built with Streamlit, PikePDF & Pillow
    """,
    unsafe_allow_html=True
)
