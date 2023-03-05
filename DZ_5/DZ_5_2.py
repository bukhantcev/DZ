# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. Из всех арифметических операций допускаются только +1 и -1. Также нельзя
# использовать циклы.

a = int(input("Enter a: "))
b = int(input("Enter b: "))
def sum(a, b, result = 0):
    if a == 0:
        if b == 0:
            print(result)
            return
        else:
            result += 1
            sum(a, b - 1, result)
    else:
        result += 1
        sum(a - 1, b, result)
sum(a, b)




