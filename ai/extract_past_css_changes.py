# -*- coding: utf-8 -*-
import json
import os

print("--- Extract Past CSS Changes Start ---")

log_path = "/Users/admin/.gemini/antigravity/brain/60ccec6e-1ef9-4a60-a5d8-4a655b4b9e52/.system_generated/logs/transcript.jsonl"

if not os.path.exists(log_path):
    # fallback
    log_path = "../../brain/60ccec6e-1ef9-4a60-a5d8-4a655b4b9e52/.system_generated/logs/transcript.jsonl"

if os.path.exists(log_path):
    with open(log_path, "r", encoding="utf-8") as f:
        for line in f:
            try:
                data = json.loads(line)
                # replacementContent や CodeContent を含む tool_calls を探す
                if "tool_calls" in data:
                    for tc in data["tool_calls"]:
                        args = tc.get("args", {})
                        # common.css に対する変更を探す
                        if "common.css" in args.get("TargetFile", "") or "common.css" in args.get("Target", ""):
                            print(f"\n[Tool] {tc.get('name')} | Summary: {tc.get('toolSummary')}")
                            if "ReplacementContent" in args:
                                print(f"--- ReplacementContent ---")
                                print(args["ReplacementContent"][:500])
                            elif "CodeContent" in args:
                                print(f"--- CodeContent (Truncated) ---")
                                print(args["CodeContent"][:500])
            except Exception as e:
                pass
else:
    print("Transcript log file not found.")

print("--- Extract Past CSS Changes End ---")
