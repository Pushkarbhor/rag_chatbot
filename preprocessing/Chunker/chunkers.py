def chunk_text(
    text:str,
    chunk_size:int =500,
    chunk_overlap:int=100
)-> list[str]:
    chunks=[]
    start=0
    text_length=len(text)

    while start<text_length:
        end =start+chunk_size
        chunk=text[start:end]
        chunks.append(chunk)

        #increment 
        start=start+chunk_size-chunk_overlap
    return chunks

#if __name__ == "__main__":
    sample="This is an example test running to see chunks are getting cut correctly and running without error"

    chunks=chunk_text(sample,chunk_size=10,chunk_overlap=5)
    for i, c in enumerate(chunks,1):
        print(f"chunk {i}:{c}")
       