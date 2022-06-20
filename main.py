from datetime import datetime
from tkinter import *


class Pakiet:
    wiadomosc = ""
    etykieta = 0
    klasaFEC = 0
    bledny = FALSE
    etykietaBlad = FALSE

def czas():
    now = datetime.now()
    return now.strftime("\n[%H:%M:%S] ")


def log(tekst):
    textareaWin3.insert(INSERT, czas() + tekst)
    textareaWin3.pack(expand=1, fill=BOTH)


def wyslij_wiadomosc():
    log("Otrzymano pakiet. Sprawdź czy jest sklasyfikowany.")
    if pakiet.klasaFEC == 0:
        log("Pakiet nie posiada klasy. Przypisz klasę FEC")
        pakiet.klasaFEC = 1
    else:
        log("Pakiet sklasyfikowany. Przejdź do nadawania etykiety.")

    pakiet.wiadomosc = textareaWin1.get("1.0", END)
    log("Sprawdź czy pakiet ma etykietę.")
    if pakiet.etykieta == 0: # jeśli pakiet nie ma etykiety
        log("Brak etykiety. Odczytaj klasę pakietu.")
        log("Nadaj nową etykietę.")
        pakiet.etykieta = 1234
        if pakiet.etykietaBlad: # jeśli niepowiodło się nadawanie etykiety
            log("Nie udało się nadać etykiety. Sprawdź poprawność pakietu.")
            if pakiet.bledny: # jeśli pakiet jest błędny
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
        else:
            pakiet.etykieta = 1324
            log("Nadano etykietę.")
            if pakiet.etykieta == 0:
                log("Nie udało się nadać etykiety. Sprawdź poprawność pakietu.")
                if pakiet.bledny:  # jeśli pakiet jest błędny
                    log("Pakiet uszkodzony. Zapisz w logach.")
                else:
                    log("Pakiet poprawny. Ponów nadawanie etykiety. Przekaż pakiet.")
                    textareaWin2.insert(INSERT, pakiet.wiadomosc)
            else:
                log("Przekaż pakiet dalej.")
                textareaWin2.insert(INSERT, pakiet.wiadomosc)



    textareaWin2.pack(expand=1, fill=BOTH)


win1 = Tk()
win1.title("Użytkownik 1")
win1.geometry("300x200")
label1 = Label(win1, text="Wiadomość")
textareaWin1 = Text(win1, bg="white", fg="black", width=30, height="4", padx="5", pady="5")
btn = Button(win1, text="Prześlij wiadomość", command=wyslij_wiadomosc)
label2 = Label(win1, text="Wiadomość zwrotna")
entry = Entry(win1, bg="white", fg="black", width=24)

label1.pack()
textareaWin1.pack()
btn.pack()
label2.pack()
entry.pack()

win2 = Tk()
win2.title("Użytkownik 2")
win2.geometry("300x150")
label = Label(win2, text="Otrzymana wiadomość")
textareaWin2 = Text(win2, bg="white", fg="black", width="30", height="4", padx="5", pady="5")

label.pack()
textareaWin2.pack()

# tutaj dodać jakieś wskaźniki istotne dla protokołu, countery itd. np. błędów czy innych takich
# dashboardy

win3 = Tk()
win3.title("Przebieg protokołu")
win3.geometry("650x300")
textareaWin3 = Text(win3, bg="white", fg="black", width="80", height="20", padx="20", pady="10")
textareaWin3.pack()

pakiet = Pakiet()
pakiet.etykieta = 0
pakiet.bledny = FALSE
pakiet.etykietaBlad = TRUE
pakiet.klasaFEC = 0

win3.mainloop()
