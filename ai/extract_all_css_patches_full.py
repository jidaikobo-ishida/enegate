# -*- coding: utf-8 -*-
import json
import os

print("--- Extract All CSS Patches (Full Log) Start ---")

log_path = "/Users/admin/.gemini/antigravity/brain/60ccec6e-1ef9-4a60-a5d8-4a655b4b9e52/.system_generated/logs/transcript_full.jsonl"

if os.path.exists(log_path):
    with open(log_path, "r", encoding="utf-8") as f:
        for idx, line in enumerate(f):
            try:
                data = json.loads(line)
                if data.get("source") == "MODEL" and "tool_calls" in data:
                    for tc in data["tool_calls"]:
                        name = tc.get("name")
                        args = tc.get("args", {})
                        
                        # common.css を含む引数があるか確認
                        args_str = json.dumps(args)
                        if "common.css" in args_str:
                            print(f"\n[Step {data.get('step_index')}] Tool: {name}")
                            desc = args.get("Description", "") or args.get("Instruction", "")
                            print(f"Description: {desc}")
                            
                            if "ReplacementContent" in args:
                                print("--- ReplacementContent ---")
                                print(args["ReplacementContent"][:800])
                            elif "ReplacementChunks" in args:
                                print("--- ReplacementChunks ---")
                                for chunk in args["ReplacementChunks"]:
                                    print(f"Target: {chunk.get('TargetContent')}")
                                    print(f"Replacement: {chunk.get('ReplacementContent')[:400]}")
                                    print("-" * 20)
                            elif "CodeContent" in args:
                                print("--- CodeContent ---")
                                print(args["CodeContent"][:800])
            except Exception as e:
                pass
else:
    print("Transcript log file not found.")

print("--- Extract All CSS Patches (Full Log) End ---")
