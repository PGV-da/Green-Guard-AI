from langchain_chroma import Chroma
from langchain_ollama import ChatOllama, OllamaEmbeddings
from langchain_groq import ChatGroq
# from langchain_openai import AzureOpenAIEmbeddings, AzureChatOpenAI

class Models:
    def __init__(self):
        # ollama pull mxbai-embed-large
        self.embedding_ollama = OllamaEmbeddings(
            model="tazarov/all-minilm-l6-v2-f32",
        )

        # ollama pull llama3.2
        self.model_ollama = ChatOllama(
            model="llama3.1",
            temperature=0,
        )

        # API key for Groq
        # self.model_ollama = ChatGroq(api_key="GROQ_API_KEY",
        # model_name="llama-3.1-8b-instant"
        # )

        # Initialize vector store once and reuse
        self.vector_store = Chroma(
            collection_name="documents",
            embedding_function=self.embedding_ollama,
            persist_directory="./db/chroma_langchain_db",
        )

        # # Azure OpenAI embedding
        # self.embedding_openai = AzureOpenAIEmbeddings(
        #     model="text-embedding-3-large",
        #     dimensions=1536,
        #     azure_endpoint="",
        #     api_key="",
        #     api_version="",
        # )

        # # Azure OpenAI chat model
        # self.model_openai = AzureChatOpenAI(
        #     azure_deployment="" , # Azure deployment name
        #     api_version="",
        #     temperature=0,
        #     max_tokens=None,
        #     timeout=None,
        #     max_retries=2,
        # )