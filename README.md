# Intelligent Complaint Analysis for Financial Services

An AI-powered system that transforms raw customer complaint data into actionable insights using RAG (Retrieval-Augmented Generation) technology.

## Project Overview

This project implements a RAG-powered chatbot that helps financial institutions analyze customer complaints across multiple product categories. The system enables internal stakeholders to quickly understand customer pain points and emerging trends through natural language queries.

## Key Features

- Semantic search over customer complaint data
- Multi-product query support (Credit Cards, Personal Loans, BNPL, Savings Accounts, Money Transfers)
- Interactive chat interface with Gradio/Streamlit
- Evidence-based responses with source document citations
- Efficient vector storage using FAISS/ChromaDB
- Robust RAG pipeline implementation

## Project Structure

```
intelligent-complaint-analysis/
├── data/                 # Raw and processed data
├── notebooks/            # Jupyter notebooks for EDA and experimentation
├── src/                 # Source code
│   ├── core/            # Core RAG implementation
│   ├── embeddings/      # Embedding generation logic
│   ├── retrieval/       # Vector store and retrieval logic
│   └── ui/              # Chat interface implementation
├── vector_store/        # Vector database storage
├── tests/               # Test files
├── requirements.txt     # Python dependencies
└── README.md           # Project documentation
```

## Setup Instructions

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Download and preprocess the CFPB complaint dataset
4. Run the preprocessing notebook to clean and filter data
5. Initialize the vector store with embeddings
6. Launch the chat interface

## Usage

1. Start the chat interface:
   ```bash
   python src/ui/app.py
   ```
2. Ask natural language questions about customer complaints
3. Review generated answers and source documents

## Development Workflow

1. Task 1: EDA and Data Preprocessing
   - Analyze complaint data distribution
   - Clean and filter relevant product categories
   - Save processed data

2. Task 2: Text Chunking and Vector Store
   - Implement text chunking strategy
   - Generate embeddings
   - Build vector store

3. Task 3: RAG Pipeline
   - Implement retrieval logic
   - Design prompt templates
   - Integrate LLM for response generation

4. Task 4: Chat Interface
   - Build interactive UI
   - Implement source document display
   - Add streaming support (optional)

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

MIT License

## Acknowledgments

- Consumer Financial Protection Bureau (CFPB) for the dataset
- LangChain for RAG implementation
- FAISS/ChromaDB for vector storage