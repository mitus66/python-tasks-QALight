'''
Дано цілий масив nums, повертає третє окреме максимальне число в цьому масиві. Якщо третій максимум не існує, поверніть максимальне число.



Example 1:

Input: nums = [3,2,1]
Output: 1
Explanation:
The first distinct maximum is 3.
The second distinct maximum is 2.
The third distinct maximum is 1.
Example 2:

Input: nums = [1,2]
Output: 2
Explanation:
The first distinct maximum is 2.
The second distinct maximum is 1.
The third distinct maximum does not exist, so the maximum (2) is returned instead.
Example 3:

Input: nums = [2,2,3,1]
Output: 1
Explanation:
The first distinct maximum is 3.
The second distinct maximum is 2 (both 2's are counted together since they have the same value).
The third distinct maximum is 1.
'''

'''Алгоритм розв’язання задачі пошуку третього максимуму в масиві:

Видалення дублікатів: Спочатку перетворимо вхідний масив nums на множину, щоб видалити будь - які дублікати чисел.

Сортування у спадному порядку: Відсортуємо масив nums у спадному порядку.Це дозволить нам отримати числа в порядку спадання.

Перевірка наявності третього максимуму:
Якщо кількість унікальних чисел у масиві nums більше або дорівнює 3, повернемо третє максимальне число(індекс 2 у відсортованому масиві).
Інакше повернемо максимальне число(індекс 0 у відсортованому масиві), оскільки третій максимум не існує.
Ось реалізація цього алгоритму'''


def third_max(nums):
    # Видаляємо дублікати
    nums = list(set(nums))

    # Сортуємо у спадному порядку
    nums.sort(reverse=True)

    # Перевіряємо, чи є третій максимум
    if len(nums) >= 3:
        return nums[2]
    else:
        # Якщо третій максимум не існує, повертаємо максимальне число
        return max(nums)


# Приклади вхідних даних
example1 = [3, 2, 1]
example2 = [1, 2]
example3 = [2, 2, 3, 1]

# Вивід результатів
print(third_max(example1))  # Виведе 1
print(third_max(example2))  # Виведе 2
print(third_max(example3))  # Виведе 1