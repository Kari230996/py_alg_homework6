'''
Практическая работа №6

Работа с динамической памятью
'''

'''Python 3.10.1'''
'''ОС Windows 10 x64'''

'''3.1'''

import sys
from size_counter import size_counter


num = {}

for i in range(2, 10):
    num[i] = []

    for j in range(2, 100):
        if i % j == 0:
            num[i].append(j)

    #print(f'Число {i} кратно - {num[i]}, количество кратности - {len(num[i])}')

sum_ = 0
var_lst = (num, i)
for i in var_lst:
    sum_ += size_counter(i)

#print(var_lst)
print(f'Под переменные задействованно {sum_} байт памяти')

# Под переменные задействованно 1316 байт памяти
# В кортеже задействованны словарь dict и переменная типа int


'''
В итоги, по моим наблюдениям, эффективным по памяти решение является первое, т.к. 
задействованно только одна переменная типа list, занимающее наименьшее место 280 байтов.
'''
