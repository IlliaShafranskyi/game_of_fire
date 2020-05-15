import curses

def main(stdscr):
    stdscr.border(0)
    
    y, x = stdscr.getmaxyx()
    height = y // 2
    main_name = stdscr.addstr(1, (x // 2 - len("GAME OF FIRE") // 2), "GAME OF FIRE")
    
    dialog_box = curses.newwin(height - 2, x-2, 2, 1)
    dialog_box.box()
    
    answers_box= curses.newwin(height - 2, x-2, 14, 1)
    answers_box.box()

    stdscr.refresh()
    dialog_box.addstr(1, 1,"Hello")
    dialog_box.refresh()
    answers_box.refresh()

    stdscr.getch()


curses.wrapper(main)
