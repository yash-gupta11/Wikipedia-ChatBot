from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate
from langchain_huggingface import HuggingFaceEmbeddings
import wikipediaapi
from langchain_ollama.llms import OllamaLLM


wiki_wiki = wikipediaapi.Wikipedia(user_agent='MyProjectName (merlin@example.com)', language='en')


print('yash')

name = input('Please enter the Title of the Wikipedia Page : ')
page_py = wiki_wiki.page(name)

if page_py.exists() == False:
    print('Page does not exist')
    exit()

data = page_py.text


splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
chunks = splitter.create_documents([data])

embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
vector_store = FAISS.from_documents(chunks, embeddings)


retriever = vector_store.as_retriever(search_type="similarity", search_kwargs={"k": 4})

llm = OllamaLLM(model="phi3.5")


prompt = PromptTemplate(
    template="""
      You are a wikipedia Page assistant.
      Answer ONLY from the provided page content context.
      If the context is insufficient, just say you don't know.

      {context}
      Question: {question}
    """,
    input_variables = ['context', 'question']
)

question          = input('Enter your query : ')
retrieved_docs    = retriever.invoke(question)

context_text = "\n\n".join(doc.page_content for doc in retrieved_docs)

final_prompt = prompt.invoke({"context": context_text, "question": question})

answer = llm.invoke(final_prompt)
print(answer)