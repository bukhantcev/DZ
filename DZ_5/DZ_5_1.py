# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и
# возводит число А в целую степень B с помощью рекурсии.
a = int(input("Enter A: "))
b = int(input("Enter B: "))
def my_function(num, degree, result = 1):

    if degree == 0:
        print(result)
        return
    else:
        result = result * num
        my_function(num, degree - 1, result)
my_function(a, b)



