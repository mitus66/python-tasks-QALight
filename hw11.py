'''
Опис завдання:

Вам надано список транзакцій із різними валютами. Ваше завдання - визначити для кожної валюти свою стелю суми транзакції. Якщо сума транзакції перевищує встановлену стелю, транзакція вважається такою, що не пройшла і повинна бути відзначена з висновком її transaction_id. Для транзакцій, що не перевищують стелю, необхідно розрахувати і вивести загальну суму транзакцій для кожної валюти.

Параметри стелі транзакцій:

USD: 10000
EUR: 8000
GBP: 7000



transactions = [
    {'transaction_id': 'T1001', 'amount': 150.0, 'currency': 'USD', 'timestamp': '2021-09-01T12:00:00'},
    {'transaction_id': 'T1002', 'amount': 9800.0, 'currency': 'EUR', 'timestamp': '2021-09-01T12:05:00'},
    {'transaction_id': 'T1003', 'amount': 12050.0, 'currency': 'GBP', 'timestamp': '2021-09-01T12:10:00'},
    {'transaction_id': 'T1004', 'amount': 250.0, 'currency': 'USD', 'timestamp': '2021-09-01T12:15:00'},
    {'transaction_id': 'T1005', 'amount': 5000.0, 'currency': 'EUR', 'timestamp': '2021-09-01T12:20:00'},
    {'transaction_id': 'T1006', 'amount': 7500.0, 'currency': 'GBP', 'timestamp': '2021-09-01T12:25:00'},
    {'transaction_id': 'T1007', 'amount': 20000.0, 'currency': 'USD', 'timestamp': '2021-09-01T12:30:00'},
    {'transaction_id': 'T1008', 'amount': 300.0, 'currency': 'EUR', 'timestamp': '2021-09-01T12:35:00'},
    {'transaction_id': 'T1009', 'amount': 450.0, 'currency': 'GBP', 'timestamp': '2021-09-01T12:40:00'},
    {'transaction_id': 'T1010', 'amount': 15000.0, 'currency': 'USD', 'timestamp': '2021-09-01T12:45:00'}
]
'''

'''Опис:

Цей код Python аналізує список транзакцій з різними валютами, визначає для кожної валюти стелю суми транзакції, та
генерує вихідні дані з наступними характеристиками:

Транзакції, що не пройшли:
ID транзакції(transaction_id)
Сума транзакції(amount)
Валюта(currency)

Транзакції, що пройшли:
Загальна сума транзакцій для кожної валюти

Код:'''


def process_transactions(transactions):
    # Словники для зберігання результатів
    failed_transactions = {}
    total_amounts = {}

    # Стеля транзакцій для кожної валюти
    currency_limits = {
        "USD": 10000,
        "EUR": 8000,
        "GBP": 7000,
    }

    # Обробка транзакцій
    for transaction in transactions:
        currency = transaction["currency"]
        amount = transaction["amount"]
        transaction_id = transaction["transaction_id"]

        # Перевірка на перевищення стелі
        if amount > currency_limits[currency]:
            failed_transactions[transaction_id] = {
                "amount": amount,
                "currency": currency,
            }
        else:
            # Додати до загальної суми
            total_amounts.setdefault(currency, 0)
            total_amounts[currency] += amount

    return failed_transactions, total_amounts


transactions = [
    {'transaction_id': 'T1001', 'amount': 150.0, 'currency': 'USD', 'timestamp': '2021-09-01T12:00:00'},
    {'transaction_id': 'T1002', 'amount': 9800.0, 'currency': 'EUR', 'timestamp': '2021-09-01T12:05:00'},
    {'transaction_id': 'T1003', 'amount': 12050.0, 'currency': 'GBP', 'timestamp': '2021-09-01T12:10:00'},
    {'transaction_id': 'T1004', 'amount': 250.0, 'currency': 'USD', 'timestamp': '2021-09-01T12:15:00'},
    {'transaction_id': 'T1005', 'amount': 5000.0, 'currency': 'EUR', 'timestamp': '2021-09-01T12:20:00'},
    {'transaction_id': 'T1006', 'amount': 7500.0, 'currency': 'GBP', 'timestamp': '2021-09-01T12:25:00'},
    {'transaction_id': 'T1007', 'amount': 20000.0, 'currency': 'USD', 'timestamp': '2021-09-01T12:30:00'},
    {'transaction_id': 'T1008', 'amount': 300.0, 'currency': 'EUR', 'timestamp': '2021-09-01T12:35:00'},
    {'transaction_id': 'T1009', 'amount': 450.0, 'currency': 'GBP', 'timestamp': '2021-09-01T12:40:00'},
    {'transaction_id': 'T1010', 'amount': 15000.0, 'currency': 'USD', 'timestamp': '2021-09-01T12:45:00'}
]

# Запуск функції з тестовими даними
failed_transactions, total_amounts = process_transactions(transactions)

# Вивід результатів
print("Неуспішні транзакції:")
for transaction_id, details in failed_transactions.items():
    print(f"  ID: {transaction_id}")
    print(f"    Сума: {details['amount']}")
    print(f"    Валюта: {details['currency']}")

print("Загальні суми транзакцій:")
for currency, total_amount in total_amounts.items():
    print(f"  {currency}: {total_amount}")

'''Пояснення коду:

Функція process_transactions приймає список транзакцій(transactions) та обробляє їх.
Словники failed_transactions та total_amounts використовуються для зберігання результатів.
Словник currency_limits містить стелю транзакцій для кожної валюти.

Для кожної транзакції:
Перевіряється, чи перевищує сума транзакції стелю. Якщо так, транзакція додається до failed_transactions.
Інакше сума транзакції додається до total_amounts для відповідної валюти. 
Функція повертає кортеж(failed_transactions, total_amounts).
Тестові дані використовуються для демонстрації роботи коду. Результати виводяться на консоль.

Результат:

Неуспішні транзакції:
ID: T1002
Сума: 9800.0
Валюта: EUR

ID: T1003
Сума: 12050.0
Валюта: GBP

ID: T1006
Сума: 7500.0
Валюта: GBP

ID: T1007
Сума: 20000.0
Валюта: USD

ID: T1010
Сума: 15000.0
Валюта: USD

Загальні суми транзакцій:
USD: 400.0
EUR: 5300.0
GBP: 450.0

Process finished with exit code 0'''

## Прекрасне рішення.