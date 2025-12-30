from fastapi import FastAPI
from rag_chain.chain import RAGChain
from rag_chain.retriever import Retriever
from vector_store.chroma_client import ChromaClient
from sentence_transformers import SentenceTransformer
from langchain_openai import ChatOpenAI
import os

app = FastAPI()

# -----------------------------
# Embedding model
# -----------------------------
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

# -----------------------------
# Vector store (ChromaDB)
# -----------------------------
chroma_client = ChromaClient(persist_dir="chroma_db")
collection = chroma_client.get_or_create_collection(name="rag_documents")

# -----------------------------
# Retriever
# -----------------------------
retriever = Retriever(
    chroma_client=chroma_client,
    collection=collection,
    embedding_model=embedding_model
)

# -----------------------------
# LLM (OpenAI)
# Make sure OPENAI_API_KEY is set
# -----------------------------
llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0
)

# -----------------------------
# RAG Chain
# -----------------------------
rag_chain = RAGChain(retriever, llm)

# -----------------------------
# API endpoint
# -----------------------------
@app.get("/ask")
def ask(question: str):
    answer = rag_chain.run(question)
    return {"answer": answer}
