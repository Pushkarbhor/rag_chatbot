from fastapi import FastAPI
from rag_chain.chain import RAGChain
from rag_chain.retriever import Retriever

app = FastAPI()

class DummyVectorStore:
    def search(self, query):
        return ["This is a dummy document from vector store"]

class DummyLLM:
    def generate(self, prompt):
        return "This is a dummy answer from the LLM"

vector_store = DummyVectorStore()
retriever = Retriever(vector_store)
llm = DummyLLM()

rag_chain = RAGChain(retriever, llm)

@app.get("/ask")
def ask(question: str):
    answer = rag_chain.run(question)
    return {"answer": answer}
