"""Sequential Reasoning Branch & Backtrack Engine.
100% Python Standard Library.
"""

class SequentialReasoningEngine:
    """Tracks multi-step reasoning chains, supports branching hypotheses, and prunes dead ends."""
    
    def __init__(self):
        self.steps = []
        self.branches = {}
        
    def append_thought(self, thought: str, confidence: float, branch_id: str = "main") -> dict:
        step_num = len(self.steps) + 1
        entry = {
            "step": step_num,
            "branch": branch_id,
            "thought": thought,
            "confidence": confidence,
            "status": "ACTIVE" if confidence >= 0.5 else "BACKTRACK_TRIGGERED"
        }
        self.steps.append(entry)
        self.branches.setdefault(branch_id, []).append(entry)
        return entry
        
    def get_summary(self) -> dict:
        active_steps = [s for s in self.steps if s["status"] == "ACTIVE"]
        backtracks = [s for s in self.steps if s["status"] == "BACKTRACK_TRIGGERED"]
        return {
            "total_steps": len(self.steps),
            "active_path_length": len(active_steps),
            "backtracks_count": len(backtracks),
            "final_conclusion": active_steps[-1]["thought"] if active_steps else "No valid path"
        }
