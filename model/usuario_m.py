import sqlite3

class UsuarioModel:
    def __init__(self):
        # Conecta ao banco de dados SQLite e cria a tabela de usuários se não existir
        self.conn = sqlite3.connect('marcio_db')
        self.conn.execute('''CREATE TABLE IF NOT EXISTS users
                             (id INTEGER PRIMARY KEY, nome TEXT, email TEXT UNIQUE, senha TEXT)''')
        self.conn.commit()

    def add_user(self, nome, email, senha):
        # Adiciona um novo usuário ao banco de dados
        try:
            self.conn.execute('INSERT INTO users (nome, email, senha) VALUES (?, ?, ?)', (nome, email, senha))
            self.conn.commit()
            return True
        except sqlite3.IntegrityError:
            # Retorna False se o email já estiver cadastrado
            return False

    def check_login(self, email, senha):
        # Verifica se as credenciais de login estão corretas
        cursor = self.conn.execute('SELECT * FROM users WHERE email=? AND senha=?', (email, senha))
        return cursor.fetchone() is not None
