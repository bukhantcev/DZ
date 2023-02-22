# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали
# билет с номером. Счастливым билетом называют такой билет с шестизначным номером, где сумма
# первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам
# требуется написать программу, которая проверяет счастливость билета.
# Пример:
# 385916 -> yes
# 123456 -> no

number_ticket = input("Введите номер билета: ")
simbol1 = int(number_ticket[0])
simbol2 = int(number_ticket[1])
simbol3 = int(number_ticket[2])
simbol4 = int(number_ticket[3])
simbol5 = int(number_ticket[4])
simbol6 = int(number_ticket[5])
result = simbol1 + simbol2 + simbol3 == simbol4 + simbol5 + simbol6
if result == True:
    print("Билет счастливый")
else:
    print("Билет не счастливый")


