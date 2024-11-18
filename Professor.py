
class Professor:
    def __init__(self, nome, idade, email, telefone):
        self.nome = nome
        self.idade = idade
        self.email = email
        self.telefone = telefone

    def __str__(self) :
        return f"Professor(nome={self.nome}, idade={self.idade}, email={self.email}, telefone={self.telefone})"






