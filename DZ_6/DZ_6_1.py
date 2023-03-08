# Задача 30:  Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

difference = int(input("Vvedite raznost`: "))
quantity = int(input("Vvedite kolichestvo elementov`: "))
first_item = int(input("Vvedite pervii element`: "))

def fill_list(diff, quant, first):
    array = []
    for i in range(quant):
        array = array + [first]
        first += diff
    return array
print(f"Otvet: {fill_list(difference, quantity, first_item)}")
