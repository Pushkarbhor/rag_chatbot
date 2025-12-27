from preprocessing.loaders.uni_loader import uni_loader
from preprocessing.loaders.text_clean import text_clean
from preprocessing.chunker.chunkers import chunk_text
from preprocessing.embeddings.embedder import EmbeddingManager
from vector_store.chroma_client import ChromaClient

#1) Load Docs 
doc_path="data\docs\PDF\product_manual.pdf"
raw =uni_loader(doc_path)

#2) clean
clean=text_clean(raw)

#3) Chunk
chunks=chunk_text(clean)

print(f"Total Chunks: {len(chunks)}")

#4)embed Chunks
embedder=EmbeddingManager()
chunk_vectors=embedder.generate_embeddings(chunks)

#5) Initialzing Chroma DB 
chroma=ChromaClient()
collection=chroma.get_or_create_collection("rag_collection")

#6) Create ids 
ids=[f"chunks_{i}" for i in range(len(chunks))]

#7) add to DB 
chroma.add_documents(collection,ids,chunks,chunk_vectors)

print("Inserted into ChromaDB successfully")
