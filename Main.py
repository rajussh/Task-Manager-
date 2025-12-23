tasks = []

def add_task(task_name):
    tasks.append({"task": task_name, "completed": False})
    print(f"Added: {task_name}")

def show_tasks():
    print("\n--- Current Task List ---")
    for index, t in enumerate(tasks):
        status = "✅" if t["completed"] else "❌"
        print(f"{index + 1}. {t['task']} [{status}]")

# Sample execution
add_task("GitHub Repository Setup")
add_task("Code Documentation")
show_tasks()
