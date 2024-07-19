import tkinter as tk

class UsuarioLogin:
    def __init__(self, root):
        # frame de login
        self.frame = tk.Frame(root)

        # Título do Cadastro
        tk.Label(self.frame, text="Faça seu Login", font=("Helvetica", 16)).pack(pady=10)
        
        # Cria entrada de email e senha
        tk.Label(self.frame, text="Email:").pack(pady=5)
        self.entry_email_login = tk.Entry(self.frame)
        self.entry_email_login.pack(pady=5)
        
        tk.Label(self.frame, text="Senha:").pack(pady=5)
        self.entry_senha_login = tk.Entry(self.frame, show='*')
        self.entry_senha_login.pack(pady=5)
        
        # Botão login
        tk.Button(self.frame, text="Login", command=self.login).pack(pady=5)
        
        # Botão mudar a tela de cadastro
        tk.Button(self.frame, text="Ir para Cadastro", command=self.switch_to_cadastro).pack(pady=5)

    def set_controller(self, controller):
        # controlador a view
        self.controller = controller

    def get_email(self):
        # Retorna o valor do campo email
        return self.entry_email_login.get()

    def get_senha(self):
        # Retorna o valor do campo senha
        return self.entry_senha_login.get()

    def login(self):
        # Chama o método de login no controlador
        self.controller.login()

    def switch_to_cadastro(self):
        # Chama o método para alternar para a tela de cadastro no controlador
        self.controller.switch_to_cadastro()

    def show(self):
        # Exibe o frame de login
        self.frame.pack()

    def hide(self):
        # Esconde o frame de login
        self.frame.pack_forget()
