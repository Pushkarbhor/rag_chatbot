import chromadb

class ChromaClient:
    def __init__(self, persist_dir: str = "chroma_db"):
        self.client = chromadb.Client(
            settings=chromadb.Settings(
                persist_directory=persist_dir
            )
        )

    def get_or_create_collection(self, name: str):
        return self.client.get_or_create_collection(name=name)

    def add_documents(self, collection, ids, documents, embeddings):
        collection.add(
            ids=ids,
            documents=documents,
            embeddings=embeddings
        )

    def search(self, collection, query_embedding, k: int = 3):
        return collection.query(
            query_embeddings=[query_embedding],
            n_results=k
        )
