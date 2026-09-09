import pymupdf4llm 
from langchain_text_splitters import RecursiveCharacterTextSplitter 
from langchain_ollama import OllamaEmbeddings, ChatOllama 
from langchain_chroma import Chroma
from langchain_core.prompts import ChatPromptTemplate

pdf_path = "ais_faq.pdf"
text = pymupdf4llm.to_markdown(pdf_path)

splitter = RecursiveCharacterTextSplitter(
    chunk_size = 800, 
    chunk_overlap = 100
)

chunks = splitter.create_documents([text])
print(len(chunks))


embeddings = OllamaEmbeddings(
    model = "nomic-embed-text"
)

vectorstore = Chroma.from_documents(
    documents = chunks, 
    embedding = embeddings, 
    collection_name = "pdf_rag"
)

retriever = vectorstore.as_retriever(
    search_kwargs = {"k":1}
)

llm = ChatOllama(
    model="llama3.2"
)

question = ""

prompt = ChatPromptTemplate.from_template("""
Answer the question using ONLY the context provided below.

If the answer is not present in the context, say:
"I don't know based on the PDF."

Context:
{context}

Question:
{question}

Answer:
""")

while True:
    question = input("Ask a question or can type exit to exit \\n")
    if question.lower() == "exit":
        break 
    documents = retriever.invoke(question)
    context = "\n\n".join(
        doc.page_content for doc in documents
    )

    format_prompt = prompt.invoke(
        {
            "context": context, 
            "question": question
        }
    )
    # print(f"Your question is {question} \n\n")
    # print(f"And your prompt is {format_prompt} \n\n")
    # print(f"And your matched documnet was this {documents} \n\n")
    # print(f"And context recieved is this: {context} \n\n")
    response = llm.invoke(format_prompt)
    print("Here is your answer\n\n\n" + response.content)