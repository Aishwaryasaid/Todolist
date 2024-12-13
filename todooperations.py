# to-do-operations.py
class TodoOperations:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
        return "Task added successfully"

    def view_tasks(self):
        if not self.tasks:
            return "No tasks available"
        
        task_list = []
        for index, task in enumerate(self.tasks, 1):
            status = "✓" if task["completed"] else " "
            task_list.append(f"{index}. [{status}] {task['task']}")
        return "\n".join(task_list)

    def complete_task(self, task_number):
        if 1 <= task_number <= len(self.tasks):
            self.tasks[task_number - 1]["completed"] = True
            return "Task marked as completed"
        return "Invalid task number"

    def delete_task(self, task_number):
        if 1 <= task_number <= len(self.tasks):
            del self.tasks[task_number - 1]
            return "Task deleted successfully"
        return "Invalid task number"