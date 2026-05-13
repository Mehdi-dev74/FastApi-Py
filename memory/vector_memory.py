"""
Vector database for agent long-term memory
"""
from chromadb import Client
from chromadb.utils import embedding_functions

class AgentMemory:
    def __init__(self, persist_path: str):
        self.client = Client(persist_directory=persist_path)
        self.collection = self.client.get_or_create_collection(
            name="agent_memory",
            embedding_function=embedding_functions.OpenAIEmbeddingFunction(
                api_key="your-openai-key"
            )
        )
    
    def save_conversation(self, role: str, content: str, metadata: dict):
        """Save conversation to vector DB"""
        self.collection.add(
            documents=[content],
            metadatas=[metadata],
            ids=[f"{role}_{len(self.collection.get())}"]
        )
    
    def retrieve_relevant(self, query: str, n_results: int = 3) -> list:
        """Retrieve relevant past conversations"""
        results = self.collection.query(
            query_texts=[query],
            n_results=n_results
        )
        return results['documents'][0] if results['documents'] else []
