import re 

def text_clean(text:str)->str:
    #1 converting into string 
    text=str(text)
    #2 removing tab space
    text=text.replace("\t"," ")
    #3 removing symbols
    text= re.sub(r"[•■▪◆●►]"," ",text)
    #4 removing multiple spaces 
    text=re.sub("\s+"," ",text)
    #5 removing strting and ending spaces 
    text=text.strip()
    #6 normalize new line 
    text=re.sub(r"\n+","\n",text)

    return text


#TEST

#if __name__ =="__main__":
    sample ="""
    • Hello     world

    This   is    a     test.

    ► New line here
    """
    print(text_clean(sample))


#Connect Loader +Cleaner
 
#from uni_loader import uni_loader

#raw=uni_loader("data\docs\PDF\product_manual.pdf")
#clean=text_clean(raw)

#print(clean[:500])