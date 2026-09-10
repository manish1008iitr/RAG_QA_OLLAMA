# RAG_QA_OLLAMA

A modular Retrieval-Augmented Generation (RAG) application that allows users to ask questions about the contents of a PDF document using a locally hosted Large Language Model (LLM) through Ollama.

The project demonstrates how PDF documents can be processed, converted into vector representations, retrieved based on semantic relevance, and supplied as context to an LLM for generating answers.

# Overview

Large Language Models can generate impressive responses, but they may not have access to information contained in a user's private or domain-specific documents.

This project addresses that problem using a Retrieval-Augmented Generation pipeline.

The application follows the workflow:

PDF Document
     │
     ▼
PDF Loading & Text Extraction
     │
     ▼
Text Chunking
     │
     ▼
Embeddings Generation
     │
     ▼
Vector Store
     │
     ▼
Semantic Retrieval
     │
     ▼
Relevant Context
     │
     ▼
Ollama LLM
     │
     ▼
Generated Answer

The complete application is implemented using a modular Python architecture, making each stage of the RAG pipeline easier to understand, maintain, and extend.

# Key Features
    PDF-based Question Answering
    Retrieval-Augmented Generation (RAG)
    Local LLM inference using Ollama
    Embedding-based semantic retrieval
    Vector-store based document search



# Tech Stack \
Technology                  Purpose \
Python	                    Application development \
Ollama	                    Local LLM inference \
Llama 3.2	                Text generation \
Nomic Embed Text	        Text embeddings \
Vector Store	            Semantic document retrieval \
RAG	Retrieval +             generation architecture \
Object-Oriented             Programming	Modular application design \


# Prerequisites

Before running the project, make sure you have: \
    Python 3.9+ \
    Ollama \
    Required Python packages \
    A local Ollama model \
    A PDF document \

# Installation
1. Clone the Repository
git clone https://github.com/manish1008iitr/RAG_QA_OLLAMA.git

2. Create a Virtual Environment: python -m venv venv \
Activate it on Windows: venv\Scripts\activate \
On macOS/Linux: source venv/bin/activate

3. Install Dependencies
Install the required Python libraries used by the project:
pip install -r requirements.txt

# Ollama Setup 
Install Ollama on your computer and verify that it is available: \
ollama --version \
Pull the LLM used by the project: \
ollama pull llama3.2 \

Pull the embedding model:
ollama pull nomic-embed-text

Verify the installed models:
ollama list

The project configuration currently expects: llama3.2, nomic-embed-text

# Add Your PDF
The current configuration expects a PDF named: ais_faq.pdf
Place the PDF in the project directory: Alternatively, update the PDF_PATH parameter in config.py:
self.PDF_PATH = "your_document.pdf"

# Run the Application
Start the application using: python main.py
You will be prompted to enter a question: "Please Enter your question here"

Enter your question about the PDF.
The application will retrieve relevant information from the document and generate an answer using the locally hosted LLM.

# Example 

Suppose the PDF contains information about an organization.
You could ask: What are the major services provided by the organization?

The architecture can be adapted for: \
    Academic document Q&A \
    Company policy assistants \
    FAQ systems \
    Research paper Q&A \
    Technical documentation assistants \
    Internal knowledge assistants \
    Business document analysis \

# Future Improvements \
    Support for multiple PDFs \
    Streamlit/Gradio user interface \
    Conversational chat history \
    Source-document citations \
    Multiple document formats \
    Improved retrieval strategies \
    RAG evaluation metrics \
    Retrieval and generation logging \
    REST API using FastAPI \
    Docker deployment \
    Document upload interface \





