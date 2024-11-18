from Departamento import Departamento


class Universidade:
    def __init__(self, nome, email, telefone):
        self.__nome = nome
        self.__email = email
        self.__telefone = telefone
        self.departamentos = []

    def motrar_universidade(self):
        print(f"Nome da Universidade: {self.__nome}, Email: {self.__email}, Telefone: {self.__telefone}")

    def adicionar_departamento(self, nome, qtdprofessores):
        self.departamentos.append(Departamento(nome, qtdprofessores))

    def listar_departamentos(self):
        for departamento in self.departamentos:
            print(f"Departamento: {departamento.nomeDepartamento}, Professores: {departamento.quatidadeProfessores}")

    def remover_departamento(self):
        self.departamentos.clear()