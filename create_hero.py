from tkinter import *
import time

root = Tk()
WIDTH_SCREEN = 1280
HEIGHT_SCREEN = 720
root.geometry("{}x{}".format(WIDTH_SCREEN, HEIGHT_SCREEN))
root.configure(bg="black")
root.resizable(width=False, height=False)
root.title("GAME OF FIRE")

create_hero_label = Label(root, text="СОЗДАЙ СОБСТВЕННОГО ГЕРОЯ", bg="black", fg="gold", font=("Press Start 2P", 30))

create_hero_label.pack()
create_hero_label.place(x = 130, y=80)


entry_name_label= Label(root, text="Имя героя: ", bg="black", fg="gold", font=("Press Start 2P", 15))
entry_name_label.pack()
entry_name_label.place(x = 330, y = 350)

entry_name = Entry(root, bg="black", fg="gold", font=("Press Start 2P", 15), borderwidth=2, highlightbackground="black")
entry_name.pack()
entry_name.place(x = 550, y=345)
entry_name.configure(disabledbackground="gold")



start_game = Button(root, bg="gold", fg="black", font=("Press Start 2P", 15), text="НАЧАТЬ ПРИКЛЮЧЕНИЕ", borderwidth=4, highlightbackground="gold")
start_game.pack()
start_game.place(x = 470, y = 600)

def button_clicked(event=None):
    time.sleep(1)
    root.destroy()
    import main_gui
start_game.bind('<Return>', button_clicked)

entry_name.focus()
root.mainloop()
