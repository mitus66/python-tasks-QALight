'''
Допоможіть жабі знайти шлях до свободи
У вас є масив цілих чисел і жаба на першому місці

[Frog, int, int, int, ..., int]

Саме ціле число може вказати вам довжину та напрямок стрибка

Наприклад:
 2 = jump two indices to the right
-3 = jump three indices to the left
 0 = stay at the same position
Ваше завдання — знайти, скільки стрибків потрібно, щоб вискочити з масиву.

Повертає -1, якщо жаба не може вискочити з масиву

Приклад:
array = [1, 2, 1, 5];
jumps = 3  (1 -> 2 -> 5 -> <jump out>)
Усі тести для цього Kata генеруються випадковим чином.

Приклад:

test.assert_equals(solution([1, 2, 2, -1]), 4)
        test.assert_equals(solution([1, 2, 1, 5]), 3)
        test.assert_equals(solution([1, -1]), -1)
'''

def jumps_count(array):
  jumps = 0      # кількість стрибків
  position = 0   # поточне положення жаби
  visited_position = set() # відвідані позиції

  while 0 <= position < len(array):
    if position in visited_position:
      return -1
    visited_position.add(position)
    position += array[position]
    jumps += 1

  return jumps

#Input
test_one = [1, 2, 2, -1]
test_two = [1, 2, 1, 5]
test_three = [1, -1]

# Output
print(jumps_count(test_one))
print(jumps_count(test_two))
print(jumps_count(test_three))

# Круто!