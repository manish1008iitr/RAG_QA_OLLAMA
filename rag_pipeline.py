from langchain_ollama import  ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from config import Config
config_data = Config() 

from vectorstore import Vector_loading
vector_loader = Vector_loading()

class prompt_make:
    def __init__(self, context):
        self.question = " "
        self.context  = context
        self.format_promt = " "

    def prompt_making():
        question = input("Please type your question here \n ")
        self.prompt = ChatPromptTemplate.from_template("""
                    Answer the question using ONLY the context provided below.
                    If the answer is not present in the context, say:
                    "I don't know based on the PDF."
                    Context:
                    {context}
                    Question:
                    {question}
                    Answer:
                    """
        )
        format_prompt = prompt.invoke(
        {
            "context": self.context, 
            "question": self.question
        }
    )
        return self.format_prompt

class RAGPipeline(prompt_make):
    def __init__(self):
        self.llm = ChatOllama(
            model = config_data.LLM,
            temperature = 0
        )
    
    def create_answer():
        response = self.llm.invoke(
            
        )



    
