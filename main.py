from tkinter import *

def uzytkownik1():
    win1 = Tk()
    win1.title("Użytkownik 1")
    win1.geometry("300x200")
    label1 = Label(win1, text="Wiadomość")
    textarea = Text(win1, bg="white", fg="black", width="30", height="4", padx="5", pady="5")
    btn = Button(win1, text="Prześlij wiadomość")
    label2 = Label(win1, text="Wiadomość zwrotna")
    entry = Entry(win1, bg="white", fg="black", width="24")

    label1.pack()
    textarea.pack()
    btn.pack()
    label2.pack()
    entry.pack()

def uzytkownik2():
    win2 = Tk()
    win2.title("Użytkownik 2")
    win2.geometry("300x150")
    label = Label(win2, text="Otrzymana wiadomość")
    textarea = Text(win2, bg="white", fg="black", width="30", height="4", padx="5", pady="5")

    label.pack()
    textarea.pack()

def demo():
    win3 = Tk()
    win3.title("Przebieg protokołu")
    win3.geometry("650x300")
    textarea = Text(win3, bg="white", fg="black", width="80", height="20", padx="20", pady="10")
    textarea.pack()

    win3.mainloop()

uzytkownik1()
uzytkownik2()
demo()
