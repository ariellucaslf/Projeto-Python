from tkinter import *
from tkinter import Tk, ttk
from tkinter import messagebox 

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


credenciais = ['joao' , '123456789']

#função para verificar senha 
def verifica_senha():
    nome = e_nome.get()
    senha = e_senha.get()

    if nome =='admin' and senha =='admin':
     messagebox.showinfo ('login' ,'seja bem vindo admin !!!')
    elif credenciais[0] == nome and credenciais[1]==senha:
         messagebox.showinfo ('login' ,'seja bem vindo de volta '+credenciais[0])

            #deletar itens presentes no frame baixo e cime
         for widget in frame_baixo.winfo_children():
            widget.destroy() 

         for widget in frame_cima.winfo_children():
            widget.destroy()

         nova_janela()



    else:
     messagebox.showwarning( 'erro' ,'verifique o nome e a senha!')


#função apos verificação
def nova_janela():
    # configurando o frame cima ----------------------
    l_nome = Label(frame_cima, text="usuario :" + credenciais[0], anchor=NE, font=("Ivy 20"), bg=cor1, fg=cor4)
    l_nome.place(x=5, y=5)

    l_linha = Label(frame_cima, text="",  width=275, anchor=NW, font=("Ivy 1"), bg=cor2, fg=cor4)
    l_linha.place(x=10, y=45)

    l_nome = Label(frame_baixo, text="seja bem vindo" + credenciais[0], anchor=NE, font=("Ivy 20"), bg=cor1, fg=cor4)
    l_nome.place(x=5, y=105)

# configurando o frame baixo ---------------------
# Usuario
l_nome = Label(frame_baixo, text="Usuario *", anchor=NW, font=("Ivy 10"), bg=cor1, fg=cor4)
l_nome.place(x=10, y=20)
e_nome = Entry(frame_baixo, width=25, justify="left", font=("", 15), highlightthickness=1, relief="solid")
e_nome.place(x=14, y=50) 

# Senha
l_senha = Label(frame_baixo, text="Senha *", anchor=NW, font=("Ivy 10"), bg=cor1, fg=cor4)
l_senha.place(x=10, y=95)
e_senha = Entry(frame_baixo, width=25, justify="left", show='*', font=("", 15), highlightthickness=1, relief="solid")
e_senha.place(x=14, y=130)

# Botão
b_confirmar = Button(frame_baixo, command=verifica_senha, text="Entrar", width=39, height=2, font=("Ivy 8 bold"), bg=cor2, fg=cor1, relief=RAISED, overrelief=RIDGE)
b_confirmar.place(x=15, y=180)

janela.mainloop()