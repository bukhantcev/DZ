import model
import view


def start():
    save_index = 1
    model.open_file()
    view.show_message("Файл успешно открыт")
    while True:
        pb = model.get_phone_book()
        choice = view.main_menu()
        match choice:
            case 1:
                model.open_file()
                view.show_message("Файл успешно открыт")
            case 2:
                model.save_file()
                view.show_message("Файл успешно сохранен")
                save_index = 1
            case 3:
                view.show_contact(pb, 'Телефонная книга пуста или не открыта')
            case 4:
                model.add_contact(view.add_contact())
                save_index = 0
            case 5:
                if view.show_contact(pb, 'Телефонная книга пуста или не открыта'):
                    index = view.input_index("Введите номер изменяемого контакта: ")
                    contact = view.change_contact(pb, index)
                    model.change_contact(contact, index)
                    view.input_index(f'Контакт {model.get_phone_book()[index-1].get("name")} успешно изменен!')
                    save_index = 0
            case 6:
                search = view.input_search('Введите искомый элемент: ')
                result = model.find_contact(search)
                view.show_contact(result, 'Контакты не найдены')
            case 7:
                if view.show_contact(pb, 'Телефонная книга пуста или не открыта'):
                    index = view.input_index("Введите номер удаляемого контакта: ")
                    model.delete_contact(index)
                    view.show_message("Контакт успешно удален!")
                    save_index = 0

            case 8:
                if save_index == 1:
                    return
                else:
                    if view.input_index('''Файл не сохранен! Хотите сохранить перед выходом? 
                    1 - Да
                    0 - Нет 
                    ''') == 0:
                        return
                    else:
                        model.save_file()
                        view.show_message("Файл успешно сохранен")
                        return






