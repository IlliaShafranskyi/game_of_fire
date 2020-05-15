from tkinter import *
import time

#INIT AND CONFIG MAIN WINDOW
root = Tk()
WIDTH_SCREEN = 1280
HEIGHT_SCREEN = 720
root.geometry("{}x{}".format(WIDTH_SCREEN, HEIGHT_SCREEN))
root.configure(bg="black")
root.resizable(width=False, height=False)
root.title("GAME OF FIRE")


#INITIALISATION MAIN WIDGETS AND FRAME
main_name = Label(root, text="GAME OF FIRE", bg="black", fg="gold")

dialog_frame = Frame(root, width = WIDTH_SCREEN - 80, height = HEIGHT_SCREEN // 3 + 20, bg="black", 
        highlightbackground="gold", highlightthickness=6)

dialog_box = Label(dialog_frame, bg="black", fg="gold", wraplength=1000)

answer_frame = Frame(root, width = WIDTH_SCREEN - 80, height = HEIGHT_SCREEN // 3 + 20, bg="black", 
        highlightbackground="gold", highlightthickness=6)

answer_box = Listbox(root, bg="black", fg="gold", 
        borderwidth=0, highlightthickness=0, selectbackground="gold", width=105)

health_label = Label(text="Здоровье:", bg="black", fg="gold")
#

#START AND CONFIGURATION ALL WIDGETS
def config_main_name():
    CENTER_MAIN_NAME = WIDTH_SCREEN//2 - len("GAME OF FIRE")// 2
    main_name.pack(pady=30)
    main_name.config(font=("Press Start 2P", 15))

def config_dialog_frame():
    global CENTER_FRAME     
    CENTER_FRAME = WIDTH_SCREEN//2 - dialog_frame['width']//2
    dialog_frame.pack(anchor=NW)
    dialog_frame.place(x=CENTER_FRAME, y=80) 
    dialog_frame.pack_propagate(0)

def config_dialog_box():
    dialog_box['text']="Слушай чудак, а тебя как сюда вообще занесло?"
    dialog_box.config(font=("Podkova ExtraBold", 13))
    dialog_box.pack(expand=1, anchor=NW, padx=20,pady=20)

def config_answer_frame():
    answer_frame.pack(anchor=NW)
    answer_frame.place(x=CENTER_FRAME, y=380) 
    answer_frame.pack_propagate(0)

def config_answer_box():
    answer_box.config(font=("Podkova ExtraBold", 13))
    answer_box.pack(anchor=NW)
    answer_box.place(x=70, y=410)

def config_health_label():
    health_label.pack(expand=1, anchor=SW)
    health_label.place(x = 37, y=670)
    health_label.config(font=("Press Start 2P", 10))



#other functions
def get_choice():
    result = 


def main():
    config_main_name()
    config_dialog_frame()
    config_dialog_box()
    config_answer_frame()
    config_answer_box()
    config_health_label()
    answer_box.focus()
    root.mainloop()



if(__name__ == "__main__"):
    main()
