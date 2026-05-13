import openai
import os
from dotenv import load_dotenv
from browser import StealthBrowser
from memory import AgentMemory
import asyncio
import json

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

class WebAutomationAgent:
    def __init__(self, session_id: str = "shopper"):
        self.memory = AgentMemory(session_id)
        self.browser = StealthBrowser()
        self.state = self.memory.load_state()
    
    async def run_mission(self, goal: str):
        """Execute autonomous web mission"""
        self.state["goal"] = goal
        self.state["status"] = "running"
        self.memory.save_state(self.state)
        
        await self.browser.start()
        
        # Agent loop: Observe → Think → Act
        for step in range(15):  # Max 15 steps
            print(f"\n🧠 Step {step+1}/15")
            
            # 1. OBSERVE
            current_url = self.browser.page.url
            page_title = await self.browser.page.title()
            screenshot = f"step_{step}.png"
            await self.browser.screenshot(screenshot)
            
            # 2. THINK (LLM decides next action)
            action = await self.decide_action(current_url, page_title, goal)
            
            # 3. ACT
            await self.execute_action(action)
            
            if "MISSION_COMPLETE" in action.get("command", ""):
                break
        
        await self.browser.close()
        self.state["status"] = "complete"
        self.memory.save_state(self.state)
    
    async def decide_action(self, url: str, title: str, goal: str) -> Dict:
        """LLM decides what to do next"""
        messages = self.memory.load_state().get("messages", [])
        messages.extend([
            {"role": "system", "content": """
            You are a web automation agent. Control browser with JSON actions.
            Available actions: 
            - {"command": "goto", "url": "https://amazon.com"}
            - {"command": "fill", "selector": "#search", "text": "laptop"}
            - {"command": "click", "selector": "button.buy-now"}
            - {"command": "scroll_down"}
            - {"command": "MISSION_COMPLETE", "reason": "why done"}
            Think step-by-step, be precise with selectors.
            """},
            {"role": "user", "content": f"""
            GOAL: {goal}
            URL: {url}
            TITLE: {title}
            What's my next action? Respond ONLY with valid JSON.
            """}
        ])
        
        response = await openai.ChatCompletion.acreate(
            model="gpt-4",
            messages=messages,
            temperature=0.1
        )
        
        action_str = response.choices[0].message.content.strip()
        try:
            action = json.loads(action_str)
            self.memory.add_message("assistant", json.dumps(action))
            return action
        except:
            return {"command": "MISSION_COMPLETE", "reason": "Parse error"}
    
    async def execute_action(self, action: Dict):
        """Execute browser action"""
        cmd = action.get("command")
        
        if cmd == "goto":
            await self.browser.goto(action["url"])
        elif cmd == "fill":
            await self.browser.fill(action["selector"], action["text"])
        elif cmd == "click":
            await self.browser.click(action["selector"])
        elif cmd == "scroll_down":
            await self.browser.page.evaluate("window.scrollBy(0, 1000)")
        
        print(f"✅ Executed: {cmd}")
