# tests/test_todo.py
import pytest
from todooperations import TodoOperations

def test_add_task():
    todo = TodoOperations()
    result = todo.add_task("Test task")
    assert result == "Task added successfully"
    assert len(todo.tasks) == 1
    assert todo.tasks[0]["task"] == "Test task"

def test_complete_task():
    todo = TodoOperations()
    todo.add_task("Test task")
    result = todo.complete_task(1)
    assert result == "Task marked as completed"
    assert todo.tasks[0]["completed"] == True

def test_delete_task():
    todo = TodoOperations()
    todo.add_task("Test task")
    result = todo.delete_task(1)
    assert result == "Task deleted successfully"
    assert len(todo.tasks) == 0
