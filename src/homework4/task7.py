"""
Даны два натуральных числа. Вычислите их наибольший общий делитель
при помощи алгоритма Евклида (мы не знаем функции и рекурсию).
"""

num1 = int(input('Input first number: '))
num2 = int(input('Input second number: '))
while num1 and num2:
    if num1 > num2:
        num1 = num1 % num2
    else:
        num2 = num2 % num1
print(num1 + num2)
