# CatanMaster 🎲

An AI-powered assistant built with open-source models to help players learn and master the board game Catan. CatanMaster uses Retrieval-Augmented Generation (RAG) to provide accurate, context-aware answers about Catan rules, strategies, and gameplay.

## 🎯 Purpose

CatanMaster is designed to be your personal Catan expert, answering questions and guiding you through the complexities of the game. Whether you're a beginner learning the basics or an experienced player looking for strategic advice, CatanMaster has you covered.

## ✨ Features

- **RAG-Powered Responses**: Uses vector embeddings and semantic search to find relevant information from the Catan rulebook
- **Local LLM**: Runs completely locally using Ollama (llama3.2 model)
- **Interactive CLI**: Simple command-line interface for asking questions
- **Persistent Vector Database**: ChromaDB stores document embeddings for fast retrieval
- **Source Citations**: Provides references to specific pages and sections from the rulebook

## 🛠️ Tech Stack

- **LangChain**: Framework for building LLM applications
- **Ollama**: Local LLM runtime (llama3.2 for generation, mxbai-embed-large for embeddings)
- **ChromaDB**: Vector database for semantic search
- **PyPDF**: PDF parsing and text extraction
- **Python 3.12+**: Core programming language

## 📋 Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.12 or higher
- [Ollama](https://ollama.ai/) installed and running
- Git (for cloning the repository)

## 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Kxtnny/CatanMaster.git
   cd CatanMaster
   ```

2. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Install Ollama models**
   ```bash
   ollama pull llama3.2
   ollama pull mxbai-embed-large
   ```

4. **Add your Catan rulebook**
   - Place your Catan rulebook PDF in the `data/` folder
   - The current setup includes `catan.pdf` as an example

## 📖 Usage

### Initial Setup: Populate the Database

Before querying, you need to process the PDF and create the vector database:

```bash
python populate_db.py
```

This will:
- Load all PDFs from the `data/` folder
- Split documents into chunks
- Generate embeddings
- Store them in the ChromaDB database

**Optional**: Reset the database if you want to start fresh:
```bash
python populate_db.py --reset
```

### Query the AI Assistant

Run the interactive CLI:

```bash
python app.py
```

Then ask questions about Catan:
```
Enter your question (q to quit): How do I get victory points in Catan?
Enter your question (q to quit): What happens when I roll a 7?
Enter your question (q to quit): Can I trade with other players?
```

Type `q` to quit the application.

## 📁 Project Structure

```
CatanMaster/
├── app.py                      # Main entry point for the CLI
├── query_data.py              # Query logic and RAG implementation
├── populate_db.py             # PDF processing and database population
├── get_embedding_function.py  # Embedding model configuration
├── requirements.txt           # Python dependencies
├── data/                      # PDF files (Catan rulebook)
│   └── catan.pdf
├── chroma/                    # ChromaDB vector database (generated)
└── README.md                  # This file
```

## 🔧 Configuration

### Change the LLM Model

Edit `query_data.py` and modify the model name:
```python
model = OllamaLLM(model="llama3.2")  # Change to any Ollama model
```

### Change the Embedding Model

Edit `get_embedding_function.py`:
```python
embeddings = OllamaEmbeddings(model="mxbai-embed-large")  # Change model name
```

### Adjust Chunk Size

Edit `populate_db.py` to modify text splitting:
```python
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=800,      # Increase for larger chunks
    chunk_overlap=80,    # Adjust overlap
)
```

## 🐛 Troubleshooting

### PDF Loading Issues

If you encounter errors loading PDFs:
- Ensure `pypdf` is installed: `pip install pypdf`
- If the PDF is encrypted, install cryptography: `pip install cryptography>=3.1`

### Ollama Connection Issues

- Verify Ollama is running: `ollama serve`
- Check if models are downloaded: `ollama list`
- Ensure the correct model names are specified in the code

### Empty Responses

- Make sure you've run `populate_db.py` before querying
- Verify the `chroma/` directory exists and contains data
- Check that your PDF is readable and contains text

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Add support for more board games
- Improve the prompt templates
- Enhance the CLI interface
- Add a web interface


## 🙏 Acknowledgments

- Built with [LangChain](https://www.langchain.com/)
- Powered by [Ollama](https://ollama.ai/)
- Vector storage by [ChromaDB](https://www.trychroma.com/)

---

**Note**: This project is for educational purposes. Make sure you have the right to use any PDF files you include in the `data/` folder.
