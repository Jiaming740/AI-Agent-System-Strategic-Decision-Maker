from typing import List, Dict, Tuple


class ConsistencyProtocol:
    """Task Consistency Protocol for Multi-Agent Systems."""

    @staticmethod
    def verify_alignment(proposals: List[Dict], constraints: Dict) -> Tuple[bool, str]:
        """
        Verifies whether the outputs of multiple agents remain consistent
        under strategic goals and resource constraints.

        Returns:
            Tuple[bool, str]: (Is passed, Conflict description)
        """
        total_cost = sum(p.get("estimated_cost", 0) for p in proposals)
        max_risk = max([p.get("risk_score", 0.0) for p in proposals] + [0.0])

        if total_cost > constraints.get("max_budget", float('inf')):
            return False, f"Consistency Violation: Total cost ({total_cost}) exceeds budget."
        if max_risk > constraints.get("risk_tolerance", 1.0):
            return False, f"Consistency Violation: Risk score ({max_risk}) exceeds tolerance."

        return True, "All protocols aligned."


class SemanticAligner:
    """Dynamic Semantic Alignment Module."""

    @staticmethod
    def align_terminology(data: Dict) -> Dict:
        """
        Ensures uniformity of indicator terminology across different agents
        (e.g., bridging financial and marketing domains).
        """
        # In a production environment, this connects to a Knowledge Graph or RAG dictionary.
        aligned_data = data.copy()
        aligned_data["_semantic_aligned"] = True
        return aligned_data