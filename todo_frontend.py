# todo_frontend.py

import tkinter as tk
from tkinter import messagebox
from tkcalendar import DateEntry
from datetime import datetime
import todo_backend as backend

tasks = backend.load_tasks()

def refresh_list():
    listbox.delete(0, "end")
    today = datetime.now().date()
    for task in tasks:
        check = "✅" if task["done"] else "🔲"
        due_str = f"(Due: {task['due']})" if task["due"] else ""
        due_date = datetime.strptime(task["due"], "%Y-%m-%d").date() if task["due"] else None

        if due_date and due_date < today and not task["done"]:
            due_str += " 🔔 Overdue!"
        elif due_date == today and not task["done"]:
            due_str += " ⏰ Due Today!"

        listbox.insert("end", f"{check} {task['text']} {due_str}")

def handle_add():
    task = entry.get()
    due = due_picker.get_date().strftime("%Y-%m-%d")
    if task:
        backend.add_task(task, due, tasks)
        entry.delete(0, "end")
        refresh_list()
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

def handle_delete():
    selected = listbox.curselection()
    if selected:
        backend.delete_task(selected[0], tasks)
        refresh_list()

def handle_toggle():
    selected = listbox.curselection()
    if selected:
        backend.toggle_status(selected[0], tasks)
        refresh_list()

# UI Setup
root = tk.Tk()
root.title("🗓️ To-Do List with Deadlines")
root.geometry("480x600")
root.config(bg="white")

# Fonts
FONT_MAIN = ("Segoe UI", 13)
FONT_TITLE = ("Segoe UI", 20, "bold")

# Header
tk.Label(root, text="📝 Task Planner", font=FONT_TITLE, bg="white", fg="#202124").pack(pady=20)

# Entry
entry = tk.Entry(root, font=FONT_MAIN, width=30, bg="#F1F3F4", relief="flat")
entry.pack(pady=5)

# Due Date Picker
due_picker = DateEntry(root, width=18, background="#4285F4", foreground="white", borderwidth=0, font=FONT_MAIN)
due_picker.pack(pady=5)

# Buttons
btn_frame = tk.Frame(root, bg="white")
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Add Task", font=FONT_MAIN, bg="#34A853", fg="white", command=handle_add).grid(row=0, column=0, padx=10)
tk.Button(btn_frame, text="Delete", font=FONT_MAIN, bg="#EA4335", fg="white", command=handle_delete).grid(row=0, column=1, padx=10)
tk.Button(btn_frame, text="✓ Toggle", font=FONT_MAIN, bg="#4285F4", fg="white", command=handle_toggle).grid(row=0, column=2, padx=10)

# Listbox
listbox = tk.Listbox(root, font=FONT_MAIN, width=50, height=15, selectbackground="#D2E3FC")
listbox.pack(pady=20)

refresh_list()

tk.Label(root, text="Made by Kunal ✨", font=("Segoe UI", 9), fg="#5f6368", bg="white").pack(pady=10)

root.mainloop()
