import fitz  # fitz for PDF extraction

def extract_text_from_pdf(pdf_file):
    """
    Extracts text from an uploaded PDF file.

    Parameters:
    pdf_file (UploadedFile): The uploaded PDF file.

    Returns:
    str: Extracted text from the PDF.
    """
    document = fitz.open(stream=pdf_file.read(), filetype="pdf")
    text = ""
    for page_num in range(len(document)):
        page = document.load_page(page_num)
        text += page.get_text("text")
    return text
