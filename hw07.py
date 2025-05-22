'''
Завдання: Розробка простого веб-проєкту

Мета: Практика роботи з розгалуженнями та Pull Requests на GitHub через розробку простої структури веб-проєкту.



Вихідні дані:

Основна гілка репозиторію: main.



Завдання:

Створення гілки розробки:

Відмовтеся від гілки main і створіть гілку для розробки, назвавши її dev.

У гілці dev створіть базову структуру проєкту (наприклад, каталоги src, docs та файл README.md з описом проєкту).



Розробка функціональності:

Відмовтеся від гілки dev і створіть дві гілки для нових функцій:

feature-index-page для створення головної сторінки веб-сайту.

feature-contact-form для створення форми зворотного зв'язку.

У гілці feature-index-page додайте файл index.html з базовою HTML-структурою головної сторінки.

У гілці feature-contact-form  створіть файл contact.html і реалізуйте форму зворотного зв'язку (можете заповнити просто тегом h1).



Злиття функціональностей:

Злийте гілку feature-index-page назад у dev, вирішивши можливі конфлікти.

Злийте гілку feature-contact-form назад у dev, аналогічно вирішуючи конфлікти.



Створення Pull Request:

Створіть Pull Request з dev в main, що включає всі зміни, зроблені у гілках функціональності.

В описі Pull Request докладно опишіть внесені зміни та причину їх впровадження.
'''

# Попередня підготовка:
# Via PyCharm
# Right click the project
# Select 'Git'
# Select 'Manage Remote...'
# Click on [+]
# Name: origin
# URL: https://github.com/<team lead>/<MyProject>.git
# [OK]
# If you made a mistake with the URL, an error message will pop up and you have a chance to correct your URL
# When the Name and URL have been added, click on [OK]

# Маємо основну гілку репозиторію: main. Сторюємо файл, наприклад task_4_bot.py з командою print('Hello')
# Ініціюємо git

'''git init

# Перевіряємо статус
git status

# Створюємо стандартний файл .gitignore і додаємо файли під контроль git
git add .

# Робимо коміт
git commit -m "init commit"

# Створюємо нову гілку dev і переходимо в неї
git checkout -b dev

# Створюємо базову структуру проєкту з каталогами src, docs та файлом README.md
mkdir src
mkdir docs
echo "# Мій веб-проект" >> README.md

# Створюємо дві гілки: feature-index-page та feature-contact-form для розробки нових функцій
git checkout -b feature-index-page
git checkout -b feature-contact-form

# Переходимо до гілки feature-index-page
git checkout feature-index-page

# Створюємо файл index.html з базовою HTML-структурою головної сторінки
echo "# Home page" > index.html

# Додаємо файл під контроль git. Робимо коміт
git add .
git commit -m "make index.html"

# Переходимо до гілки feature-contact-form.
git checkout feature-contact-form

# Створюємо файл contact.html з формою зворотного зв'язку
echo "# Форма зворотного зв'язку" > contact.html

# Додаємо файл під контроль git. Робимо коміт
git add .
git commit -m "make contact.html"

# Переходимо до гілки dev.
git checkout dev

# Робимо злиття гілок в dev
git merge feature-index-page
git merge feature-contact-form

# Додаємо файли під контроль git. Робимо коміт
git add .
git commit -m "merg feature-index-page & feature-contact-form"

# Створюємо Pull Request
git push origin dev'''

# Відкриваємо GitHub-репозиторій
# Переходимо до гілки dev
# Натискаємо кнопку "Створити Pull Request"
# Вибераємо цільову гілку main
# Описуємо внесені зміни та причину їх впровадження
# Натискаємо кнопку "Створити Pull Request"
# Очікуємо Pull Request в гілку main
# Вирішуємо конфлікти злиття, якщо вони виникають
# Детально описуємо всі дії в Pull Request

## Все правильно, але відтсутня лінка на пул реквест. Додайте будь ласка до рішення.