import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


def adicionar_ao_carrinho(produto):
    print(f"{produto} adicionado ao carrinho!")


def criar_janela():
    janela = tk.Tk()
    janela.title("Loja de Camisetas de Rock")


    janela.columnconfigure(0, weight=1)
    janela.columnconfigure(1, weight=1)
    janela.columnconfigure(2, weight=1)

  
    produtos = [
        ("Camiseta Banda 1", "camiseta1.jpg", "R$ 50,00"),
        ("Camiseta Banda 2", "camiseta2.jpg", "R$ 60,00"),
        ("Camiseta Banda 3", "camiseta3.jpg", "R$ 70,00"),
        ("Camiseta Banda 4", "camiseta4.jpg", "R$ 70,00"),
        ("Camiseta Banda 5", "camiseta5.jpg", "R$ 70,00"),
        ("Camiseta Banda 6", "camiseta6.jpg", "R$ 70,00")
    ]

  
    for i, (nome, imagem, preco) in enumerate(produtos):
        frame = ttk.Frame(janela)
        frame.grid(row=i//3, column=i%3, padx=10, pady=10, sticky="nsew")

        
        img = Image.open(imagem)
        img = img.resize((150, 150), Image.ANTIALIAS)
        img_tk = ImageTk.PhotoImage(img)

        label_img = ttk.Label(frame, image=img_tk)
        label_img.image = img_tk 
        label_img.grid(row=0, column=0, columnspan=2)

        label_nome = ttk.Label(frame, text=nome)
        label_nome.grid(row=1, column=0, columnspan=2)

        label_preco = ttk.Label(frame, text=preco)
        label_preco.grid(row=2, column=0, columnspan=2)

        btn_adicionar = ttk.Button(frame, text="Adicionar ao Carrinho", command=lambda n=nome: adicionar_ao_carrinho(n))
        btn_adicionar.grid(row=3, column=0, columnspan=2, pady=5)

    janela.mainloop()
criar_janela()
