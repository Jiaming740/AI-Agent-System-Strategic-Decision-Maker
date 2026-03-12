from core.base_agent import BaseStrategicAgent
from core.protocols import ConsistencyProtocol, SemanticAligner


class DecisionController(BaseStrategicAgent):
    """5. Decision Controller Agent: Responsible for global orchestration and protocol verification."""

    async def execute_task(self, task_input):
        proposals = task_input.get("proposals", [])
        constraints = task_input.get("constraints", {})

        print(f"[{self.agent_id}] Initiating Semantic Alignment...")
        aligned_proposals = [SemanticAligner.align_terminology(p) for p in proposals]

        print(f"[{self.agent_id}] Running Task Consistency Protocol Check...")
        is_consistent, message = ConsistencyProtocol.verify_alignment(aligned_proposals, constraints)

        if not is_consistent:
            print(f"[{self.agent_id}] [WARNING] Conflict Detected: {message}")
            return {"status": "failed", "reason": message, "action": "request_revision"}

        print(f"[{self.agent_id}] Protocols aligned. Synthesizing final strategy...")
        await self._mock_llm_call("Drafting final strategic report")
        return {"status": "success", "final_strategy": "Approved Strategic Blueprint V1.0"}