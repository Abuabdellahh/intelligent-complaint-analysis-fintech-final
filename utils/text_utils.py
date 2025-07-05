import re
from typing import List, Dict, Any
from config.config import Config


class TextUtils:
    @staticmethod
    def clean_text(text: str) -> str:
        """
        Clean and normalize text for processing
        
        Args:
            text: Input text to clean
            
        Returns:
            Cleaned text
        """
        if not text:
            return ""
            
        # Convert to lowercase
        text = text.lower()
        
        # Remove special characters and numbers
        text = re.sub(r'[^\w\s]', '', text)
        
        # Remove extra whitespace
        text = ' '.join(text.split())
        
        return text

    @staticmethod
    def format_source_document(doc: Dict[str, Any]) -> str:
        """
        Format a source document for display
        
        Args:
            doc: Document dictionary containing text and metadata
            
        Returns:
            Formatted string representation of the document
        """
        return f"""
Product: {doc['metadata']['product']}
Complaint ID: {doc['metadata']['complaint_id']}
{'-'*80}
{doc['text']}
{'-'*80}
"""

    @staticmethod
    def format_error_message(error: Exception) -> str:
        """
        Format error message for user display
        
        Args:
            error: Exception object
            
        Returns:
            User-friendly error message
        """
        return f"Error: {str(error)}. Please try again with a different query."

    @staticmethod
    def validate_product(product: str) -> bool:
        """
        Validate if a product is in the target products list
        
        Args:
            product: Product name to validate
            
        Returns:
            True if valid, False otherwise
        """
        return product in Config.TARGET_PRODUCTS

    @staticmethod
    def split_text(text: str, chunk_size: int = Config.CHUNK_SIZE, 
                  chunk_overlap: int = Config.CHUNK_OVERLAP) -> List[str]:
        """
        Split text into chunks with overlap
        
        Args:
            text: Input text to split
            chunk_size: Size of each chunk
            chunk_overlap: Overlap between chunks
            
        Returns:
            List of text chunks
        """
        words = text.split()
        chunks = []
        
        if len(words) <= chunk_size:
            return [text]
            
        for i in range(0, len(words), chunk_size - chunk_overlap):
            chunk = words[i:i + chunk_size]
            chunks.append(' '.join(chunk))
            
        return chunks
