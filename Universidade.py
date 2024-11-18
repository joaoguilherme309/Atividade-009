from Departamento import Departamento


class Universidade:
    def __init__(self, nome, email, telefone):
        self.__nome = nome
        self.__email = email
        self.__telefone = telefone
        self.departamentos = []

    def adicionar_departamento(self, nome, qtdprofessores):
        self.departamentos.append(Departamento(nome, qtdprofessores))

    def listar_departamentos(self):
        for departamento in self.departamentos:
            print(f"Departamento: {departamento.nomeDepartamento}, Professores: {departamento.quatidadeProfessores}")