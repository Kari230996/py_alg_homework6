'''
Практическая работа №6

Работа с динамической памятью
'''

'''Python 3.10.1'''
'''ОС Windows 10 x64'''

'''3.3  В массиве случайных целых чисел поменять местами минимальный и максимальный элементы'''


import sys
import random
from size_counter import size_counter

SIZE = 10

new = [random.randint(0, 99) for i in range(SIZE)]



maxi_ = new[new.index(sorted(new)[-1])]
mini_ = new[new.index(sorted(new)[0])]

new[new.index(maxi_)], new[new.index(mini_)] = new[new.index(mini_)], new[new.index(maxi_)]

#print(new)

sum_ = 0


for i in new:
    sum_ += size_counter(i)

print(f'Под переменные задействованно {sum_} байт памяти')


# Под переменные задействованно 280 байт памяти
# Переменная типа int

