'''
Знайдіть індекс першого входження в рядок

Дано два рядки needle і haystack, повертає індекс першого входження needle у haystack або -1, якщо needle не є частиною haystack.

Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.

Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
'''

def str_str(haystack, needle):
  """
  Функція знаходить індекс першого входження needle у haystack.

  Args:
      haystack (str): Рядок, в якому шукаємо.
      needle (str): Рядок, який шукаємо.

  Returns:
      int: Індекс першого входження needle, або -1, якщо needle не знайдено.
  """
  if needle == "":
    return 0

  len_needle = len(needle)
  for i in range(len(haystack) - len_needle + 1):
    if haystack[i:i + len_needle] == needle:
      return i

  return -1

# Приклади використання
haystack = "sadbutsad"
needle = "sad"
print(str_str(haystack, needle))  # 0

haystack = "leetcode"
needle = "leeto"
print(str_str(haystack, needle))  # -1


'''Пояснення:
Функція str_str приймає два рядки: haystack - рядок, в якому шукаємо, і needle - рядок, який шукаємо.
Якщо needle пустий рядок, то повертається 0.
Інакше, код використовує цикл for, щоб перебрати всі підрядки haystack довжиною len(needle).
В циклі for код порівнює поточний підрядок з needle.
Якщо підрядок збігається з needle, то функція повертає індекс цього підрядка.
Якщо needle не знайдено, то функція повертає -1.

Варіації:
Замість циклу for можна використовувати метод find.
Можна додати параметр start, щоб вказати, з якого символу haystack починати пошук.
Можна додати параметр end, щоб вказати, на якому символі haystack закінчити пошук.'''

# Чим простіше рішення тим краще. У данному випадку, дійсно краще  використовувати метод find.