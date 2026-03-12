class MemoryManager:
    """Manages global knowledge base and simulates RAG vector retrieval."""
    def __init__(self):
        self.global_knowledge_base = {}

    def store(self, key: str, value: any):
        self.global_knowledge_base[key] = value

    def retrieve(self, query: str):
        return self.global_knowledge_base.get(query, "No historical data found.")