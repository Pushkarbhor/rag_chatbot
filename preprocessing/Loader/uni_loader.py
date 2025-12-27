import os 
from text_loader import text_loader
from pdf_loader import pdf_loader

def uni_loader(file_path:str)-> str:
    _,ext=os.path.splitext(file_path)
    ext=ext.lower()
    if ext==".txt":
        return text_loader(file_path)
    if ext==".pdf":
        return pdf_loader(file_path)
    else:
        raise ValueError("Please add correct file type")

load=uni_loader(r"data\docs\PDF\faq.pdf")

print(load)