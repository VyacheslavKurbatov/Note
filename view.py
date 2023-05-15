import notion


def ShowMenu():
    print('\n 1- Добавить заметку \n 2- Показать все заметки\n 3- Редактировать заметку\n 4- Удалить заметку\n 5- Сохранитьв файл\n 6- Загрузить базу\n 7- Сортировать по дате\n 8- Выход из меню\n')
    # Проверяем, что пользователь ввел число из диапазона меню от1 до 8
    while True:
        menu = input('\nВведите пункт меню: ')
        try:
            menu = int(menu)
        except ValueError:
            print('\nВведите пункт меню цифрами! Буквы вводить запрещено!')
            continue
        if 0 < menu < 9:
            break
        else:
            print('\nВ меню отсутствует данный пункт. Введите значения из диапазона от 1 до 8')

    if menu == 1:
        notion.addNote()
    elif menu == 2:
        notion.ShowAllNotion()
    elif menu == 3:
        notion.EditNotion()
    elif menu == 4:
        notion.DeleteNotion()
    elif menu == 5:
        notion.SaveBase()
    elif menu == 6:
        notion.LoadBase()
    elif menu == 7:
        notion.SortedDate()
    elif menu == 8:
        print('\nexit from programm\n')
    return menu