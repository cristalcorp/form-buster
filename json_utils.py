import json

def read_json(json_file):
    with open(json_file, "r", encoding="utf-8") as f:
        data = json.load(f)
        flat = flatten_json(data)

        print("""
JSON content :
--------------\n
          """)

        for key, value in flat:
            print(f"{key}: {value}")

def flatten_json(data, parent_key=""):
    result = []

    if isinstance(data, dict):
        for key, value in data.items():
            new_key = f"{parent_key}.{key}" if parent_key else key
            result.extend(flatten_json(value, new_key))

    elif isinstance(data, list):
        for i, item in enumerate(data):
            new_key = f"{parent_key}[{i}]"
            result.extend(flatten_json(item, new_key))

    else:
        result.append((parent_key, data))

    return result
