from tkinter import *
tela = Tk()

txt_nome = Entry(tela, width=50, fg="black", bg="#133753", borderwidth=5)
txt_nome.pack()
txt_nome.insert(0, "Digite seu nome")

def clicar():
    lbl_nome = Label(tela, text="Bem Venidos Filha Duma Puta " + txt_nome.get())
    lbl_nome.pack()



btn_botao = Button(tela, text="Clique", command=clicar)
btn_botao.pack()

tela.mainloop()