import json

data = [
    {"id": 0, "name": "all", "pid": -1},
    {"id": 1, "name": "1", "pid": 0},
    {"id": 11, "name": "1-1", "pid": 1},
    {"id": 111, "name": "1-1-1", "pid": 11},
    {"id": 112, "name": "1-1-2", "pid": 11},
    {"id": 12, "name": "1-2", "pid": 1},
    {"id": 2, "name": "2", "pid": 0},
    {"id": 21, "name": "2-1", "pid": 2},
    {"id": 22, "name": "2-2", "pid": 2},
    {"id": 221, "name": "2-2-1", "pid": 22},
    {"id": 222, "name": "2-2-2", "pid": 22},
    {"id": 23, "name": "2-3", "pid": 2},
]


def insert(root):
    childs = [item for item in data if item["pid"] == root["id"]]
    if len(childs) == 0:
        return root
    root["childs"] = []
    for item in childs:
        root["childs"].append(insert(item))
    return root


root = [item for item in data if item["pid"] == -1][0]
root = insert(root)
print(json.dumps(root, sort_keys=False, indent=2))
