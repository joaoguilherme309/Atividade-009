from Departamento import Departamento


class Professor:
    def __init__(self, nome, idade, email, telefone):
        self.nome = nome
        self.idade = idade
        self.email = email
        self.telefone = telefone

    def __str__(self) :
        return f"Professor(nome={self.nome}, idade={self.idade}, email={self.email}, telefone={self.telefone})"

departamento = Departamento("Biologia", 10)

nomeProfessor = input("Digite o nome do professor: ").upper()
idadeProfessor = int(input("Digite a idade do professor: "))
emailProfessor = input("Digite o email do professor: ")
telefoneProfessor = int(input("Digite o telefone do professor: "))

professor = Professor(nomeProfessor, idadeProfessor, emailProfessor, telefoneProfessor)

departamento.adicionar_professor(professor)

print(departamento.professores[0])





