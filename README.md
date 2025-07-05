# Intelligent Complaint Analysis for Financial Services

An AI-powered system that transforms raw customer complaint data into actionable insights using RAG (Retrieval-Augmented Generation) technology.

## 🚀 Project Overview

This project implements a RAG-powered chatbot that helps financial institutions analyze customer complaints across multiple product categories. The system enables internal stakeholders to quickly understand customer pain points and emerging trends through natural language queries.

## 🎯 Key Features

- 🤖 Semantic search over customer complaint data
- 📊 Multi-product query support (Credit Cards, Personal Loans, BNPL, Savings Accounts, Money Transfers)
- 📱 Interactive chat interface with Gradio
- 📋 Evidence-based responses with source document citations
- 🚀 Efficient vector storage using FAISS
- 🧪 Robust RAG pipeline implementation

## 📁 Project Structure

```
intelligent-complaint-analysis/
├── config/              # Configuration files
│   └── config.py       # Project configuration
├── data/               # Raw and processed data
├── docs/               # Documentation
├── notebooks/          # Jupyter notebooks for EDA
├── src/               # Source code
│   ├── core/          # Core RAG implementation
│   ├── embeddings/    # Embedding generation
│   ├── retrieval/     # Vector store and retrieval
│   └── ui/            # Chat interface
├── tests/             # Test files
├── utils/             # Utility modules
├── vector_store/      # Vector database
├── .gitignore         # Git ignore file
├── requirements.txt   # Python dependencies
├── README.md          # Project documentation
└── .github/           # GitHub configuration
```

## 🛠️ Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/Abuabdellahh/intelligent-complaint-analysis-fintech-final.git
   cd intelligent-complaint-analysis-fintech-final
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the preprocessing notebook:
   ```bash
   jupyter notebook notebooks/01_eda_and_preprocessing.ipynb
   ```

5. Initialize the vector store:
   ```bash
   python src/core/create_vector_store.py
   ```

6. Launch the chat interface:
   ```bash
   python src/ui/app.py
   ```

## 🤝 Usage

1. Start the chat interface:
   ```bash
   python src/ui/app.py
   ```

2. Ask natural language questions about customer complaints:
   - "What are common credit card issues?"
   - "Why do people complain about BNPL?"
   - "Compare savings account complaints"

3. Review generated answers and source documents in the interface

## 📚 Development Workflow

### Task 1: EDA and Data Preprocessing
- Analyze complaint data distribution
- Clean and filter relevant product categories
- Save processed data

### Task 2: Text Chunking and Vector Store
- Implement text chunking strategy
- Generate embeddings
- Build vector store

### Task 3: RAG Pipeline
- Implement retrieval logic
- Design prompt templates
- Integrate LLM for response generation

### Task 4: Chat Interface
- Build interactive UI
- Implement source document display
- Add streaming support

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## 📄 License

MIT License

## 👏 Acknowledgments

- Consumer Financial Protection Bureau (CFPB) for the dataset
- LangChain for RAG implementation
- FAISS for vector storage
- HuggingFace for LLM and embedding models