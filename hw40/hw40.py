'''
Покрити юніт тестами модуль "елементи"

elements.zip elements.zip8 травня 2024, 21:59 PM

'''

'''
Щоб створити unit-тести для модуля task_4_bot.py, ми будемо використовувати бібліотеку unittest. Ми протестуємо різні функції, які визначені у файлі task_4_bot.py.

Підготовка до тестування
Спершу, створимо окремий файл для тестів, наприклад, test_main.py. Переконаємося, що файл elements.txt доступний для тестування, або створимо його копію у тестовому каталозі.

Структура проекту
/project_root
    /data
        elements.txt
    task_4_bot.py
    test_main.py

Зміст test_main.py
import unittest
from main import check_file, check_element_format, read_elements_from_file, find_element, Element
from pathlib import Path
import os

class TestMainFunctions(unittest.TestCase):

    def setUp(self):
        """Create a temporary elements.txt file for testing"""
        self.test_file_path = str(Path(__file__).parent.joinpath('data').joinpath('elements.txt'))
        if not os.path.exists(os.path.dirname(self.test_file_path)):
            os.makedirs(os.path.dirname(self.test_file_path))
        with open(self.test_file_path, 'w') as f:
            f.write("1,H,Hydrogen\n2,He,Helium\n11,Na,Sodium\n")

    def tearDown(self):
        """Remove the temporary elements.txt file after testing"""
        if os.path.exists(self.test_file_path):
            os.remove(self.test_file_path)

    def test_check_file(self):
        self.assertTrue(check_file(self.test_file_path))
        self.assertFalse(check_file("non_existent_file.txt"))

    def test_check_element_format(self):
        self.assertTrue(check_element_format("1,H,Hydrogen"))
        self.assertTrue(check_element_format("2,He,Helium"))
        self.assertFalse(check_element_format("1,H,Hydrogenium"))
        self.assertFalse(check_element_format("H,Hydrogen"))

    def test_read_elements_from_file(self):
        elements = read_elements_from_file(self.test_file_path)
        self.assertEqual(len(elements), 3)
        self.assertEqual(elements[0], Element(1, 'H', 'Hydrogen'))
        self.assertEqual(elements[1], Element(2, 'He', 'Helium'))
        self.assertEqual(elements[2], Element(11, 'Na', 'Sodium'))

    def test_find_element(self):
        elements = read_elements_from_file(self.test_file_path)
        element = find_element(elements, 'Na')
        self.assertIsNotNone(element)
        self.assertEqual(element, Element(11, 'Na', 'Sodium'))
        self.assertIsNone(find_element(elements, 'Unknown'))

if __name__ == '__main__':
    unittest.main()

Опис тестів
test_check_file:

Перевіряє, чи існує файл і чи є він текстовим файлом.
Використовує правильний шлях до файлу та неіснуючий файл для перевірки.
test_check_element_format:

Перевіряє правильність формату елементів.
Використовує коректні та некоректні рядки для тестування.
test_read_elements_from_file:

Перевіряє, чи правильно зчитуються елементи з файлу.
Використовує тимчасовий файл для перевірки функції.
test_find_element:

Перевіряє, чи правильно знаходяться елементи за їх скороченнями.
Використовує список елементів для пошуку.
Запуск тестів
Для запуску тестів потрібно виконати наступну команду в терміналі, перебуваючи в кореневій директорії проекту:

python -m unittest test_main.py

Це забезпечить виконання всіх тестів і виведе результати тестування.

Зміни у task_4_bot.py
Додатково, для кращого відокремлення функціональності та тестування, рекомендується трохи змінити модуль task_4_bot.py, щоб забезпечити легше тестування.

Додамо можливість передавати шлях до файлу та пошуковий запит у функцію main: if __name__ == '__main__':
    import sys
    if len(sys.argv) == 3:
        filepath1 = sys.argv[1]
        user_search1 = sys.argv[2]
    else:
        file = 'elements.txt'
        filepath1 = str(Path(__file__).parent.joinpath('data').joinpath(file))
        user_search1 = 'Na'
    main(filepath1, user_search1)
Ці зміни дозволять запускати скрипт з аргументами командного рядка, наприклад: python task_4_bot.py data/elements.txt Таким чином, ми створили unit-тести для всіх основних функцій у task_4_bot.py, забезпечивши перевірку коректної роботи програми.
'''

# Браво. усміхаюсь