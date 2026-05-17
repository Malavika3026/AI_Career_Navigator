from dotenv import load_dotenv
import os

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

MODEL_NAME = "llama-3.1-8b-instant"

# Embedding model
EMBEDDING_MODEL = "all-MiniLM-L6-v2"

# Matching weights
SKILL_WEIGHT = 0.7
EXPERIENCE_WEIGHT = 0.3

SIMILARITY_THRESHOLD = 0.6