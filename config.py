import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    SERPER_API_KEY = os.getenv("SERPER_API_KEY")
    CHROMADB_PATH = os.getenv("CHROMADB_PATH", "./memory/chroma.db")
    MODEL_NAME = "gpt-4o-mini"
    MAX_TOKENS = 4000
