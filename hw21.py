'''
Функція приймає ID користувача та повертає загальну кількість виконаних, невиконаних завдань користувача.
https://jsonplaceholder.typicode.com/todos
'''

import requests


def get_todos(user_id):
    """Завантажує дані про завдання користувача з JSONPlaceholder API."""
    url = f"https://jsonplaceholder.typicode.com/todos?userId={user_id}"
    response = requests.get(url)
    return response.json()


def count_completed_and_todo(todos):
    """Рахує загальну кількість виконаних та невиконаних завдань. """
    completed_count = 0
    todo_count = 0
    for todo in todos:
        if todo["completed"]:
            completed_count += 1
        else:
            todo_count += 1

    return completed_count, todo_count


def get_user_task_counts(user_id):
    """ Повертає загальну кількість виконаних та невиконаних завдань користувача."""
    todos = get_todos(user_id)
    completed_count, todo_count = count_completed_and_todo(todos)
    return completed_count, todo_count


user_id = 10

completed_count, todo_count = get_user_task_counts(user_id)

print(f"User_Id: {user_id}")
print(f"Виконано: {completed_count}")
print(f"Залишилося: {todo_count}")

# User_Id: 1
# Виконано: 11
# Залишилося: 9

# User_Id: 10
# Виконано: 12
# Залишилося: 8

## Круто. усміхаюсь