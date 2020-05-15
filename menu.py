import curses, time

menu = ["НАЧАТЬ НОВУЮ ИГРУ", "ПРОДОЛЖИТЬ", "НАСТРОЙКИ", "ВЫХОД"]

def show_menu(stdscr, selected_row):
    """Модель меню в центре терминала"""
    stdscr.clear()
    y, x = stdscr.getmaxyx()

    for indx, element in enumerate(menu):
        width = x // 2 - len(element) // 2
        height = y // 2 - len(menu) + indx
        if(indx == selected_row):
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(height, width, element)
            stdscr.attroff(curses.color_pair(1))
        else:
            stdscr.addstr(height, width, element)

    stdscr.refresh()

        
def main(stdscr):
    curses.curs_set(0)

    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

    current_position = 0
    show_menu(stdscr,current_position)
   
    while True:
        key = stdscr.getch()
        stdscr.clear()
        if(key == curses.KEY_DOWN and current_position < len(menu) - 1):
            current_position += 1
            stdscr.refresh()
        elif(key == curses.KEY_UP and current_position > 0):
            current_position -= 1
            stdscr.refresh() 
        elif(key == curses.KEY_ENTER):
            stdscr.clear()
            stdscr.addstr("You pressed {}".format(menu[current_position]))
            stdscr.refresh()
            stdscr.getch()
        show_menu(stdscr,current_position)
        stdscr.refresh()


curses.wrapper(main)
