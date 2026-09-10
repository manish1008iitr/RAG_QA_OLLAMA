from pdf_loader import PDFLoader
from vector_store import Vector_loading
from rag_pipeline import RAGPipeline
from config import Config
config_data = Config()

class PDF_RAG_Application:
    def __init__(self):
        self.pdf_loader = PDFLoader(
            config_data.PDF_PATH
        )
        self.vector_store = Vector_loading()

    def initialize(self):
        splitted_pdf_data = self.pdf_loader.process_pdf()
        self.vector_store.create_vector_store(splitted_pdf_data)

        retriever = self.vector_store.get_retreiver()

        self.rag_pipleline = RAGPipeline(retriever)

    def run(self):
        self.initialize()
        question = input("Please Entre your question here \n ")
        answer = self.rag_pipleline.ask_question(question)
        print(answer)


if __name__ == "__main__":
    app = PDF_RAG_Application()
    app.run()

