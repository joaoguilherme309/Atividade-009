from Departamento import Departamento


class Universidade:
    def __init__(self, nome, email, telefone):
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.departamentos = []

    def adicionar_departamento(self, nome, qtdprofessores):
        self.departamentos.append(Departamento(nome, qtdprofessores))
