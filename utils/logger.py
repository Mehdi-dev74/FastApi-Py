"""
Professional logging for production agents
"""
import logging
from datetime import datetime

class AgentLogger:
    def __init__(self, agent_name: str):
        self.agent_name = agent_name
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        self.logger = logging.getLogger(agent_name)
    
    def info(self, message: str):
        self.logger.info(f"🤖 {self.agent_name}: {message}")
    
    def success(self, message: str):
        self.logger.info(f"✅ {self.agent_name}: {message}")
    
    def error(self, message: str):
        self.logger.error(f"❌ {self.agent_name}: {message}")

# Global loggers
loggers = {}
def get_logger(agent_name: str):
    if agent_name not in loggers:
        loggers[agent_name] = AgentLogger(agent_name)
    return loggers[agent_name]
