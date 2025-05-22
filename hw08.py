'''
Our fruit guy has a bag of fruit (represented as an array of strings) where some fruits are rotten.

He wants to replace all the rotten pieces of fruit with fresh ones.

For example, given ["apple","rottenBanana","apple"] the replaced array should be ["apple","banana","apple"].

Your task is to implement a method that accepts an array of strings containing fruits should returns an array

of strings where all the rotten fruits are replaced by good ones.



Notes

If the array is null/nil/None or empty you should return empty array ([]).

The rotten fruit name will be in this camelcase (rottenFruit).

The returned array should be in lowercase.



['rottenKiwi', 'strawberry', 'mango', 'rottenBanana', 'tomato', 'apple']

['kiwi', 'strawberry', 'mango', 'banana', 'tomato', 'apple']
'''

'''Алгоритм вирішення задачі

Вхід:
fruits: список рядків, що представляють фрукти, де деякі фрукти можуть бути гнилими.

Вихід:
fresh_fruits: новий список, де всі гнилі фрукти замінені свіжими, всі рядки в нижньому регістрі.

Кроки:
Перевірка порожнього списку:
Перевірити: Чи є fruits пустим списком(None, [], або len(fruits) == 0).

Дія: Якщо так, повернути порожній список[].

Ітерація по фруктах:
Цикл: Перебрати всі фрукти в списку fruits.
Обробка: Для
кожного
фрукта:
Перевірка
гнилі:
Перевірити: Чи починається фрукт(у нижньому регістрі) з "rotten".

Дія:
Гнилий: Витягти назву свіжого фрукта, відрізавши "rotten" і перевівши в нижній регістр.
Додати свіжий фрукт до нового списку fresh_fruits.
Не гнилий: Додати фрукт(у нижньому регістрі) до нового списку fresh_fruits.
Повернення результату:
Повернути: список fresh_fruits.
 
Розтлумачення: 
Крок 1: Перевірка порожнього списку гарантує, що алгоритм правильно обробляє відсутність фруктів.
Крок 2: Цикл for використовується для перебору всіх фруктів у списку fruits.
Крок 2.1: Перевірка гнилі використовує.lower() для порівняння назви фрукта без урахування регістру.
Крок 2.2: Для гнилих фруктів використовується fruit[6:].lower() для вилучення назви свіжого фрукта 
після "rotten" та переведення її в нижній регістр. 
Крок 3: Повертає список fresh_fruits, що містить всі свіжі фрукти в нижньому регістрі.

Приклад:
Вхід: fruits = ["rottenKiwi", "strawberry", "mango", "rottenBanana", "tomato", "apple"]
Вихід: fresh_fruits = ["kiwi", "strawberry", "mango", "banana", "tomato", "apple"]

Рішення:'''


def replace_rotten(fruits):
    """Replaces rotten fruits with fresh ones in a list of fruits, handling edge cases and ensuring clarity.

    Args:
        fruits (list[str]): A list of fruit strings, potentially containing rotten fruits.

    Returns:
        list[str]: A new list with rotten fruits replaced by fresh ones, all lowercase.
    """

    if not fruits:  # Check for empty list and return empty list
        return []

    fresh_fruits = []
    for fruit in fruits:
        if fruit.lower().startswith("rotten"):  # Handle case-insensitive rotten fruit names
            fresh_fruits.append(fruit[6:].lower())  # Extract fresh fruit name and lowercase
        else:
            fresh_fruits.append(fruit.lower())  # Keep non-rotten fruit, lowercase

    return fresh_fruits


# Example usage
fruits = ["rottenKiwi", "strawberry", "mango", "rottenBanana", "tomato", "apple"]
fresh_fruits = replace_rotten(fruits)
print(fresh_fruits)  # Output: ['kiwi', 'strawberry', 'mango', 'banana', 'tomato', 'apple']

'''
Пара мілких зауважень по коду:
if fruit.lower().startswith("rotten"):  # це не є обов'язковим, за уомовою rotten вже в нижньому ...
 '''