from langchain_ollama import OllamaEmbeddings


def get_embedding_function():
    #initialize the Ollama Embeddings model
    embeddings = OllamaEmbeddings(model="mxbai-embed-large")
    return embeddings