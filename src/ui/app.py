import gradio as gr
from src.core.rag_pipeline import RAGPipeline

class ComplaintAnalysisBot:
    def __init__(self):
        """
        Initialize financial complaint analysis bot with enhanced UI features
        """
        self.rag_pipeline = RAGPipeline()
        self.initialize_pipeline()

    def initialize_pipeline(self):
        """
        Initialize optimized RAG pipeline with improved error handling
        """
        try:
            self.rag_pipeline.create_vector_store("../data/filtered_complaints.csv")
            self.rag_pipeline.initialize_llm()
        except Exception as e:
            print(f"Pipeline initialization error: {str(e)}")
            raise

    def get_response(self, question: str) -> dict:
        """
        Get optimized response with enhanced source formatting
        
        Args:
            question: User query
            
        Returns:
            Response dictionary with formatted sources
        """
        try:
            response = self.rag_pipeline.query(question)
            return {
                "answer": response['answer'],
                "sources": [f"Product: {doc['metadata']['product']}\n"
                           f"Complaint ID: {doc['metadata']['complaint_id']}\n"
                           f"{doc['text']}\n{'-'*80}" 
                           for doc in response['sources']]
            }
        except Exception as e:
            error_msg = f"Error processing query: {str(e)}"
            return {
                "answer": error_msg,
                "sources": [error_msg]
            }

def chat_interface(question: str):
    """
    Process user query through enhanced chat interface
    """
    try:
        bot = ComplaintAnalysisBot()
        response = bot.get_response(question)
        return response['answer'], "\n\n".join(response['sources'])
    except Exception as e:
        return f"Error: {str(e)}", ""

# Create enhanced Gradio interface with improved styling
demo = gr.Interface(
    fn=chat_interface,
    inputs=gr.Textbox(
        label="Ask about financial complaints",
        placeholder="e.g., 'What are common credit card issues?'",
        lines=2,
        container=True
    ),
    outputs=[
        gr.Textbox(
            label="Analysis",
            lines=5,
            container=True
        ),
        gr.Textbox(
            label="Source Complaints",
            lines=10,
            container=True
        )
    ],
    title="Financial Complaint Analysis",
    description="""
    Analyze customer complaints across financial products.
    This tool helps you understand common issues and patterns in customer feedback.
    """,
    examples=[
        "What are common credit card issues?",
        "Why do people complain about BNPL?",
        "Compare savings account complaints",
        "What are the most frequent complaints about money transfers?",
        "Analyze patterns in personal loan complaints"
    ],
    css="""
    .gr-box {
        background-color: #f8f9fa;
    }
    .gr-input-container textarea {
        font-size: 16px;
        padding: 12px;
    }
    .gr-output-container {
        margin: 15px 0;
        padding: 15px;
        background: white;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    """
)

if __name__ == "__main__":
    demo.launch(share=True, show_error=True)
