from tkinter import *
tela = Tk()

tela.title("Check Button")
tela.configure(background='#1e3743')
tela.geometry("300x300")

def show():
    Label(tela, text=var.get()).pack()

var = StringVar

chk_button = Checkbutton(tela, text="check box", variable=var, onvalue="On", offvalue="Off")
chk_button.deselect()
chk_button.pack()

Button(tela, text="Show me", command=show).pack()

tela.mainloop()