import os
import time
from uuid import uuid4

from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from utils.chatbot.models import Models

# Load the models
models = Models()
embeddings = models.embedding_ollama
llm = models.model_ollama
vector_store = models.vector_store

# Define constants
data_folder = "./data"
chunk_size = 1000
chunk_overlap = 50
check_interval = 10

# Ingest a file
def ingest_file(file_path):
    try:
        if file_path.lower().endswith(".pdf"):
            loader = PyPDFLoader(file_path)
        elif file_path.lower().endswith(".txt"):
            loader = TextLoader(file_path)
        else:
            print(f"Skipping unsupported file type: {file_path}")
            return

        print(f"Ingesting {file_path}")
        documents = loader.load()
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size, chunk_overlap=chunk_overlap
        )
        docs = text_splitter.split_documents(documents)
        vector_store.add_documents(docs, uuids=[str(uuid4()) for _ in docs])
        print(f"Finished ingesting: {file_path}")
    except Exception as e:
        print(f"Error processing {file_path}: {e}")

# Main loop
def main_loop():
     while True:
        for filename in os.listdir(data_folder):
            if not filename.startswith("_"):
                file_path = os.path.join(data_folder, filename)
                ingest_file(file_path)
                os.rename(file_path, os.path.join(data_folder, "_" + filename))
        time.sleep(check_interval)

# Run the main loop
if __name__ == "__main__":
    main_loop()