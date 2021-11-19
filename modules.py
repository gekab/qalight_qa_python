def exit_menu():
    print('Программа завершает свою работу')
    exit(0)


def checking():
    answer = input("Вы подтверждаете выбранное действие?(да/нет)")
    if answer == "да":
        return 1
    else:
        return 0


def create_menu(lst, new_item_menu=''):
    if new_item_menu == '':
        new_item_menu = input("Введите новый раздел в меню:")
        lst.append(new_item_menu)
    else:
        lst.append(new_item_menu)
    return 0


def find_item_menu(lst,sub_menu):
    if sub_menu in lst:
        return sub_menu
    else:
        if checking():
            create_menu(lst, sub_menu)
            return sub_menu
        else:
            exit_menu()


def edit_menu(lst, sub_menu, new_item):
    if sub_menu in lst:
        if find_item_menu(lst, sub_menu):
            lst[lst.index(sub_menu)] = new_item
    else:
        print('Данной записи нет в меню. Программа завершает свою работу.')
        exit_menu()

def del_submenu(lst, sub_menu):
    print('Вы действительно желаете удалить подменю?')
    if checking():
        if find_item_menu(lst, sub_menu):
            lst.remove(sub_menu)
    else:
        exit_menu()


