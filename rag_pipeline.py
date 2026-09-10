from langchain_ollama import  ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from config import Config
config_data = Config() 

from vector_store import Vector_loading
vector_loader = Vector_loading()

class RAGPipeline():
    def __init__(self, retriever):
        self.llm = ChatOllama(
            model = config_data.LLM,
            temperature = 0
        )

        self.retriever = retriever
        self.prompt = ChatPromptTemplate.from_template("""
                Answer the question using ONLY the context provided below.
                If the answer is not present in the context, say:
                "I don't know based on the PDF."

                Context: {context}
                Question: {question}
                Answer: """)

    def create_answer(self, question):
        documents = self.retriever.invoke(question)
        
        ##combining retrieved texts
        context = "\n\n".join(
        document.page_content for document in documents
        )

        ## Generating prompt 
        format_prompt = self.prompt.invoke({
            "context":context
            "question": question
        })

        ##Generating response 
        response = self.llm.invoke(
            self.format_prompt
        )
        return response.context



    
