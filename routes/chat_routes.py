
import concurrent.futures

from flask import Blueprint, jsonify, render_template, request
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.retrieval import create_retrieval_chain
from langchain_core.prompts import ChatPromptTemplate

from utils.authentication import require_login
from utils.chatbot.models import Models

chat_bp = Blueprint('chat', __name__)

# Initilize the models
models = Models()
vector_store = models.vector_store
retriever = vector_store.as_retriever(kwargs={"k": 3})

prompt = ChatPromptTemplate([
    ("system", "You are Bloom, an assistant designed to help with agriculture-based problems. Answer based on provided documents, ensuring responses are between 10 and 30 words."),
    ("user", "Use the user question {input} to answer. Use only {context}.")
])

combine_docs_chain = create_stuff_documents_chain(models.model_ollama, prompt)
retrieval_chain = create_retrieval_chain(retriever, combine_docs_chain)

# Function to process the query asynchronously
def process_query(query):
    try:
        result = retrieval_chain.invoke({"input": query})
        answer = result.get("answer", "I couldn't find an answer.")
        
        # Ensure the answer meets word constraints
        words = answer.split()
        if len(words) < 10:
            answer += " " + " ".join(["..." for _ in range(10 - len(words))])
        elif len(words) > 30:
            answer = " ".join(words[:30]) + "..."
        
        return answer
    except Exception as e:
        return f"Error processing query: {e}"

@chat_bp.route('/chat', methods=['POST'])
@require_login
def chat():
    """Handles chatbot interactions."""
    with concurrent.futures.ThreadPoolExecutor() as executor:
        user_input = request.json.get('message')
        future = executor.submit(process_query, user_input)
        answer = future.result()
        return jsonify({'message': answer})

@chat_bp.route('/chatassistant')
@require_login
def chatassistant():
    """Renders the chat assistant page."""
    return render_template('chat-assistant.html')