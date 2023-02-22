# Найдите сумму цифр трехзначного числа.
# Пример:
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

input_num = input("Введите трехзначное число: ")
divider = 10 ** (len(input_num) - 1)
input_num = int(input_num)
result = input_num // divider
input_num = input_num % divider
divider = divider / 10
result = result + input_num // divider
input_num = input_num % divider
divider = divider / 10
result = result + input_num // divider
input_num = input_num % divider
divider = divider / 10
print(f"Сумма цифр трехзначного числа равна {int(result)}")


