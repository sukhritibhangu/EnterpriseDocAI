from pathlib import Path
from dotenv import load_dotenv
import os

load_dotenv()

# -------------------------
# Paths
# -------------------------

BASE_DIR = Path(__file__).resolve().parents[2]

UPLOAD_DIR = BASE_DIR / "data" / "uploads"
PROCESSED_DIR = BASE_DIR / "data" / "processed"
CHROMA_DIR = BASE_DIR / "chroma_db"

UPLOAD_DIR.mkdir(parents=True, exist_ok=True)
PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
CHROMA_DIR.mkdir(parents=True, exist_ok=True)

# -------------------------
# API
# -------------------------

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

MODEL_NAME = os.getenv(
    "MODEL_NAME",
    "llama-3.3-70b-versatile"
)

# -------------------------
# RAG Settings
# -------------------------

CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200
TOP_K = 4