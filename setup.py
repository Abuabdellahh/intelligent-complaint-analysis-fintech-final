from setuptools import setup, find_packages

setup(
    name="intelligent-complaint-analysis",
    version="1.0.0",
    description="RAG-powered chatbot for analyzing financial complaints",
    author="Abuabdellahh",
    author_email="",
    url="https://github.com/Abuabdellahh/intelligent-complaint-analysis-fintech-final",
    packages=find_packages(),
    install_requires=[
        "pandas>=2.0.0",
        "numpy>=1.24.0",
        "sentence-transformers>=2.2.2",
        "faiss-cpu>=1.7.4",
        "langchain>=0.1.0",
        "transformers>=4.36.0",
        "torch>=2.0.0",
        "gradio>=4.30.0",
        "python-dotenv>=1.0.0",
        "pytest>=7.4.0",
        "pytest-cov>=4.1.0",
        "black>=23.7.0",
        "isort>=5.12.0",
        "flake8>=6.1.0",
        "mypy>=1.6.1",
        "jupyter>=1.0.0",
        "notebook>=7.0.0"
    ],
    extras_require={
        "dev": [
            "black>=23.7.0",
            "isort>=5.12.0",
            "flake8>=6.1.0",
            "mypy>=1.6.1",
            "pytest>=7.4.0",
            "pytest-cov>=4.1.0"
        ]
    },
    python_requires=">=3.8",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Financial and Insurance Industry",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    entry_points={
        "console_scripts": [
            "complaint-analysis=src.ui.app:main"
        ]
    }
)
