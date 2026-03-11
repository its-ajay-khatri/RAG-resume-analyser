from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.llms import Ollama
from langchain_core.prompts import PromptTemplate


prompt_template = """
You are an AI HR assistant.

Analyze the resume information below.

Resume Content:
{context}

Do the following:

1. Extract all technical skills
2. Extract key projects
3. Suggest best suitable job roles for this candidate

Return response in format:

Skills:
-

Projects:
-

Best Suitable Roles:
-
"""


def run_rag_pipeline(text):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    docs = splitter.create_documents([text])

    embeddings = HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2"
    )

    vector_store = FAISS.from_documents(docs, embeddings)

    retriever = vector_store.as_retriever(search_kwargs={"k": 5})

    query = "Analyze this resume"

    retrieved_docs = retriever.invoke(query)

    context = "\n\n".join([d.page_content for d in retrieved_docs])

    prompt = PromptTemplate(
        template=prompt_template,
        input_variables=["context"]
    )

    llm = Ollama(model="llama3.2:3b")

    final_prompt = prompt.format(context=context)

    response = llm.invoke(final_prompt)

    return response