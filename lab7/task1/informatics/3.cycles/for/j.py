'''
Задача №342. Сумма ста
Вычислите сумму данных 100 натуральных чисел.
'''
sum = 0
for i in range(100):
    sum += int(input())
print(sum)