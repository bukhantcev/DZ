# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты
# вверх одной и той же стороной. Выведите минимальное количество м
import random
quan_coin = int(input('Введите количество монет: '))
face1 = 0
face2 = 0
for i in range(0, quan_coin):

    coin_face = random.randint(0, 1)
    # print(coin_face)
    if coin_face == 0:
        face1 += 1
    else:
        face2 += 1
print(f'Орел = {face1}')
print(f'Решка = {face2}')
if face1 < face2:
    print(f'Минимальное количество монет = {face1}')
else:
    print(f'Минимальное количество монет = {face2}')
