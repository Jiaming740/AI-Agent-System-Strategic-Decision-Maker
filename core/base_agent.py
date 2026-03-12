from abc import ABC, abstractmethod
from typing import Dict, Any
import asyncio


class BaseStrategicAgent(ABC):
    """
    Standardized interface base class for AI Agents.
    Ensures that all heterogeneous agents follow a unified input/output protocol
    and context management specification.
    """

    def __init__(self, agent_id: str, role_description: str):
        self.agent_id = agent_id
        self.role_description = role_description
        self.context_memory = []  # Simulating short-term memory

    @abstractmethod
    async def execute_task(self, task_input: Dict[str, Any]) -> Dict[str, Any]:
        """
        Core logic encapsulation: The asynchronous task execution flow
        that each agent must implement.
        """
        pass

    def update_context(self, new_info: Dict[str, Any]):
        """
        Model Context Protocol (MCP) adaptation: Dynamically updates the agent's context.
        """
        self.context_memory.append(new_info)

    async def _mock_llm_call(self, prompt: str, delay: float = 1.0) -> str:
        """
        Simulates the underlying LLM call.
        (In actual deployment, replace this with Google GenAI / LangChain interfaces)
        """
        await asyncio.sleep(delay)
        return f"[{self.agent_id}] Processed: {prompt[:20]}..."