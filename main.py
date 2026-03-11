import os

from loaders.pdf_loader import load_pdf
from loaders.image_loader import load_image

from rag.embeddings import chunk_text, get_embeddings
from rag.vector_store import create_vector_store
from rag.retriever import get_retriever
from rag.chain import generate_response


def read_file(file_path):

    if file_path.endswith(".pdf"):
        return load_pdf(file_path)

    elif file_path.endswith((".png", ".jpg", ".jpeg")):
        return load_image(file_path)

    else:
        raise Exception("Unsupported file format")


def main():

    file_path = "resume/resume.pdf"

    text = read_file(file_path)

    chunks = chunk_text(text)

    embeddings = get_embeddings()

    vector_store = create_vector_store(chunks, embeddings)

    retriever = get_retriever(vector_store)

    query = "Analyze this resume and suggest best job roles"

    docs = retriever.invoke(query)

    result = generate_response(query, docs)

    print("\nAI Resume Analysis\n")
    print(result)


if __name__ == "__main__":
    main()