# todo_backend.py

import json
from datetime import datetime

TASK_FILE = "tasks.json"

def load_tasks():
    try:
        with open(TASK_FILE, "r") as f:
            return json.load(f)
    except:
        return []

def save_tasks(tasks):
    with open(TASK_FILE, "w") as f:
        json.dump(tasks, f, indent=2)

def add_task(text, due_date, tasks):
    if text.strip():
        tasks.append({
            "text": text.strip(),
            "done": False,
            "due": due_date
        })
        save_tasks(tasks)

def delete_task(index, tasks):
    if 0 <= index < len(tasks):
        tasks.pop(index)
        save_tasks(tasks)

def toggle_status(index, tasks):
    if 0 <= index < len(tasks):
        tasks[index]["done"] = not tasks[index]["done"]
        save_tasks(tasks)
