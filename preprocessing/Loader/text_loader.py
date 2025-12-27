def text_loader(file_path:str)->str:
    with open (file_path,"r",encoding="utf-8") as f:
        return f.read()


read=text_loader("data\docs\Text\sample_faq.txt")

print(read)
