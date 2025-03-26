from tkinter import *

tela = Tk()

tela.title("Fatec de Registro")
tela.configure(background='#FD01D3')
tela.geometry("780x600")
tela.resizable(True, True)
tela.maxsize(width=760, height=680)
tela.minsize(width=300, height=200)

lbl_nome = Label(tela, text="Waifu").place (x=10,y=10)
lbl_nome = Label(tela, text="Waifu2").place (x=10,y=40)
lbl_nome = Label(tela, text="Waifu3").place (x=10,y=70)
lbl_nome = Label(tela, text="Waifu4").place (x=10,y=100)

btn = Button(tela, text="Cadastrar")
btn.pack()


tela.mainloop()
