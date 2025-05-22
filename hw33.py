'''
Завдання: Розробка системи керування замовленнями
Ціль: Метою даного завдання є практика у створенні та використанні винятків користувача в контексті системи управління замовленнями. Студенти навчаться визначати та обробляти різні види помилок, специфічних для бізнес-логіки.

Завдання:
Студенти повинні створити кілька класів, які моделюватимуть процес замовлення продуктів в онлайн-магазині, а також розробити винятки для обробки можливих помилок.

Компоненти системи:
Клас Product:
Властивості: назва продукту, ціна.
Методи: ні.
Клас Order:
Властивості: список продуктів, статус замовлення (наприклад, новий, оброблений, виконаний, скасований).
Методи: додавання продукту на замовлення, видалення продукту із замовлення, розрахунок загальної вартості замовлення.
Клас Inventory:
Властивості: доступні продукти та їх кількість.
Методи: перевірка наявності товару, оновлення кількості після замовлення.
Визначення винятків користувача:
ProductNotFoundError: Викликається, якщо намагаються замовити продукт, якого немає в інвентарі.
OutOfStockError: Викликається, якщо намагаються замовити більше продукту, ніж доступно.
OrderAlreadyCompletedError: Викликається при спробі змінити замовлення, яке вже виконано.
'''

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Order:
    def __init__(self):
        self.items = []
        self.status = "new"

    def add_product(self, product):
        self.items.append(product)

    def remove_product(self, product):
        self.items.remove(product)

    def calculate_total(self):
        total = 0
        for product in self.items:
            total += product.price
        return total

    def complete(self):
        if self.status == "new":
            self.status = "completed"
        else:
            raise OrderAlreadyCompletedError("Замовлення вже виконано.")

    def cancel(self):
        if self.status == "new":
            self.status = "canceled"
        else:
            raise OrderAlreadyCompletedError("Замовлення вже виконано.")


class Inventory:
    def __init__(self, products):
        self.products = products

    def check_stock(self, product, quantity):
        if product not in self.products:
            raise ProductNotFoundError(f"Продукт '{product.name}' не знайдено.")

        if self.products[product] < quantity:
            raise OutOfStockError(f"Недостатньо '{product.name}' на складі. Доступно лише {self.products[product]} шт.")

    def update_stock(self, product, quantity):
        self.products[product] -= quantity


class ProductNotFoundError(Exception):
    pass


class OutOfStockError(Exception):
    pass


class OrderAlreadyCompletedError(Exception):
    pass


# Створення продуктів і сховища
product1 = Product("Laptop", 1000)
product2 = Product("Phone", 500)
inventory = Inventory({product1: 10, product2: 5})

# Створення замовлення
order = Order()

# Додавання продуктів до замовлення
order.add_product(product1)
order.add_product(product2)

# Перевірка наявності та оновлення кількості на складі
try:
    inventory.check_stock(product1, 2)
    inventory.update_stock(product1, 2)
except ProductNotFoundError as e:
    print(f"Помилка: {e}")
except OutOfStockError as e:
    print(f"Помилка: {e}")

# Розрахунок загальної вартості замовлення
total_price = order.calculate_total()
print(f"Загальна вартість замовлення: {total_price}")

# Спроба змінити виконане замовлення
try:
    order.add_product(product2)
except OrderAlreadyCompletedError as e:
    print(f"Помилка: {e}")

# Скасування замовлення
order.cancel()
print(f"Статус замовлення: {order.status}")

## Круто)