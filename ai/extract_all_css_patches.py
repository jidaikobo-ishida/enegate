# -*- coding: utf-8 -*-
import json
import os

print("--- Extract All CSS Patches Start ---")

log_path = "/Users/admin/.gemini/antigravity/brain/60ccec6e-1ef9-4a60-a5d8-4a655b4b9e52/.system_generated/logs/transcript.jsonl"

if os.path.exists(log_path):
    with open(log_path, "r", encoding="utf-8") as f:
        for idx, line in enumerate(f):
            try:
                data = json.loads(line)
                # MODEL の planner_response のみ
                if data.get("source") == "MODEL" and "tool_calls" in data:
                    for tc in data["tool_calls"]:
                        name = tc.get("name")
                        args = tc.get("args", {})
                        
                        # TargetFile または Target に common.css が含まれているか確認
                        target_file = args.get("TargetFile", "") or args.get("Target", "")
                        if "common.css" in target_file:
                            print(f"\n[Step {data.get('step_index')}] Tool: {name}")
                            # Description
                            desc = args.get("Description", "") or args.get("Instruction", "")
                            print(f"Description: {desc}")
                            
                            # ReplacementContent または ReplacementChunks を表示
                            if "ReplacementContent" in args:
                                print("--- ReplacementContent ---")
                                print(args["ReplacementContent"])
                            elif "ReplacementChunks" in args:
                                print("--- ReplacementChunks ---")
                                for chunk in args["ReplacementChunks"]:
                                    print(f"Target: {chunk.get('TargetContent')}")
                                    print(f"Replacement: {chunk.get('ReplacementContent')}")
                                    print("-" * 20)
                            elif "CodeContent" in args:
                                print("--- CodeContent ---")
                                print(args["CodeContent"][:1000])
            except Exception as e:
                # デバッグ用にエラーを表示
                # print(f"Error on line {idx}: {e}")
                pass
else:
    print("Transcript log file not found.")

print("--- Extract All CSS Patches End ---")
