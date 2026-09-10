import pymupdf4llm 
from langchain_text_splitters import RecursiveCharacterTextSplitter 
from config import Config
config_data = Config()

class PDFLoader:
    def __init__(self, pdf_path):
        self.pdf_path = pdf_path
    
    def pdf_loader(self):
        markdown_text = pymupdf4llm.to_markdown(
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
        pdf_markdown_data = self.pdf_loader() # Loading of pdf 

        print(" \n Splitting PDF into chunks....")
        splitted_pdf_text = self.split_text(pdf_markdown_data) # creation of chunks 
        return splitted_pdf_text



