from datetime import datetime
from tkinter import *


class Pakiet:
    wiadomosc = ""
    etykieta = 0
    klasaFEC = 0
    bledny = FALSE
    etykietaBlad = FALSE


nadaneEtykiety = 0
blednePakiety = 0
bledyNadawaniaEtykiet = 0


def czas():
    now = datetime.now()
    return now.strftime("\n[%H:%M:%S] ")


def log(tekst):
    textareaWin3.insert(INSERT, czas() + tekst)
    textareaWin3.grid(column=0, row=0, rowspan=10)

def wyczysc_okno():
    textareaWin3.delete('1.0', END)
    global nadaneEtykiety
    global blednePakiety
    global bledyNadawaniaEtykiet
    nadaneEtykiety = 0
    blednePakiety = 0
    bledyNadawaniaEtykiet = 0
    l1 = Label(win3, text=nadaneEtykiety)
    l2 = Label(win3, text=blednePakiety)
    l3 = Label(win3, text=bledyNadawaniaEtykiet)
    l1.grid(column=2, row=0)
    l2.grid(column=2, row=1)

def wyslij_wiadomosc():
    global nadaneEtykiety
    global blednePakiety
    global bledyNadawaniaEtykiet

    pakiet = Pakiet()
    if czyBledny.get() == 1:
        pakiet.bledny = TRUE
    else:
        pakiet.bledny = FALSE

    if czyBladEtykiety.get() == 1:
        pakiet.etykietaBlad = TRUE
    else:
        pakiet.etykietaBlad = FALSE

    pakiet.klasaFEC = entry2.get()
    pakiet.etykieta = entry3.get()

    textareaWin2.delete('1.0', END)

    log("Otrzymano pakiet. Sprawdź czy jest sklasyfikowany.")
    if not pakiet.klasaFEC:
        log("Pakiet nie posiada klasy. Przypisz klasę FEC")
        pakiet.klasaFEC = "1234"
    else:
        log("Pakiet sklasyfikowany. Przejdź do nadawania etykiety.")

    pakiet.wiadomosc = textareaWin1.get("1.0", END)
    log("Sprawdź czy pakiet ma etykietę.")
    if not pakiet.etykieta:  # jeśli pakiet nie ma etykiety
        log("Brak etykiety. Odczytaj klasę pakietu.")
        log("Nadaj nową etykietę.")
        pakiet.etykieta = "1234"
        nadaneEtykiety = nadaneEtykiety + 1
        if pakiet.etykietaBlad:  # jeśli niepowiodło się nadawanie etykiety
            log("Nie udało się nadać etykiety. Sprawdź poprawność pakietu.")
            bledyNadawaniaEtykiet = bledyNadawaniaEtykiet + 1
            if pakiet.bledny:  # jeśli pakiet jest błędny
                log("Pakiet uszkodzony. Zapisz w logach.")
            else:
                log("Pakiet poprawny. Ponów nadawanie etykiety. Przekaż pakiet.")
                textareaWin2.insert(INSERT, pakiet.wiadomosc)
        else:
            log("Przekaż pakiet dalej.")
            textareaWin2.insert(INSERT, pakiet.wiadomosc)
    else:
        log("Sprawdź czy następnym odbiorcą jest router.")
        log("Odczytaj nową wartość etykiety i zweryfikuj")
        if pakiet.etykietaBlad:
            log("Wartość etykiety niepoprawna. Zapisz w logach.")
            log("Nie udało się nadać etykiety. Sprawdź poprawność pakietu.")
            bledyNadawaniaEtykiet = bledyNadawaniaEtykiet + 1
            if pakiet.bledny:  # jeśli pakiet jest błędny
                log("Pakiet uszkodzony. Zapisz w logach.")
                blednePakiety = blednePakiety + 1
            else:
                log("Pakiet poprawny. Ponów nadawanie etykiety. Przekaż pakiet.")
                textareaWin2.insert(INSERT, pakiet.wiadomosc)
        else:
            pakiet.etykieta = "1234"
            log("Nadano etykietę.")
            nadaneEtykiety = nadaneEtykiety + 1
            log("Przekaż pakiet dalej.")
            textareaWin2.insert(INSERT, pakiet.wiadomosc)

    l1 = Label(win3, text=nadaneEtykiety)
    l2 = Label(win3, text=blednePakiety)
    l3 = Label(win3, text=bledyNadawaniaEtykiet)
    l1.grid(column=2, row=0)
    l2.grid(column=2, row=1)
    l3.grid(column=2, row=2)
    textareaWin2.pack()


win1 = Tk()
win1.title("Użytkownik 1")
win1.geometry("300x250")
textareaWin1 = Text(win1, bg="white", fg="black", width=30, height="4", padx="5", pady="5")
btn = Button(win1, text="Prześlij wiadomość", command=wyslij_wiadomosc)
entry1 = Entry(win1, bg="white", fg="black", width=24)
czyBledny = IntVar()
czyBladEtykiety = IntVar()
checkBtn1 = Checkbutton(win1, text="Błedny pakiet", variable=czyBledny)
checkBtn2 = Checkbutton(win1, text="Błąd nadawania etykiety", variable=czyBladEtykiety)
entry2 = Entry(win1, bg="white", fg="black", width=12)
entry3 = Entry(win1, bg="white", fg="black", width=12)

Label(win1, text="Wiadomość").grid(column=0, columnspan=2, row=0)
textareaWin1.grid(column=0, columnspan=2, row=1)
Label(win1, text="Opcje pakietu").grid(column=0, columnspan=2, row=2)
checkBtn1.grid(column=0, row=3)
checkBtn2.grid(column=1, row=3)
Label(win1, text="Etykieta").grid(column=0, row=4)
entry2.grid(column=1, row=4)
Label(win1, text="Klasa FEC").grid(column=0, row=5)
entry3.grid(column=1, row=5)
btn.grid(column=0, columnspan=2, row=6)

win2 = Tk()
win2.title("Użytkownik 2")
win2.geometry("300x150")
label = Label(win2, text="Otrzymana wiadomość")
textareaWin2 = Text(win2, bg="white", fg="black", width="30", height="4", padx="5", pady="5")

label.pack()
textareaWin2.pack()

win3 = Tk()
win3.title("Przebieg protokołu")
win3.geometry("730x300")
l1 = Label(win3, text=nadaneEtykiety)
l2 = Label(win3, text=blednePakiety)
l3 = Label(win3, text=bledyNadawaniaEtykiet)

Label(win3, text="Nadane etykiety").grid(column=1, row=0)
l1.grid(column=2, row=0)
Label(win3, text="Błedne pakiety").grid(column=1, row=1)
l2.grid(column=2, row=1)
Label(win3, text="Błędy nadawania etykiet").grid(column=1, row=2)
l3.grid(column=2, row=2)
textareaWin3 = Text(win3, bg="white", fg="black", width="70", height="20", padx="20", pady="10")
textareaWin3.grid(column=0, row=0, rowspan=10)
Button(win3, text="Wyczyść okno", command=wyczysc_okno).grid(column=1, columnspan=2, row=3)

win3.mainloop()
