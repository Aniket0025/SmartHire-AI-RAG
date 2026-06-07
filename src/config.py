import os
from dotenv import load_dotenv

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

##print(f"OPENROUTER_API_KEY: {OPENROUTER_API_KEY}")