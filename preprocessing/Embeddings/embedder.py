import numpy as np
from sentence_transformers import SentenceTransformer
from typing import List , Union , Dict

class EmbeddingManager:
    def __init__(self,model_name:str="all-MiniLM-L6-v2"):
        self.model_name=model_name
        self.model=None
        self._load_model()
    def _load_model(self):
        try:
            print("Model is Loading",self.model_name)
            self.model=SentenceTransformer(self.model_name)
            print(f"Model is Loaded Successfuly, Model Diementions are:{self.model.get_sentence_embedding_dimension()}")
        except Exception as e:
            print(f"error While Loading:{self.model}")
            raise
    def generate_embeddings(self,text:List[str])->np.ndarray:
        if not self.model:
            raise ValueError("Mdel Not loaded")
        print(f"Generating Embedding for {len(text)}Texts...")
        embeddings=self.model.encode(text,show_progress_bar=True)
        print(f"Generated Embeddings with shape:{embeddings.shape}")
        return embeddings

embedding_manager=EmbeddingManager()
#Test
sample = ["this is a test", "reset your password"]
vecs = embedding_manager.generate_embeddings(sample)