'''
Ціль:
Метою цього завдання є розробка основних компонентів системи управління бібліотекою з використанням принципів ОВП, таких як інкапсуляція та поліморфізм.

Клас Book:

Кожна книга повинна мати назву, автора, рік видання та статус доступності.
Методи управління статусом книги (видана, повернута).


Клас User:

Користувачі бібліотеки повинні мати унікальний ідентифікатор, ім'я та список узятих книг.
Методи для додавання та видалення книг зі списку взятих.


Клас Librarian (успадковується від User):

Бібліотекар може додавати та видаляти книги з каталогу бібліотеки.
Бібліотекар може реєструвати нових користувачів та видаляти існуючих.


Клас Library:

Повинен містити каталог усіх книг та список усіх користувачів.
Методи для видачі книг користувачеві та прийому книг назад.
Методи для виведення інформації про всі книги або всіх користувачів.


Інкапсуляція:
Дані кожного класу мають бути захищені (використовувати приватні чи захищені атрибути там, де це необхідно).
Доступ до даних повинен здійснюватись через методи класу.
'''

class Book:
    def __init__(self, title, author, publication_year, status):
        self._title = title
        self._author = author
        self._publication_year = publication_year
        self._status = status

    def get_title(self):
        return self._title

    def get_author(self):
        return self._author

    def get_publication_year(self):
        return self._publication_year

    def get_status(self):
        return self._status

    def set_status(self, new_status):
        self._status = new_status

    def is_available(self):
        return self._status == "available"


class User:
    def __init__(self, user_id, name):
        self._user_id = user_id
        self._name = name
        self._checked_out_books = []

    def get_user_id(self):
        return self._user_id

    def get_name(self):
        return self._name

    def get_checked_out_books(self):
        return self._checked_out_books

    def add_checked_out_book(self, book):
        self._checked_out_books.append(book)

    def remove_checked_out_book(self, book):
        self._checked_out_books.remove(book)


class Librarian(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)

    def add_book_to_catalog(self, library, book):
        library.add_book(book)

    def remove_book_from_catalog(self, library, book):
        library.remove_book(book)

    def register_new_user(self, library, user):
        library.add_user(user)

    def remove_user(self, library, user_id):
        library.remove_user(user_id)


class Library:
    def __init__(self):
        self._book_catalog = []
        self._user_list = []

    def add_book(self, book):
        self._book_catalog.append(book)

    def remove_book(self, book):
        self._book_catalog.remove(book)

    def add_user(self, user):
        self._user_list.append(user)

    def remove_user(self, user_id):
        for user in self._user_list:
            if user.get_user_id() == user_id:
                self._user_list.remove(user)
                break

    def checkout_book(self, user, book):
        if book.is_available():
            book.set_status("checked_out")
            user.add_checked_out_book(book)
            print(f"Книга '{book.get_title()}' видана користувачеві '{user.get_name()}'.")
        else:
            print(f"Книга '{book.get_title()}' недоступна.")

    def return_book(self, user, book):
        if book in user.get_checked_out_books():
            book.set_status("available")
            user.remove_checked_out_book(book)
            print(f"Книга '{book.get_title()}' повернута користувачем '{user.get_name()}'.")
        else:
            print(f"Користувач '{user.get_name()}' не має книги '{book.get_title()}'.")

    def print_book_catalog(self):
        if self._book_catalog:
            print("\n**Каталог книг:**")
            for book in self._book_catalog:
                print(f"- {book.get_title()} ({book.get_author()}), {book.get_publication_year()}, {book.get_status()}")
        else:
            print("Каталог книг порожній.")

    def print_user_list(self):
        if self._user_list:
            print("\n**Список користувачів:**")
            for user in self._user_list:
                print(f"- Ідентифікатор: {user.get_user_id()}")
                print(f"  Ім'я: {user.get_name()}")
                print(f"  Книги на руках:")
                if user.get_checked_out_books():
                    for book in user.get_checked_out_books():
                        print(f"    - {book.get_title()} ({book.get_author()})")
                else:
                    print(f"    Користувач не має книг на руках.")
        else:
            print("Список користувачів порожній.")

# Добре. усміхаюсь