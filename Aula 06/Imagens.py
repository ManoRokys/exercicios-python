from tkinter import filedialog
from tkinter import *
from PIL import Image, ImageTk
tela = Tk()
pasta_inicial=""

def escolher_imagem():

    caminho_imagem = filedialog.askopenfilename(initialdir=pasta_inicial, title="Escolha uma imagem", filetypes=(("Arquivos de imagem", "*.jpg;*.jpeg;*.png"),("Todos os arquivos", "*.*")))

    imagem_pil = Image.open(caminho_imagem) 
    largura, altura = imagem_pil.size
    if largura > 150:
        proporcao = largura / 150
        nova_altura = int(altura / proporcao)
        imagem_pil = imagem_pil.resize((110, nova_altura))

    imagem_tk = ImageTk.PhotoImage(imagem_pil)
    lbl_imagem = Label(tela, image=imagem_tk)
    lbl_imagem.image = imagem_tk
    lbl_imagem.place(x=10, y=50)

btn_escolher = Button(tela, text="Escolher imagem", command=escolher_imagem)
btn_escolher.place(x=10, y=140)

tela.mainloop()