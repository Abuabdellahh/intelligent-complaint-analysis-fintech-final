# Intelligent Complaint Analysis for Financial Services

An AI-powered system that transforms raw customer complaint data into actionable insights using RAG technology.

## 🚀 Features

- 🤖 Semantic search over customer complaints
- 📊 Multi-product analysis (Credit Cards, Personal Loans, BNPL, Savings Accounts, Money Transfers)
- 📱 Interactive Gradio interface
- 📋 Evidence-based insights with source citations
- 🚀 Efficient FAISS vector storage
- 🧪 Robust RAG implementation

## 📁 Structure

```
intelligent-complaint-analysis/
├── data/               # Dataset
├── notebooks/          # EDA notebook
├── src/               # Source code
│   ├── config.py      # Project settings
│   ├── core/          # RAG implementation
│   └── ui/            # Chat interface
├── vector_store/      # FAISS index
├── requirements.txt   # Dependencies
└── README.md          # Documentation
```

## 🛠️ Setup

1. Clone and install:
   ```bash
   git clone https://github.com/Abuabdellahh/intelligent-complaint-analysis-fintech-final.git
   cd intelligent-complaint-analysis-fintech-final
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. Run preprocessing:
   ```bash
   jupyter notebook notebooks/01_eda_and_preprocessing.ipynb
   ```

3. Initialize vector store:
   ```bash
   python src/core/create_vector_store.py
   ```

4. Launch chatbot:
   ```bash
   python src/ui/app.py
   ```

## 🤝 Usage

Ask questions about customer complaints:
- "What are common credit card issues?"
- "Why do people complain about BNPL?"
- "Compare savings account complaints"

## 📄 License

MIT License

## 👏 Acknowledgments

- Consumer Financial Protection Bureau (CFPB)
- LangChain
- FAISS
- HuggingFace