from tkinter import *
from tkinter import ttk

## cores utilizadas ## 
co0 = "#444466"  # Preta
co1 = "#feffff"  # branca
co2 = "#6f9fbd"  # azul
co3 = "#38576b"  # valor
co4 = "#403d3d"   # letra
co5 = "#ef5350"   # vermelha

janela = Tk()
janela.title('')
janela.geometry('550x510')
janela.configure(bg=co1)

ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columspan=1, ipadx=272)

style = ttk.Style(janela)
style.theme_use("clam")

janela.mainloop()