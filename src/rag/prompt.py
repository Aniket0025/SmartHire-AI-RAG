from langchain_core.prompts import ChatPromptTemplate

def get_prompt():

    prompt = ChatPromptTemplate.from_template(
        """
You are an expert HR Assistant.

Answer ONLY from the provided resume context.

If the answer is not present in the resume,
say "Information not found in resume."

Resume Context:
{context}

Question:
{question}
"""
    )

    return prompt