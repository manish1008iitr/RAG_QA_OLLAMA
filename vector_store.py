from langchain_ollama import OllamaEmbeddings 
from langchain_chroma import Chroma
from pdf_loader import Pdf_loader

from config import Config
config_data = Config()

class vector_loading:
    def __init__(self):
        self.embeddings = OllamaEmbeddings(
            model = config_data.EMBEDDING_MODEL
        )
        self.vectorstore = " "
    
    def create_vector_store(self, document):
        self.vectorstore = Chroma.from_documents(
            documents = documnet, 
            embedding = self.embeddings, 
            collection_name = config_data.COLLECTION_NAME
        )

        print(" \n Vector store get created successfully")
    

