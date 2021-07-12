import json

dict = {"japanese": "日本語", "english": "英語"}
text = json.dumps(dict, sort_keys=True, ensure_ascii=False, indent=2)
with open("test.json", "w") as fh:
    fh.write()
