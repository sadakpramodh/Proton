import fitz
import PyPDF2
import pytesseract
from pdf2image import convert_from_path

class PDFReader:
    def __init__(self, file_path):
        self.file_path = file_path

    def check_pdftype(file_path):
        # check weather pdf is OCR based or text based
        doc = fitz.open(file_path)
        for page in doc:
            if len(page.get_text()) == 0:
                print("This page is an image")
            else:
                print("This page contains text")

    def check_password(file_path, password):
        with open(file_path, 'rb') as f:
            pdf = PyPDF2.PdfFileReader(f)
            if pdf.isEncrypted:
                try:
                    pdf.decrypt(password)
                    return True
                except PyPDF2.utils.PdfReadError:
                    return False
            else:
                return False
            
    # Function to read PDF that are in image format and convert to text
    def read_pdf_image(pdf_path):
        images = convert_from_path(pdf_path)
        text = ""
        for page in images:
            text += pytesseract.image_to_string(page)
        return text
    # Function to read PDF and convert to text
    def read_pdf_text(pdf_path):
        doc = fitz.open(pdf_path)
        text = ""
        for page in doc:
            text += page.get_text()
        return text
 