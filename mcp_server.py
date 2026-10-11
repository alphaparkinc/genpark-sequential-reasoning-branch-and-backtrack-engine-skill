"""MCP server for Sequential Reasoning Engine."""
import sys
import json
from client import SequentialReasoningEngine

_engine = SequentialReasoningEngine()

def handle_request(req):
    method = req.get("method")
    if method == "tools/list":
        return {
            "tools": [
                {
                    "name": "record_reasoning_step",
                    "description": "Appends a reasoning step with confidence score and automatic backtrack detection",
                    "inputSchema": {
                        "type": "object",
                        "properties": {
                            "thought": {"type": "string"},
                            "confidence": {"type": "number"},
                            "branch_id": {"type": "string"}
                        },
                        "required": ["thought", "confidence"]
                    }
                },
                {
                    "name": "summarize_reasoning_chain",
                    "description": "Returns active path length, backtracks, and final conclusion",
                    "inputSchema": {"type": "object", "properties": {}}
                }
            ]
        }
    elif method == "tools/call":
        params = req.get("params", {})
        tname = params.get("name")
        args = params.get("arguments", {})
        if tname == "record_reasoning_step":
            res = _engine.append_thought(args.get("thought", ""), args.get("confidence", 1.0), args.get("branch_id", "main"))
            return {"content": [{"type": "text", "text": json.dumps(res, indent=2)}]}
        elif tname == "summarize_reasoning_chain":
            res = _engine.get_summary()
            return {"content": [{"type": "text", "text": json.dumps(res, indent=2)}]}
    return {"error": "Method not found"}

if __name__ == "__main__":
    for line in sys.stdin:
        if line.strip():
            print(json.dumps(handle_request(json.loads(line))))
            sys.stdout.flush()
