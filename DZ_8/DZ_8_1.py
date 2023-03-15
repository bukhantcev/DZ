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
def open_file(file):                                        # Открывает файл
    with open(file, "r", encoding="UTF-8") as my_file:
        data = list(map(lambda x: x.split(), my_file.readlines()))
    print("Файл открыт")
    return data

def search_contakt(data: list):                             # Поиск контакта по фамилии, имени, номеру или статусу.  Доработать регистр
    answer = input("Введите информацию для поиска: ")
    for i in range(len(data)):
        if answer in data[i]:
            print(" ".join(data[i]))
            index = i
    return index
def show_all(file):                                         # Показывает все имеющиеся контакты
    with open(file, "r", encoding="UTF-8") as my_file:
        print(my_file.read())
    return
def main_menu(file, answer = 0):                            # Главное меню
    answer = int(input("Выберите нужный пункт меню: "))
    if answer > 8 or answer <= 0:
        print("В меню нет такого пункта")
    if answer == 8:
        print("Программа окончена")
        return "", answer
    if answer == 3:
        show_all(my_file)
        return "", answer
    if answer == 4:
        search_contakt(data)
        return "", answer
    if answer == 1:
        return open_file(my_file), answer
    return
data = main_menu(my_file)[0]                             # Записывает данные из файла в список data
while main_menu(my_file)[1] < 8:                        # Запуск программы
    main_menu(my_file)





