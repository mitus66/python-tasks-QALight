# Завдання 1: Обробка набору даних про назви книг і авторів

# Опис проблеми:

# У вас є набір даних, що містить назви книг та їх авторів у форматі списку словників.

books_data = [
    {'title': 'Brave New World', 'author': 'Aldous Huxley'},
    {'title': '1984', 'author': 'George Orwell'},
    {'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald'},
    {'title': 'To Kill a Mockingbird', 'author': 'Harper Lee'},
    {'title': 'The Catcher in the Rye', 'author': 'J.D. Salinger'},
    {'title': 'Sapiens', 'author': 'Yuval Noah Harari'},
    {'title': 'Thinking, Fast and Slow', 'author': 'Daniel Kahneman'},
    {'title': 'Sapiens', 'author': 'Yuval Noah Harari'},
    {'title': 'Thinking, Fast and Slow', 'author': 'Daniel Kahneman'},
    {'title': 'The Lord of the Rings', 'author': 'J.R.R. Tolkien'},
    {'title': 'A Brief History of Time', 'author': 'Stephen Hawking'},
    {'title': 'Freakonomics', 'author': ['Steven D. Levitt', 'Stephen J. Dubner', 'Stephen Hawking']},
    {'title': 'Good Omens', 'author': ['Neil Gaiman', 'Terry Pratchett']},
    {'title': 'The Innovators', 'author': ['Walter Isaacson', 'Steve Wozniak']},
    {'title': 'Beautiful Code', 'author': ['Andy Oram', 'Greg Wilson', 'Steve Wozniak']}
]
# Ваше завдання:
# 1. Створіть словник, де кожен ключ є автором, а значенням є список назв книг, які вони написали.
# 2. Знайдіть авторів, які написали більше ніж вказану кількість книг.

# Зверніть увагу, що деякі автори, можливо, написали кілька книг.

# Виправив код з урахуванням зауважень:

from collections import defaultdict

# Створюємо словник, де ключем є автор, а значенням - множина книг
authors_books = defaultdict(set)

for book in books_data:
    authors = book['author']
    # Якщо у книги декілька авторів, обробляємо їх окремо
    if isinstance(authors, list):
        for author in authors:
            authors_books[author].add(book['title'])
    else:
        authors_books[authors].add(book['title'])

# Виводимо словник авторів та їх книг
for author, books in authors_books.items():
    print(f"{author}: {books}")

# Знаходимо авторів, які написали більше ніж 1 книгу
print("\nАвтори, які написали більше ніж 1 книгу:")
for author, books in authors_books.items():
    if len(books) > 1:
        print(f"{author}: {len(books)} книги")

'''Тепер результат такий:
Aldous Huxley: {'Brave New World'}
George Orwell: {'1984'}
F.Scott Fitzgerald: {'The Great Gatsby'}
Harper Lee: {'To Kill a Mockingbird'}
J.D.Salinger: {'The Catcher in the Rye'}
Yuval Noah Harari: {'Sapiens'}
Daniel Kahneman: {'Thinking, Fast and Slow'}
J.R.R.Tolkien: {'The Lord of the Rings'}
Stephen Hawking: {'A Brief History of Time', 'Freakonomics'}
Steven D.Levitt: {'Freakonomics'}
Stephen J.Dubner: {'Freakonomics'}
Neil Gaiman: {'Good Omens'}
Terry Pratchett: {'Good Omens'}
Walter Isaacson: {'The Innovators'}
Steve Wozniak: {'Beautiful Code', 'The Innovators'}
Andy Oram: {'Beautiful Code'}
Greg Wilson: {'Beautiful Code'}'''

'''Автори, які написали більше ніж 1 книгу:
Stephen Hawking: 2 книги
Steve Wozniak: 2 книги

Старий код:'''

## Lashyn Svitozar - нд 3 бер. 2024 15:40 PM Так, через set -- прекрасний варіант,
# і так менше треба переписувати, ніж якщо ми захочемо вставити один або кілька іфів.

# Чудово. Лаконічно і добре читається. І так, defaultdict -- хороший інструмент, який
# допомагає не думати, додавали ми вже такий ключ чи ні...
# Є одна проблемка. Бачите, що Юваль Ноель Харарі написав дві однакові книги? Що з цим можна зробити?

'''from collections import defaultdict

# Створюємо словник, де ключем є автор, а значенням - список книг
authors_books = defaultdict(list)

for book in books_data:
    authors = book['author']
    # Якщо у книги декілька авторів, обробляємо їх окремо
    if isinstance(authors, list):
        for author in authors:
            authors_books[author].append(book['title'])
    else:
        authors_books[authors].append(book['title'])

# Виводимо словник авторів та їх книг
for author, books in authors_books.items():
    print(f"{author}: {books}")

# Знаходимо авторів, які написали більше ніж 1 книгу
print("\nАвтори, які написали більше ніж 1 книгу:")
for author, books in authors_books.items():
    if len(books) > 2:
        print(f"{author}: {len(books)} книги")'''