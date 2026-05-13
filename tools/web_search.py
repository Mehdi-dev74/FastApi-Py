"""
Real web search tool for agents
"""
import requests
import json
from typing import List, Dict

class WebSearchTool:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://google.serper.dev/search"
    
    def search(self, query: str, num_results: int = 5) -> str:
        """Perform Google search and return formatted results"""
        headers = {"X-API-KEY": self.api_key, "Content-Type": "application/json"}
        data = {"q": query, "num": num_results}
        
        try:
            response = requests.post(self.base_url, headers=headers, json=data)
            results = response.json()
            
            formatted_results = []
            for result in results.get("organic", [])[:3]:
                formatted_results.append({
                    "title": result.get("title"),
                    "link": result.get("link"),
                    "snippet": result.get("snippet")
                })
            
            return json.dumps(formatted_results, indent=2)
        except Exception as e:
            return f"Search failed: {str(e)}"

# Global instance
search_tool = WebSearchTool("your-serper-key-here")  # Get free key at serper.dev
