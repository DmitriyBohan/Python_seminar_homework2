""" 
Напишите программу, которая принимает на вход вещественное число 
и показывает сумму его цифр.

Пример:

6782 -> 23
0,56 -> 11 
"""


number_input = input("Введите число: ")
sum = 0
number_type = number_input.find('.')
if number_type < 0:

    number = int(number_input)
    while number > 0:
        sum += number % 10
        number //= 10
else:
    number_division = number_input.split('.')
    integer_number = int(number_division[0])
    fractional_number = int(number_division[1])
    while integer_number > 0:
        sum += integer_number % 10
        integer_number //= 10
    while fractional_number > 0:
        sum += fractional_number % 10
        fractional_number //= 10
print("сумма цифр равна: ", sum)
