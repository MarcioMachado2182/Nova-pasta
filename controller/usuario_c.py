from tkinter import messagebox
from model.usuario_m import UsuarioModel



class UsuarioController:
    def __init__(self, cadastro_view, login_view):
        # Inicializa o modelo e as views
        self.model = UsuarioModel()
        self.cadastro_view = cadastro_view
        self.login_view = login_view
        self.cadastro_view.set_controller(self)
        self.login_view.set_controller(self)

    def cadastrar(self):
        # Obtém os dados de cadastro da view e tenta cadastrar o usuário
        nome = self.cadastro_view.get_nome()
        email = self.cadastro_view.get_email()
        senha = self.cadastro_view.get_senha()
        if nome and email and senha:
            if self.model.add_user(nome, email, senha):
                messagebox.showinfo("Sucesso", "Cadastro realizado com sucesso!")
            else:
                messagebox.showwarning("Erro", "Email já cadastrado!")
        else:
            messagebox.showwarning("Erro", "Todos os campos são obrigatórios!")

    def login(self):
        # Obtém os dados de login da view e tenta realizar o login
        email = self.login_view.get_email()
        senha = self.login_view.get_senha()
        if self.model.check_login(email, senha):
            messagebox.showinfo("Sucesso", "Login realizado com sucesso!")
        else:
            messagebox.showerror("Erro", "Email ou senha incorretos!")

    def switch_to_login(self):
        # Alterna para a tela de login
        self.cadastro_view.hide()
        self.login_view.show()

    def switch_to_cadastro(self):
        # Alterna para a tela de cadastro
        self.login_view.hide()
        self.cadastro_view.show()
