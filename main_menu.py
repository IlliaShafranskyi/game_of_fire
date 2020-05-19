"""START GAME MENU"""

from tkinter import *

root = Tk()
root.title("GAME OF FIRE")
WIDTH_SCREEN = 1280
HEIGHT_SCREEN = 720
root.geometry("{}x{}".format(WIDTH_SCREEN, HEIGHT_SCREEN))
root.resizable(width=False, height=False)
root.configure(bg="black")


main_name = Label(root, text="GAME OF FIRE", bg="black",
        fg="gold", font=("Press Start 2P", 50))
main_name.pack()
main_name.place(x = 250, y=80)

main_menu = Listbox(root,  fg="gold", bg="black", borderwidth=0,
        highlightthickness=0, font=("Press Start 2P", 15))

start = "НАЧАТЬ ИГРУ"
exit = "ВЫХОД"
for i in (start, exit):
    main_menu.insert(END, i)

def menu_clicked(event):
    index_result = main_menu.curselection()
    result = main_menu.get(index_result)
    if(result == "НАЧАТЬ ИГРУ"):
        root.destroy()
        import main_gui
    elif(result == "ВЫХОД"):
        root.destroy()

MAIN_MENU_CENTER = WIDTH_SCREEN // 2 - main_menu['width'] // 2
main_menu.pack(expand=1)
main_menu.place(x = MAIN_MENU_CENTER - 190, y=360)
main_menu.configure(justify=CENTER)
main_menu.bind('<Return>', menu_clicked)
main_menu.focus()


author = Label(root, text="created by Illia Shafranskyi", bg="black",
        fg="gold", font=("Podkova Extrabold", 10))
author.pack()
author.place(x=540, y=685)
root.mainloop()
