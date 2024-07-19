import tkinter as tk
from view.usuario_cadastro import UsuarioCadastro
from view.usuario_login import UsuarioLogin
from controller.usuario_c import UsuarioController

def main():
    # Cria a janela principal do Tkinter
    root = tk.Tk()
    root.title("Tela Incial")
    root.geometry("300x300")

    # Inicializa as views de cadastro e login
    view_cadastro = UsuarioCadastro(root)
    view_login = UsuarioLogin(root)

    # Inicializa o controlador
    controller_usuario_c = UsuarioController(view_cadastro, view_login)

    # Exibe a tela de cadastro por padrão
    view_cadastro.show()

    # Inicia o loop principal do Tkinter
    root.mainloop()

if __name__ == "__main__":
    main()
