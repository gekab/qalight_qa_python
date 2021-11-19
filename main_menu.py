#  Т.к. меню это логичиски упорядочненная структура данных, то для решения этой задачи более всего подходят списки
import  modules as m


main_menu = []
m.create_menu(main_menu)
m.find_item_menu('Создать запись', main_menu)


print(main_menu)