import chainlit as cl
import Readers.read_documents as reader
import textSplitter

def store_files(file):
    # Save the file in temp location
    file_path = f"tmp\{file.name}"
    with open(file_path, "wb") as f:
        f.write(file.content)
        f.close()
        # print(file_path)
        # print(file.name)
        # print(file.content)
    return file_path

def select_reader(file_path):
    # load the pdf from the temp location and process the contents
    # load the pdf from the temp location and process the contents
    mime_type = reader.guess_type(file_path)
    if mime_type == "application/pdf":
        check_password = reader.PDFReader.check_password(file_path)
        if check_password:
            return "currently we are not supporting the password protected file :("
        else:
            return reader.PDFReader.read_pdf_text(file_path)
        
def split_text(text):
    # Split the text into chunks
    texts = textSplitter.split_text(text)
    return texts





