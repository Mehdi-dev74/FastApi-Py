import redis
import json
from typing import Dict, List
import os
from dotenv import load_dotenv

load_dotenv()
r = redis.from_url(os.getenv("REDIS_URL", "redis://localhost:6379"))

class AgentMemory:
    def __init__(self, session_id: str = "default"):
        self.session_id = session_id
    
    def save_state(self, state: Dict):
        r.set(f"agent:{self.session_id}:state", json.dumps(state))
    
    def load_state(self) -> Dict:
        state = r.get(f"agent:{self.session_id}:state")
        return json.loads(state) if state else {}
    
    def add_message(self, role: str, content: str):
        messages = self.load_state().get("messages", [])
        messages.append({"role": role, "content": content})
        self.save_state({"messages": messages[-10:]})  # Keep last 10
