""" 
Вклад в банке составляет X рублей. 
Ежегодно он увеличивается на P процентов, 
после чего дробная часть копеек отбрасывается.
Требуется определить: через сколько лет вклад составит не менее Y рублей.

Пример:

100
10
200

Вывод:

8 
"""

contribution = int(input('Первоначальный взнос: '))
interest = int(input('Укажите процентную ставку: '))
desired_amount = int(input('Желаемая сумма: '))
year = 0
while contribution <= desired_amount:
    contribution += int(contribution/100*interest)
    year += 1
print('Ваш вклад достигнет желаемой суммы через',year, 'лет и составит :',contribution,'рублей')

