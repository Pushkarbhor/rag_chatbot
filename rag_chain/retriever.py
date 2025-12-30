# rag_chain/retriever.py

class Retriever:
    def __init__(self, chroma_client, collection, embedding_model):
        """
        chroma_client: instance of ChromaClient
        collection: the name or object of the Chroma collection
        embedding_model: a sentence-transformer model to encode queries
        """
        self.chroma_client = chroma_client
        self.collection = collection
        self.embedding_model = embedding_model

    def retrieve(self, query: str, k: int = 3):
        """
        Retrieve top-k relevant documents from ChromaDB
        """
        # Encode query into embedding
        query_embedding = self.embedding_model.encode(query).tolist()

        # Search ChromaDB
        results = self.chroma_client.search(
            collection=self.collection,
            query_embedding=query_embedding,
            k=k
        )

        return results
