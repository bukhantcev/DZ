# 1. Открыть файл
# 2. Сохранить файл
# 3. Показать все контакты
# 4. Найти контакт
# 5. Добавить контакт
# 6. Изменить контакт
# 7. Удалить контакт
# 8. Выход
my_file = "phonebook.txt"
data = []
def open_file(file):
    with open(file, "r", encoding="UTF-8") as my_file:
        data = list(map(lambda x: x.split(), my_file.readlines()))
    print("Файл открыт")
    return data
def main_menu(file):
    answer = int(input("Выберите нужный пункт меню: "))
    if answer > 8 or answer <= 0:
        print("В меню нет такого пункта")
    if answer == 1:

        return open_file(my_file)
    return
data = main_menu(my_file)
# print(" ".join(data[0]))




