# Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца.
# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны.
# Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля).
# Примечание: бинарной операцией называется любая операция, у которой ровно
# два аргумента, как, например, у операции умножения.


operation = lambda x, y: [x, y]


def print_operation_table(operation, num_rows=6, num_columns=6):
    list_row = []
    list_col = []
    print_row = ""
    res = None
    # for i in range(num_rows):
    #     for k in range(num_columns):
    #         res = (i + 1) * (k + 1)
    #         print_row = print_row + " " + str(res)
    #     print(print_row)
    #     print_row = ""

    for i in range(num_rows):
        for k in range(num_columns):
            res = (i + 1) * (k + 1)
            list_row.append(res)
        list_col.append(list_row)
        list_row = []
    print(f"Iskomii element = {list_col[operation[0] - 1][operation[1] - 1]}")
    return
list_row = []
ist_col = []
print_row = ""
num_rows = 6
num_columns = 6
print("Dana tablica: ")
for i in range(num_rows):
    for k in range(num_columns):
        res = (i + 1) * (k + 1)
        print_row = print_row + " " + str(res)
    print(print_row)
    print_row = ""
row = int(input("Vvedite nomer stroki: "))
col = int(input("Vvedite nomer stolbca: "))

print_operation_table(operation(row, col))


