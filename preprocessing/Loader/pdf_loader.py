from pypdf import PdfReader

def pdf_loader(file_path:str)->str:
    reader=PdfReader(file_path)
    text="" 
    for page in reader.pages:
        page_text=page.extract_text()
        if page_text:
            text+=page_text + "\n"
    return text

read=pdf_loader("data\docs\PDF\support_docs.pdf")
print(read)