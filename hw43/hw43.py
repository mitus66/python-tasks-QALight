'''
Зробити таблицю як на скріншоті та перенести логіку завдання зі створення, оновлення видалення та зміни даних у таблиці users. Приклад того коли ми додавали користувачів до текстового файлу.

photo_2024-05-16_14-53-13.jpg photo_2024-05-16_14-53-13.jpg16 травня 2024, 14:54 PM

'''

'''
Для виконання завдання з перенесення логіки роботи з користувачами з текстового файлу до бази даних, нам знадобиться налаштувати SQLAlchemy у Flask-додатку. Також додамо CRUD-операції для роботи з таблицею users.

Кроки:
Налаштування бази даних у Flask.
Створення моделі для таблиці users.
Додавання CRUD-операцій.
Оновлення шаблонів для роботи з даними з бази.
1. Налаштування бази даних у Flask
Додамо SQLAlchemy до нашого Flask-додатку.

requirements.txt
Flask
Flask-SQLAlchemy

app.py
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    first_name = db.Column(db.String(50), nullable=True)
    last_name = db.Column(db.String(50), nullable=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    is_superuser = db.Column(db.Boolean, default=False)
    is_staff = db.Column(db.Boolean, default=False)
    is_active = db.Column(db.Boolean, default=True)
    last_login = db.Column(db.DateTime, nullable=True)
    date_joined = db.Column(db.DateTime, default=datetime.utcnow)

@app.route('/')
def index():
    users = User.query.all()
    return render_template('index.html', users=users)

@app.route('/add', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        new_user = User(username=username, password=password, first_name=first_name,
                        last_name=last_name, email=email)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add_user.html')

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update_user(id):
    user = User.query.get_or_404(id)
    if request.method == 'POST':
        user.username = request.form['username']
        user.password = request.form['password']
        user.first_name = request.form['first_name']
        user.last_name = request.form['last_name']
        user.email = request.form['email']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('update_user.html', user=user)

@app.route('/delete/<int:id>')
def delete_user(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)

2. Створення шаблонів
Створимо прості HTML-шаблони для відображення, додавання та оновлення користувачів.

templates/index.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Users List</title>
</head>
<body>
    <h1>Users List</h1>
    <a href="{{ url_for('add_user') }}">Add User</a>
    <table>
        <thead>
            <tr>
                <th>ID</th>
                <th>Username</th>
                <th>Email</th>
                <th>First Name</th>
                <th>Last Name</th>
                <th>Actions</th>
            </tr>
        </thead>
        <tbody>
            {% for user in users %}
            <tr>
                <td>{{ user.id }}</td>
                <td>{{ user.username }}</td>
                <td>{{ user.email }}</td>
                <td>{{ user.first_name }}</td>
                <td>{{ user.last_name }}</td>
                <td>
                    <a href="{{ url_for('update_user', id=user.id) }}">Edit</a>
                    <a href="{{ url_for('delete_user', id=user.id) }}">Delete</a>
                </td>
            </tr>
            {% endfor %}
        </tbody>
    </table>
</body>
</html>

templates/add_user.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Add User</title>
</head>
<body>
    <h1>Add User</h1>
    <form method="POST">
        <label for="username">Username:</label>
        <input type="text" id="username" name="username"><br>
        <label for="password">Password:</label>
        <input type="password" id="password" name="password"><br>
        <label for="first_name">First Name:</label>
        <input type="text" id="first_name" name="first_name"><br>
        <label for="last_name">Last Name:</label>
        <input type="text" id="last_name" name="last_name"><br>
        <label for="email">Email:</label>
        <input type="email" id="email" name="email"><br>
        <button type="submit">Add User</button>
    </form>
    <a href="{{ url_for('index') }}">Back to Users List</a>
</body>
</html>

templates/update_user.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Update User</title>
</head>
<body>
    <h1>Update User</h1>
    <form method="POST">
        <label for="username">Username:</label>
        <input type="text" id="username" name="username" value="{{ user.username }}"><br>
        <label for="password">Password:</label>
        <input type="password" id="password" name="password" value="{{ user.password }}"><br>
        <label for="first_name">First Name:</label>
        <input type="text" id="first_name" name="first_name" value="{{ user.first_name }}"><br>
        <label for="last_name">Last Name:</label>
        <input type="text" id="last_name" name="last_name" value="{{ user.last_name }}"><br>
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" value="{{ user.email }}"><br>
        <button type="submit">Update User</button>
    </form>
    <a href="{{ url_for('index') }}">Back to Users List</a>
</body>
</html>

3. Запуск проекту
Встановлюємо залежності з requirements.txt.
Запускаємо Flask-додаток:
export FLASK_APP=app.py
flask run

Відкриваємо браузер і перейдіть на http://127.0.0.1:5000/ для перевірки роботи додатку.
Таким чином, ми налаштували базу даних для зберігання користувачів та реалізували CRUD-операції для роботи з цією базою за допомогою Flask і SQLAlchemy.
'''


# Браво)