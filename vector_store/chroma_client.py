import chromadb

class ChromaClient:
    def __init__(self,persist_dir:str="chroma_db"):
        self.client=chromadb.PersistentClient(path=persist_dir)

    def get_or_create_collection(self,name:str):
        collection=self.client.get_or_create_collection(name=name)
        return collection
    def add_documents(self,collection,ids,text,embeddings):
        collection.add(ids=ids,documents=text,embeddings=embeddings)
    def search(self,collection,query_embedding,k:int=3):
        results=collection.query(
            query_embedding=[query_embedding],
            n_resuts=k
        )
        return results
