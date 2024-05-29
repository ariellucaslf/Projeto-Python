from tkinter import *
from tkinter import Tk, ttk

# cores ----------------------------------------
cor1 = "#141111" # preto
cor2 = "#feffff" # branco
cor3 = "#249c89" # verde
cor4 = "#38576b" # azul escuro (valor)
cor5 = "#403d3d" # cinza (letra)

# criando a janela ------------------------------
janela = Tk()
janela.title("")
janela.geometry("310x300")
janela.configure(background=cor2)
janela.resizable(width=FALSE, height=FALSE)

# divisao da janela ------------------------------
frame_cima = Frame(janela, width=310, height=50, bg=cor2, relief="flat")
frame_cima.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)

frame_baixo = Frame(janela, width=310, height=250, bg=cor2, relief="flat")
frame_baixo.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

# configurando o frame cima ----------------------
l_nome = Label(frame_cima, text="LOGIN", anchor=NE, font=("Ivy 25"), bg=cor1, fg=cor4)
l_nome.place(x=5, y=5)

l_linha = Label(frame_cima, text="",  width=275, anchor=NW, font=("Ivy 1"), bg=cor2, fg=cor4)
l_linha.place(x=10, y=45)

# configurando o frame baixo ---------------------
# Usuario
l_nome = Label(frame_baixo, text="Usuario *", anchor=NW, font=("Ivy 10"), bg=cor1, fg=cor4)
l_nome.place = Label(x=10, y=20)
e_nome = Entry(frame_baixo, width=25, justify="left", font=("", 15), highlightthickness=1, relief="solid")
e_nome.place(x=14, y=50)

#Senha
l_senha = Label(frame_baixo, text="Senha *", anchor=NW, font=("Ivy 10"), bg=cor1, fg=cor4)
l_senha.place = Label(x=10, y=95)
e_senha = Entry(frame_baixo, width=25, justify="left", font=("", 15), highlightthickness=1, relief="solid")
e_senha.place(x=14, y=130)

janela.mainloop()