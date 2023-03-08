# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат
# заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)
from random import randint as ri
minimum = int(input("Vvedite minimum diapazona: "))
maximum = int(input("Vvedite maximum diapazona: "))
my_list = [ri(0, 100) for _ in range(12)]
print(f"Zadan massiv: {my_list}")
result = []
for i in range(len(my_list) - 1):
    if my_list[i] >= minimum and my_list[i] <= maximum:
        result.append(i)
if result == []:
    print("Net elementov, udovletvoryashih usloviyu zadachi!")
else:
    print(f"V diapazon ot {minimum} do {maximum} vhodyt elementi so sleduyushimi indeksami: {result}")