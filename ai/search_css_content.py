# -*- coding: utf-8 -*-
import json
import os

print("--- Search CSS Content in Logs Start ---")

log_path = "/Users/admin/.gemini/antigravity/brain/60ccec6e-1ef9-4a60-a5d8-4a655b4b9e52/.system_generated/logs/transcript_full.jsonl"

# 探したいCSSのキーワード（SDGsやgraytbなど）
keywords = ["graytb", "sdgs", "flex-wrap", "fnav"]

if os.path.exists(log_path):
    with open(log_path, "r", encoding="utf-8") as f:
        for idx, line in enumerate(f):
            # 行の中にキーワードが複数含まれるか確認する
            # 特に MODEL の応答で、かつコードブロックらしき部分
            if any(kw in line for kw in keywords) and "MODEL" in line and "run_command" in line:
                try:
                    data = json.loads(line)
                    for tc in data.get("tool_calls", []):
                        args = tc.get("args", {})
                        cmd = args.get("CommandLine", "")
                        if "common.css" in cmd or "rebuild" in cmd or "add" in cmd or "update" in cmd:
                            print(f"\n[Step {data.get('step_index')}] cmd: {cmd[:300]}")
                            # 300文字以降もキーワードが含まれる付近を出力
                            for kw in keywords:
                                if kw in cmd:
                                    kw_idx = cmd.find(kw)
                                    print(f"  Context for '{kw}': ... {cmd[max(0, kw_idx-150):kw_idx+300]} ...")
                except Exception as e:
                    pass
else:
    print("Log not found.")

print("--- Search CSS Content in Logs End ---")
