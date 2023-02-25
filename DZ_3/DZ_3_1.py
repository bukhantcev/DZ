# Первая задача:
# Задаем длину списка наполненного рандомными числами от 1 до 100.
# Вводим искомое число X
# Программа должна вывести в консоль сколько раз встречается в заданном списке искомое число X,
# которое мы вводим с клавиатуры, либо выводим на экран, максимально близкое ему по значению

import  random

list_1 = [random.randint(0, 100) for _ in range(0, 600)]
print(list_1)
result = 0
result_if = 0
difference = 0

my_number = int(input("Введите число: "))
new_difference = my_number
for i in list_1:
    if i == my_number:
        result += 1
    difference = i - my_number
    if difference < 0:
        difference *= -1
    if difference < new_difference:
        new_difference = difference
        result_if = i

print(f"Искомое число встречается {result} раз")
if result == 0:
    print(f"Ближайшее по значению число {result_if}")