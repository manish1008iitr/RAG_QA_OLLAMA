from langchain_ollama import OllamaEmbeddings 
from langchain_chroma import Chroma

from config import Config
config_data = Config()

class Vector_loading:
    def __init__(self):
        self.embeddings = OllamaEmbeddings(
            model = config_data.EMBEDDING_MODEL
        )
        self.vectorstore = " "
    
    def create_vector_store(self, document):
        print(" \n Creating Vector store.... ")
        self.vectorstore = Chroma.from_documents(
            documents = document, 
            embedding = self.embeddings, 
            collection_name = config_data.COLLECTION_NAME
        )

        print(" \n Vector store get created successfully")

    def get_retreiver(self):
        return self.vectorstore.as_retriever(
            search_kwargs = {
                "k":config_data.TOP_K
            }
        )
    

