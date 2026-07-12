# app for PDF merge, image-to-PDF, and PDF split/insert
import streamlit as st
import pikepdf
from PIL import Image

st.set_page_config(page_title="PDF Worker", page_icon="📄", layout="centered")

st.title("PDF Worker")

# --- PDF Merger ---
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

# --- Image to PDF ---
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

# --- PDF Split & Insert ---
st.header("✂️ Split & Insert PDF")
split_pdf = st.file_uploader("Upload a PDF to split", type="pdf")
insert_pdf = st.file_uploader("Upload another PDF to insert", type="pdf")
start_page = st.number_input("Start page to split (1-indexed)", min_value=1, step=1)
end_page = st.number_input("End page to split (inclusive)", min_value=1, step=1)

if st.button("Split and Insert"):
    if split_pdf and insert_pdf:
        base = pikepdf.Pdf.open(split_pdf)
        insert = pikepdf.Pdf.open(insert_pdf)
        # Split the base PDF
        part1 = base.pages[:start_page - 1]
        part2 = base.pages[end_page:]
        # Create new PDF and insert
        new_pdf = pikepdf.Pdf.new()
        new_pdf.pages.extend(part1)
        new_pdf.pages.extend(insert.pages)
        new_pdf.pages.extend(part2)
        new_pdf.save("modified.pdf")
        st.success("PDF split and insertion completed!")
        st.download_button("Download modified PDF", open("modified.pdf", "rb"), "modified.pdf")
    else:
        st.warning("Please upload both PDFs and specify page range.")

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
