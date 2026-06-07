from langchain_openai import ChatOpenAI

from src.config import OPENROUTER_API_KEY

def get_llm():
    llm = ChatOpenAI(
        model="deepseek/deepseek-chat",
        api_key=OPENROUTER_API_KEY,
        base_url="https://openrouter.ai/api/v1",
        temperature=0
    )

    return llm