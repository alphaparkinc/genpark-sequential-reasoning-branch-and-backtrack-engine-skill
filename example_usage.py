"""Example usage for Sequential Reasoning Engine."""
from client import SequentialReasoningEngine

if __name__ == "__main__":
    engine = SequentialReasoningEngine()
    engine.append_thought("Check if database lock is causing latency", 0.75)
    engine.append_thought("Lock table is empty; hypothesis falsified", 0.20)
    engine.append_thought("Inspect missing index on foreign key column", 0.95)
    summary = engine.get_summary()
    print("Final Conclusion:", summary["final_conclusion"])
    print("Backtracks Triggered:", summary["backtracks_count"])
