from langchain_chroma import Chroma

def create_vector_store(
        chunks,
        embedding_model,
):
    vectordb = Chroma.from_documents(
        documents=chunks,
        embedding=embedding_model,
        persist_directory="vector_db"
    )
    return vectordb