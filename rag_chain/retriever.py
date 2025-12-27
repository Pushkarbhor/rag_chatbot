class Retriever:
    def __init__(self, vector_store):
        self.vector_store = vector_store

    def retrieve(self, query: str):
        """
        Retrieve relevant documents from vector store
        """
        results = self.vector_store.search(query)
        return results
