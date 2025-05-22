'''
Дано ціле число n, поверніть відповідь у вигляді масиву рядків (з індексом 1), де:

answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i (as a string) if none of the above conditions are true.


Приклад 1:

Input: n = 3
Output: ["1","2","Fizz"]
Example 2:

Input: n = 5
Output: ["1","2","Fizz","4","Buzz"]
Example 3:

Input: n = 15
Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]


Обмеження:

1 <= n <= 104
'''

def fizzbuzz(n):
    result = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0: # Якщо i ділиться без остатку і на 3 і на 5
            result.append("FizzBuzz") # Додаємо "FizzBuzz" у список result
        elif i % 3 == 0:              # Якщо i ділиться без остатку на 3
            result.append("Fizz")     # Додаємо "Buzz" у список result
        elif i % 5 == 0:              # Якщо i ділиться без остатку на 5
            result.append("Buzz")     # Додаємо "Buzz" у список result
        else:                         # інакше
            result.append(str(i))     # дадаємо значення i
    return result

# Приклад виклику функції
n = 104
print(fizzbuzz(n))