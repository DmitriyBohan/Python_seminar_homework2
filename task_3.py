""" 
Задана последовательность натуральных чисел, завершающаяся числом 0. 
Требуется определить значение второго по величине элемента в этой последовательности, 
то есть элемента, который будет наибольшим, 
если из последовательности удалить наибольший элемент.

Пример:

1
7
9
0

Вывод:

7 
"""

import random
numbers = [random.randint(0, 100) for i in range(4)]
print(numbers, end=' -> ')


def find_max(numbers):
    max = numbers[0]
    for i in range(len(numbers)):
        if numbers[i] > max:
            max = numbers[i]
    return max


numbers.remove(find_max(numbers))
print(find_max(numbers))
