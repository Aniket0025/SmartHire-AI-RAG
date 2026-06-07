from langchain_core.prompts import ChatPromptTemplate

def get_skill_prompt():

    prompt = ChatPromptTemplate.from_template(
        """
Extract technical skills from the text.

Return ONLY a comma-separated list.

Text:

{text}
"""
    )

    return prompt