from typing import Type
from Professor import Professor


class Departamento:

    def __init__(self, nome, qtdprofessores):
        self.nomeDepartamento = nome
        self.quatidadeProfessores = qtdprofessores
        self.professores = []

    def adicionar_professor(self, professor: Type[Professor]):
        self.professores.append(professor)

    def listar_professores(self):
        for professor in self.professores:
            professor.lista_professores()
            professor.get_disciplina()