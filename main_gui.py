from tkinter import *
import time
from handler import validate_phrase

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
        borderwidth=0, highlightthickness=0, selectbackground="gold", highlightcolor="green", width=100)

health_label = Label(text="Здоровье:", bg="black", fg="gold")

health_player = 100
health_label = Label(text="Здоровье: {}".format(health_player), bg="black", fg="gold")
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
    a = "А ты зачем спрашиваешь, старик?"
    b = "Ищу семью, может вы знаете?"
    c = "Проваливай, рухлядь чердачная"
    for i in (a, b, c):
        answer_box.insert(END, i)
    
    answer_box.bind('<Return>', answer_box_clicked)

def config_health_label():
    health_label.pack(expand=1, anchor=SW)
    health_label.place(x = 37, y=670)
    health_label.config(font=("Press Start 2P", 10))



#handler
def answer_box_clicked(event):
   answer_box_get_result()
   clear_all_boxes()
   set_new_phrases()
def clear_all_boxes():
   dialog_box['text'] = ""
   answer_box.delete(0, END)

def answer_box_get_result():
    index_result = answer_box.curselection()
    global answer_player
    answer_player = answer_box.get(index_result)

def set_new_phrases():
    new_phrases_list = validate_phrase(answer_player)
    main_phrase = new_phrases_list[0]
    dialog_box['text'] = main_phrase
    new_player_phrases = new_phrases_list[1]
    for i in new_player_phrases:
        answer_box.insert(END, i)


#START PROGRAM
def main():
    config_main_name()
    config_dialog_frame()
    config_dialog_box()
    config_answer_frame()
    config_answer_box()
    config_health_label()
    answer_box.focus()
    root.mainloop()

main()
