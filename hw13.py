'''
Напишіть функцію для пошуку найдовшого спільного рядка префікса серед масиву рядків.

Якщо загального префікса немає, поверніть порожній рядок "".



Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""


Пояснення: серед вхідних рядків немає спільного префікса.
'''

def longest_common_prefix(strs):
    if not strs:
        return ""
    shortest_str = min(strs, key=len)
    for i, char in enumerate(shortest_str):
        for other in strs:
            if other[i] != char:
                return shortest_str[:i]
    return shortest_str

strs1 = ["flower","flow","flight"]
strs2 = ["dog","racecar","car"]

print(longest_common_prefix(strs1))  # Виведе: "fl"
print(longest_common_prefix(strs2))  # Виведе: ""

# Прекрасно, нема до чого причепитись. усміхаюсь