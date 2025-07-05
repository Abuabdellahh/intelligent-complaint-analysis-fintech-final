import gradio as gr
from src.core.rag_pipeline import RAGPipeline

class ComplaintAnalysisBot:
    def __init__(self):
        """
        Initialize financial complaint analysis bot
        """
        self.rag_pipeline = RAGPipeline()
        self.initialize_pipeline()

    def initialize_pipeline(self):
        """
        Initialize optimized RAG pipeline
        """
        try:
            self.rag_pipeline.create_vector_store("../data/filtered_complaints.csv")
            self.rag_pipeline.initialize_llm()
        except Exception as e:
            print(f"Pipeline initialization error: {str(e)}")

    def get_response(self, question: str) -> dict:
        """
        Get optimized response with sources
        
        Args:
            question: User query
            
        Returns:
            Response dictionary
        """
        try:
            response = self.rag_pipeline.query(question)
            return {
                "answer": response['answer'],
                "sources": [f"Product: {doc['metadata']['product']}\n{doc['text']}" 
                           for doc in response['sources']]
            }
        except Exception as e:
            return {
                "answer": f"Error processing query: {str(e)}",
                "sources": []
            }

def chat_interface(question: str):
    """
    Process user query through chat interface
    """
    bot = ComplaintAnalysisBot()
    response = bot.get_response(question)
    return response['answer'], "\n\n".join(response['sources'])

# Create optimized Gradio interface
demo = gr.Interface(
    fn=chat_interface,
    inputs=gr.Textbox(
        label="Ask about financial complaints",
        placeholder="e.g., 'What are common credit card issues?'"
    ),
    outputs=[
        gr.Textbox(label="Analysis"),
        gr.Textbox(label="Source Complaints")
    ],
    title="Financial Complaint Analysis",
    description="Analyze customer complaints across financial products.",
    examples=[
        "What are common credit card issues?",
        "Why do people complain about BNPL?",
        "Compare savings account complaints"
    ]
)

if __name__ == "__main__":
    demo.launch(share=True)
