import os
from docx import Document
import PyPDF2

def read_docx(file_path):
    """Reads a .docx file and returns the text content."""
    try:
        doc = Document(file_path)
        text = []
        for paragraph in doc.paragraphs:
            text.append(paragraph.text)
        return '\n'.join(text)
    except Exception as e:
        return f"Error reading .docx file: {e}"

def read_pdf(file_path):
    """Reads a .pdf file and returns the text content."""
    try:
        with open(file_path, 'rb') as pdf_file:
            reader = PyPDF2.PdfReader(pdf_file)
            text = []
            for page in reader.pages:
                text.append(page.extract_text())
            return '\n'.join(text)
    except Exception as e:
        return f"Error reading .pdf file: {e}"

def read_document(file_path):
    """Determines the file type and reads the document accordingly."""
    if not os.path.exists(file_path):
        return "File not found. Please check the file path."

    _, file_extension = os.path.splitext(file_path)

    if file_extension.lower() == '.docx':
        return read_docx(file_path)
    elif file_extension.lower() == '.pdf':
        return read_pdf(file_path)
    else:
        return "Unsupported file format. Please use .docx or .pdf."