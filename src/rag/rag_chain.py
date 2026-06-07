from langchain_core.runnables import (
    RunnablePassthrough
)

from langchain_core.output_parsers import (
    StrOutputParser
)

from src.rag.prompt import get_prompt


def create_rag_chain(
    retriever,
    llm
):

    prompt = get_prompt()

    chain = (
        {
            "context": retriever,
            "question": RunnablePassthrough()
        }
        | prompt
        | llm
        | StrOutputParser()
    )

    return chain