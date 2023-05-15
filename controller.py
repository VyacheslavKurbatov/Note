import view


def start():
    while True:
        menu = view.ShowMenu()
        if menu == 8:
            return "Exit from programm"