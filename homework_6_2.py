'''
Практическая работа №6

Работа с динамической памятью
'''

'''Python 3.10.1'''
'''ОС Windows 10 x64'''

'''3.4'''

import sys
import random
from size_counter import size_counter



SIZE = 100

n = []

for i in range(SIZE):
    random_ = random.randint(0, 99)
    n.append(random_)

maxi = n[0]
max_count = n.count(maxi)

for i in n:
    if n.count(i) > max_count:
        maxi = i
        max_count = n.count(i)


#print('Число', maxi, 'встречается', max_count, 'раз(а)')
#print(n)

var_lst = (SIZE, n)
sum_ = 0

for i in var_lst:
    sum_ += size_counter(i)

print(f'Под переменные задействованно {sum_} байт памяти')

# Под переменные задействованно 3744 байт памяти
# В кортеже задействованны переменные типа int и list