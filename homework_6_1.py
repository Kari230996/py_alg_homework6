'''
Практическая работа №6

Работа с динамической памятью
'''

'''Python 3.10.1'''
'''ОС Windows 10 x64'''

'''3.6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
 Сами минимальный и максимальный элементы в сумму не включать.'''

import random
import sys
from size_counter import size_counter


'''1 Вариант'''



N = 100


n = []

for i in range(N):
    random_ = random.randint(0, 99)
    n.append(random_)
print(n)

maxi = n[0]
max_count = n.count(maxi)

for i in n:
    if n.count(i) > max_count:
        maxi = i
        max_count = n.count(i)


print('Число', maxi, 'встречается', max_count, 'раз(а)')

sum_member = (n, N, maxi, max_count)
sum_ = 0
for i in sum_member:
    sum_ += size_counter(i)

print(f'В программе задействовано байт памяти: {sum_}')

# В программе задействовано байт памяти: 3800
# 1 список и 3 три переменные типа инт

'''
type(data)=<class 'list'> sys.getsizeof(data)=920 data=[38, 36, 61, 13, 57, 92, 87, 35, 37, 92, 88, 88, 86, 68, 54, 29, 19, 66, 68, 5, 6, 52, 76, 36, 86, 43, 77, 49, 30, 3, 5, 85, 77, 42, 92, 67, 53, 7, 85, 54, 24, 89, 92, 36, 0, 54, 43, 3, 61, 29, 26, 57, 13, 28, 86, 16, 81, 90, 75, 32, 70, 85, 61, 87, 34, 37, 96, 17, 42, 50, 88, 25, 6, 56, 22, 42, 67, 15, 54, 65, 74, 20, 4, 5, 26, 96, 87, 79, 87, 82, 94, 6, 36, 52, 29, 35, 88, 1, 54, 31]
type(data)=<class 'int'> sys.getsizeof(data)=28 data=100
type(data)=<class 'int'> sys.getsizeof(data)=28 data=54
type(data)=<class 'int'> sys.getsizeof(data)=28 data=5
'''