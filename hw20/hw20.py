'''
Вам потрібно знайти студентів другого курсу, чиї оцінки з математики вищі за середній серед усіх студентів другого курсу, і відсортувати їх за оцінкою з фізики в порядку зменшення.

data.json data.json16 березня 2024, 18:57 PM

'''

# 1. Завантаження та обробка даних:
import json

with open("data.json", "r") as f:
    data = json.load(f)

students = []
for student in data:
    students.append(
        {
            "name": student["name"],
            "course": student["course"],
            "math_grade": student["grades"]["math"],
            "physics_grade": student["grades"]["physics"],
        }
    )

# 2. Розрахунок середнього балу з математики:
math_grades = [student["math_grade"] for student in students if student["course"] == 2]
average_math_grade = sum(math_grades) / len(math_grades)

# 3. Вибір студентів з балами з математики вище середнього:
above_average_students = [
    student for student in students if student["course"] == 2 and student["math_grade"] > average_math_grade
]

# 4. Сортування за балом з фізики:
sorted_students = sorted(
    above_average_students, key=lambda student: student["physics_grade"], reverse=True
)

# 5. Вивід результатів:
for student in sorted_students:
    print(f"{student['name']}: {student['physics_grade']}")

# Judy: 95
# Frank: 90

# Або теж саме через функції:

import json

def load_data(filename):
    with open(filename, "r") as f:
        data = json.load(f)

    students = []
    for student in data:
        students.append(
            {
                "name": student["name"],
                "course": student["course"],
                "math_grade": student["grades"]["math"],
                "physics_grade": student["grades"]["physics"],
            }
        )

    return students

def calculate_average_math_grade(students):
    math_grades = [student["math_grade"] for student in students if student["course"] == 2]
    return sum(math_grades) / len(math_grades)

def filter_above_average_students(students, average_math_grade):
    return [
        student for student in students if student["course"] == 2 and student["math_grade"] > average_math_grade
    ]

def sort_by_physics_grade(students):
    return sorted(students, key=lambda student: student["physics_grade"], reverse=True)

def print_results(students):
    for student in students:
        print(f"{student['name']}: {student['physics_grade']}")

def main():
    students = load_data("data.json")
    average_math_grade = calculate_average_math_grade(students)
    above_average_students = filter_above_average_students(students, average_math_grade)
    sorted_students = sort_by_physics_grade(above_average_students)
    print_results(sorted_students)

if __name__ == "__main__":
    main()

# Judy: 95
# Frank: 90

## Добре. усміхаюсь