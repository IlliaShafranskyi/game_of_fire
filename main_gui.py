from tkinter import *
import time
def main():
    root = Tk()

    #Main window config
    WIDTH_SCREEN = 1280
    HEIGHT_SCREEN = 720
    root.geometry("{}x{}".format(WIDTH_SCREEN, HEIGHT_SCREEN))
    root.configure(bg="black")
    root.resizable(width=False, height=False)
    root.title("GAME OF FIRE")


    #Main name config
    main_name = Label(root, text="GAME OF FIRE", bg="black", fg="gold")
    CENTER_MAIN_NAME = WIDTH_SCREEN//2 - len("GAME OF FIRE")// 2
    main_name.pack(pady=30)
    main_name.config(font=("Press Start 2P", 15))



    #Dialog frame and label config
    dialog_frame = Frame(root, width = WIDTH_SCREEN - 80, height = HEIGHT_SCREEN // 3 + 20, bg="black", 
            highlightbackground="gold", highlightthickness=6)

    CENTER_FRAME = WIDTH_SCREEN//2 - dialog_frame['width']//2
    dialog_frame.pack(anchor=NW)
    dialog_frame.place(x=CENTER_FRAME, y=80) 
    dialog_frame.pack_propagate(0)
    dialog_box = Label(dialog_frame, bg="black", fg="gold", wraplength=1000)

    dialog_box['text']="Слушай чудак, а тебя как сюда вообще занесло?"
    dialog_box.config(font=("Podkova ExtraBold", 13))

    dialog_box.pack(expand=1, anchor=NW, padx=20,pady=20)



    #Answer frame and listbox config 
    answer_frame = Frame(root, width = WIDTH_SCREEN - 80, height = HEIGHT_SCREEN // 3 + 20, bg="black", 
            highlightbackground="gold", highlightthickness=6)

    answer_frame.pack(anchor=NW)
    answer_frame.place(x=CENTER_FRAME, y=380) 
    answer_frame.pack_propagate(0)

    answer_box = Listbox(root, bg="black", fg="gold", 
            borderwidth=0, highlightthickness=0, selectbackground="gold", width=105)
    answer_box.config(font=("Podkova ExtraBold", 13))
    answer_box.pack(anchor=NW)
    answer_box.place(x=70, y=410)
    
    
    def get_selection():
        result = answer_box.curselection()
        return result

    health_label = Label(text="Здоровье:", bg="black", fg="gold")
    health_label.pack(expand=1, anchor=SW)
    health_label.place(x = 37, y=670)
    health_label.config(font=("Press Start 2P", 10))

    

    answer_box.focus()
    root.mainloop()

main()
