from tkinter import *

root = Tk()
WIDTH_SCREEN = 1280
HEIGHT_SCREEN = 720
root.geometry("{}x{}".format(WIDTH_SCREEN, HEIGHT_SCREEN))
root.configure(bg="black")
root.resizable(width=False, height=False)
root.title("GAME OF FIRE")

create_hero_label = Label(root, text="СОЗДАЙ СОБСТВЕННОГО ГЕРОЯ", bg="black", fg="gold", font=("Press Start 2P", 30))

create_hero_label.pack()
create_hero_label.place(x = 130, y=60)


entry_name_label= Label(root, text="Имя героя: ", bg="black", fg="gold", font=("Press Start 2P", 15))
entry_name_label.pack()
entry_name_label.place(x = 330, y = 200)

entry_name = Entry(root, bg="black", fg="gold", font=("Press Start 2P", 15), borderwidth=2, highlightbackground="gold")
entry_name.pack()
entry_name.place(x = 550, y=195)
entry_name.configure(disabledbackground="gold")

entry_race_label= Label(root, text="Раса героя: ", bg="black", fg="gold", font=("Press Start 2P", 15))
entry_race_label.pack()
entry_race_label.place(x = 330, y = 500)

entry_race = Entry(root, bg="black", fg="gold", font=("Press Start 2P", 15), borderwidth=2, highlightbackground="gold")
entry_race.pack()
entry_race.place(x = 550, y=495)
entry_race.configure(disabledbackground="gold")
root.mainloop()
