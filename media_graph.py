from tkinter import *
from tkinter import ttk
from tkinter import PhotoImage
from math import *

# Construção da janela
window = Tk()
window.geometry('600x300')
window.title("Calculadora - Média FSA")

frame = ttk.Frame(window, padding=20)
frame.grid()

# Adicionar logo da FSA
image = PhotoImage(file="img/fsa.png")
image_label = ttk.Label(frame, image=image)
image_label.grid(column=3, row=0, rowspan=5, padx=40)

# Criação de campos de inserção de nota e resultado da média aritmética
nota_at = ttk.Entry(frame)
nota_at.grid(column=2, row=0)

label_at = ttk.Label(frame, text="Digite a nota de atividade:")
label_at.grid(column=1, row=0)

nota_p1 = ttk.Entry(frame)
nota_p1.grid(column=2, row=1,pady=20)

label_p1 = ttk.Label(frame, text="Digite a nota da P1:")
label_p1.grid(column=1, row=1)

nota_p2 = ttk.Entry(frame)
nota_p2.grid(column=2, row=2)

label_p2 = ttk.Label(frame, text="Digite a nota da P2:")
label_p2.grid(column=1, row=2)

nota_p3 = ttk.Entry(frame)
nota_p3.grid(column=2, row=3, pady=20)

label_p3 = ttk.Label(frame, text="Digite a nota da P3:")
label_p3.grid(column=1, row=3)

def media_geral():
    """Função para realizar o cálculo de média aritmética"""
    try:
        n1 = float(nota_p1.get())
        n2 = float(nota_p2.get())
        at = float(nota_at.get())
    except ValueError:
        blank.delete(0, END)
        blank.insert(0, "Valor inválido")
        return

    total_prova = n1 + n2
    media_prova = ((total_prova / 2) * 0.8)
    media_at = at * 0.2
    mg = media_at + media_prova
    
    if nota_p3.get() == "":
        blank.delete(0, END)
        blank.insert(0, f"{mg:.2f}")
    else:
        try:
            n3 = float(nota_p3.get())
            total_final = (n3 + mg)
            mf = (total_final / 2)
            blank.delete(0, END)
            blank.insert(0, f"{mf:.2f}")
        except ValueError:
            blank.delete(0, END)
            blank.insert(0, "Valor inválido")

Button(frame, text="Calcular", command=media_geral, width=15).grid(column=2, row=5, sticky=W, pady=10)

label_result = ttk.Label(frame, text="Sua média foi:")
label_result.grid(column=1, row=4)

blank = ttk.Entry(frame)
blank.grid(column=2, row=4)

window.mainloop()
