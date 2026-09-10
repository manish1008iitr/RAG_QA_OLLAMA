import pymupdf4llm as pdf_load
from langchain_text_splitters import RecursiveCharacterTextSplitter 
from config import Config
config_data = Config()

class pdf_loader:
    def __init__(self, pdf_path):
        self.pdf_path = pdf_path
    
    def pdf_loader(self,pdf_path):
        markdown_text = pdf_load.to_markdown(
            self.pdf_path
        )
        return markdown_text
    
    def split_text(self, text):
        splitter = RecursiveCharacterTextSplitter(
            chunk_size = config_data.CHUNK_SIZE,
            chunk_overlap = config_data.CHUNK_OVERLAP
        )
        splitted_document = splitter.create_documents([text])
        return splitted_document

    def process_pdf(self):
        print(" \n Loading PDF....")
        pdf_data = self.pdf_loader(config_data) # Loading of pdf 

        print(" \n Splitting PDF into chunks....")
        splitted_pdf = self.split_text(splitted_pdf) # creation of chunks 
        return splitted_pdf



