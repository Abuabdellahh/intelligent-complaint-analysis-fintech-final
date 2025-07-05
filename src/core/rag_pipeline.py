from typing import List, Dict, Any
import pandas as pd
from sentence_transformers import SentenceTransformer
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.llms import HuggingFacePipeline
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline


TARGET_PRODUCTS = ['Credit card', 'Personal loan', 'Buy Now, Pay Later (BNPL)',
                   'Savings account', 'Money transfer']


class RAGPipeline:
    def __init__(self, embedding_model: str = "all-MiniLM-L6-v2"):
        """
        Initialize RAG pipeline with efficient embedding model
        
        Args:
            embedding_model: Name of the embedding model
        """
        self.embeddings = HuggingFaceEmbeddings(model_name=embedding_model)
        self.vector_store = None
        self.llm = None
        self.chain = None

    def create_vector_store(self, data_path: str):
        """
        Create optimized vector store for financial complaints
        
        Args:
            data_path: Path to preprocessed data
        """
        df = pd.read_csv(data_path)
        
        # Filter for target products
        df = df[df['Product'].isin(TARGET_PRODUCTS)]
        
        # Optimal chunking for financial text
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=500,  # Smaller chunks for better context
            chunk_overlap=100
        )
        
        documents = []
        for _, row in df.iterrows():
            chunks = text_splitter.split_text(row['cleaned_narrative'])
            for chunk in chunks:
                documents.append({
                    'text': chunk,
                    'metadata': {
                        'product': row['Product'],
                        'complaint_id': row['Complaint ID']
                    }
                })
        
        self.vector_store = FAISS.from_documents(
            documents=[doc['text'] for doc in documents],
            embedding=self.embeddings,
            metadatas=[doc['metadata'] for doc in documents]
        )
        
        self.vector_store.save_local("../vector_store/faiss_index")

    def initialize_llm(self):
        """
        Initialize optimized LLM for financial analysis
        """
        model_name = "mistralai/Mixtral-8x7B-v0.1"
        
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        model = AutoModelForCausalLM.from_pretrained(
            model_name,
            torch_dtype=torch.float16,
            device_map="auto"
        )
        
        pipe = pipeline(
            "text-generation",
            model=model,
            tokenizer=tokenizer,
            max_length=1024,  # Reduced for efficiency
            temperature=0.7,
            top_p=0.95
        )
        
        self.llm = HuggingFacePipeline(pipeline=pipe)
        
        prompt = PromptTemplate(
            template="""
            You are a financial analyst for CrediTrust. Answer questions about customer complaints 
            using ONLY the provided context. Focus on key financial issues and patterns.
            
            Context: {context}
            Question: {question}
            Answer:
            """,
            input_variables=["context", "question"]
        )
        
        self.chain = LLMChain(llm=self.llm, prompt=prompt)

    def query(self, question: str) -> Dict[str, Any]:
        """
        Efficient query processing with optimized parameters
        
        Args:
            question: User's question
            
        Returns:
            Dictionary with answer and sources
        """
        if not self.vector_store:
            raise ValueError("Vector store not initialized")
        
        if not self.chain:
            raise ValueError("LLM chain not initialized")
        
        docs = self.vector_store.similarity_search(question, k=3)  # Reduced from 5
        context = "\n\n".join([doc['text'] for doc in docs])
        
        answer = self.chain.run({
            "context": context,
            "question": question
        })
        
        return {
            "answer": answer,
            "sources": docs
        }
