from dataclasses import dataclass
from typing import List

@dataclass
class Config:
    # Project Settings
    PROJECT_NAME: str = "Intelligent Complaint Analysis"
    VERSION: str = "1.0.0"
    
    # Data Settings
    DATA_DIR: str = "data"
    RAW_DATA_FILE: str = "consumer_complaints.csv"
    PROCESSED_DATA_FILE: str = "filtered_complaints.csv"
    
    # Embedding Settings
    EMBEDDING_MODEL: str = "sentence-transformers/all-MiniLM-L6-v2"
    CHUNK_SIZE: int = 500
    CHUNK_OVERLAP: int = 100
    
    # LLM Settings
    LLM_MODEL: str = "mistralai/Mixtral-8x7B-v0.1"
    MAX_LENGTH: int = 1024
    TEMPERATURE: float = 0.7
    
    # Vector Store Settings
    VECTOR_STORE_DIR: str = "vector_store"
    VECTOR_STORE_NAME: str = "faiss_index"
    
    # Target Products
    TARGET_PRODUCTS: List[str] = [
        "Credit card",
        "Personal loan",
        "Buy Now, Pay Later (BNPL)",
        "Savings account",
        "Money transfer"
    ]
    
    # UI Settings
    UI_TITLE: str = "Financial Complaint Analysis"
    UI_DESCRIPTION: str = """
    Analyze customer complaints across financial products.
    This tool helps you understand common issues and patterns in customer feedback.
    """
    UI_EXAMPLES: List[str] = [
        "What are common credit card issues?",
        "Why do people complain about BNPL?",
        "Compare savings account complaints",
        "What are the most frequent complaints about money transfers?",
        "Analyze patterns in personal loan complaints"
    ]
