def exit_menu():
    exit(0)


def create_menu(lst=[]):
    new_item_menu = input("Введите новый раздел в меню:")
    lst.append(new_item_menu)
    return 0


def find_item_menu(sub_menu, lst=[]):
    if len(lst) > 0:
        if sub_menu in lst:
            print(sub_menu)
        else:
            print("Меню не создано. Желаете создать?(да/нет)")
            otwet = input()
            if otwet == "да":
                create_menu(lst)
            else:
                exit_menu()
    else:
        print("Меню не создано. Желаете создать?(да/нет)")
        otwet = input()
        if otwet == "да":
            create_menu(lst)
        else:
            exit_menu()
    return 0
