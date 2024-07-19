from tkinter import *
from tkinter import ttk
from math import *

# Construção da janela
window = Tk()
window.geometry('500x300')
window.title("Calculadora Média - FSA")

frame = ttk.Frame(window, padding=20)
frame.grid()

# Criação de campos de inserção de nota e resultado da média aritmética
nota_at = ttk.Entry(frame)
nota_at.grid(column=1, row=0)

label_at = ttk.Label(frame, text="Digite a nota de atividade:")
label_at.grid(column=0, row=0)

nota_p1 = ttk.Entry(frame)
nota_p1.grid(column=1, row=1,pady=20)

label_p1 = ttk.Label(frame, text="Digite a nota da P1:")
label_p1.grid(column=0, row=1)

nota_p2 = ttk.Entry(frame)
nota_p2.grid(column=1, row=2)

label_p2 = ttk.Label(frame, text="Digite a nota da P2:")
label_p2.grid(column=0, row=2)

def media_geral():
    n1 = nota_p1.get()
    n2 = nota_p2.get()
    at = nota_at.get()
    total_prova = float(n1) + float(n2)
    media_prova = ((total_prova / 2) * 0.8)
    media_at = float(at) * 0.2
    mg = media_at + media_prova
    blank.delete(0, END)
    blank.insert(0, mg)



Button(frame, text="Calcular", command=media_geral).grid(column=1, row=4, sticky=W)

label_result = ttk.Label(frame, text="Sua média foi:")
label_result.grid(column=0, row=3, pady=15)

blank = ttk.Entry(frame)
blank.grid(column=1, row=3)

window.mainloop()