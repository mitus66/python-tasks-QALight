'''
Завдання те саме що і до заняття 35, тільки пишемо його на шаблонах
'''

'''
Для переписання коду на шаблони у Flask, необхідно використовувати бібліотеку Jinja2, яка є вбудованою у Flask для створення HTML-шаблонів. Ми будемо створювати HTML-шаблони, які будуть відображати результати гонок у форматі таблиці.

Кроки для реалізації:
Створення HTML-шаблонів.
Модифікація Flask-додатка для використання шаблонів.
Додавання маршруту для рендерингу шаблонів.
Структура проекту
project/
├── templates/
│   └── race_results.html
├── __init__.py
├── app.py
├── file_handler.py
└── report.py

1. Створення HTML-шаблонів
templates/race_results.html
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Race Results</title>
    <style>
        table {
            width: 50%;
            border-collapse: collapse;
            margin: 25px 0;
            font-size: 18px;
            text-align: left;
        }
        th, td {
            padding: 12px;
            border-bottom: 1px solid #ddd;
        }
        th {
            background-color: #f2f2f2;
        }
    </style>
</head>
<body>
    <h1>Race Results</h1>
    <table>
        <thead>
            <tr>
                <th>№</th>
                <th>Driver</th>
                <th>Company</th>
                <th>Race Time</th>
            </tr>
        </thead>
        <tbody>
            {% for row in race_table %}
            <tr>
                <td>{{ row['position'] }}</td>
                <td>{{ row['driver'] }}</td>
                <td>{{ row['company'] }}</td>
                <td>{{ row['race_time'] }}</td>
            </tr>
            {% endfor %}
        </tbody>
    </table>
</body>
</html>

2. Модифікація Flask-додатка
app.py
from flask import Flask, render_template, request
import os
from report import main as main_report, sort_race_logs
from file_handler import read_data_fromfile

app = Flask(__name__)

@app.route('/race_results', methods=['GET'])
def get_race_results():
    folder = request.args.get('folder', default='racing_data', type=str)
    order = request.args.get('order', default='asc', type=str)
    driver = request.args.get('driver', default='', type=str)

    if order not in ['asc', 'desc']:
        return render_template('error.html', error="Invalid order value, should be 'asc' or 'desc'"), 400

    try:
        race_results, abbrs = main_report(folder)
        race_results_sorted = sort_race_logs(race_results, order)
        race_table = prepare_race_table(race_results_sorted, abbrs, driver)
        if not race_table:
            return render_template('error.html', error="Driver not found"), 404
        return render_template('race_results.html', race_table=race_table)
    except FileNotFoundError as e:
        return render_template('error.html', error=str(e)), 404
    except Exception as e:
        return render_template('error.html', error=str(e)), 500

def prepare_race_table(race_results: dict[str, str], abbrs: dict[str, tuple[str, str]], current_driver: str):
    """Prepare race data to print"""
    race_table = []
    for counter, code in enumerate(race_results, 1):
        driver = abbrs[code][0]
        company = abbrs[code][1]
        race_time = race_results[code]
        if current_driver:
            if driver == current_driver:
                race_table.append({"position": counter, "driver": driver, "company": company, "race_time": race_time})
                break
            continue
        race_table.append({"position": counter, "driver": driver, "company": company, "race_time": race_time})

    if current_driver and not race_table:
        return False
    return race_table

if __name__ == '__main__':
    app.run(debug=True)

3. Створення шаблону для помилок
templates/error.html
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Error</title>
</head>
<body>
    <h1>Error</h1>
    <p>{{ error }}</p>
</body>
</html>

Пояснення коду
Шаблон race_results.html:

Цей HTML-шаблон відображає результати гонки у вигляді таблиці.
Використовуються цикли Jinja2 для відображення кожного рядка даних.
Flask-додаток:

get_race_results тепер використовує render_template для рендерингу HTML-шаблонів.
Якщо є помилка, наприклад, неправильне значення параметра order або файл не знайдено, відповідний шаблон помилки буде відображений.
Шаблон error.html:

Відображає повідомлення про помилку.
Цей код дозволяє отримувати результати гонки та відображати їх у вигляді HTML-сторінки, використовуючи шаблони Flask. Ви можете запустити додаток та отримати доступ до маршруту /race_results у браузері, щоб побачити результати у вигляді таблиці.
'''

# Все так. усміхаюсь