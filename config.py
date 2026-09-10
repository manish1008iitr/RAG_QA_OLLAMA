class Config:
    def __init__(self):
        self.PDF_PATH = "ais_faq.pdf"
        self.LLM = "llama3.2"
        self.EMBEDDING_MODEL = "nomic-embed-text"
        self.COLLECTION_NAME = "pdf_rag"
        self.CHUNK_SIZE = 800
        self.CHUNK_OVERLAP = 100
        self.TOP_K = 3