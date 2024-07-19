import tkinter as tk

class UsuarioCadastro:
    def __init__(self, root):
        # Cria o frame de cadastro
        self.frame = tk.Frame(root)
        
         # Título do Cadastro
        tk.Label(self.frame, text="Efetue aqui o seu\n Cadastro", font=("Helvetica", 16)).pack(pady=10)

        # Cria os widgets para entrada de nome, email e senha
        tk.Label(self.frame, text="Nome:").pack(pady=5)
        self.entry_nome = tk.Entry(self.frame)
        self.entry_nome.pack(pady=5)
        
        tk.Label(self.frame, text="Email:").pack(pady=5)
        self.entry_email = tk.Entry(self.frame)
        self.entry_email.pack(pady=5)
        
        tk.Label(self.frame, text="Senha:").pack(pady=5)
        self.entry_senha = tk.Entry(self.frame, show='*')
        self.entry_senha.pack(pady=5)
        
        # Botão para cadastrar
        tk.Button(self.frame, text="Cadastrar", command=self.cadastrar).pack(pady=5)
        
        # Botão para alternar para a tela de login
        tk.Button(self.frame, text="Ir para Login", command=self.switch_to_login).pack(pady=5)

    def set_controller(self, controller):
        # Associa o controlador à view
        self.controller = controller

    def get_nome(self):
        # Retorna o valor do campo nome
        return self.entry_nome.get()

    def get_email(self):
        # Retorna o valor do campo email
        return self.entry_email.get()

    def get_senha(self):
        # Retorna o valor do campo senha
        return self.entry_senha.get()

    def cadastrar(self):
        # Chama o método de cadastro no controlador
        self.controller.cadastrar()

    def switch_to_login(self):
        # Chama o método para alternar para a tela de login no controlador
        self.controller.switch_to_login()

    def show(self):
        # Exibe o frame de cadastro
        self.frame.pack()

    def hide(self):
        # Esconde o frame de cadastro
        self.frame.pack_forget()
