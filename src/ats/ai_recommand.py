from langchain_core.prompts import ChatPromptTemplate

recommend_prompt = ChatPromptTemplate.from_template(
    """
    ATS Score: {score}

    Missing Skills:
    {skills}

    Give recommendations.
    """
)