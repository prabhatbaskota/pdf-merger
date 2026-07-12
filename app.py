# app for pdf-merge
import streamlit as st
import pikepdf

st.title("PDF Merger")

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
        st.download_button(
            "Download merged PDF",
            open("merged.pdf", "rb"),
            "merged.pdf"
        )
    else:
        st.warning("Please upload at least one PDF.")
