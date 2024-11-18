class Departamento:
    def __init__(self, nome, qtdprofessores):
        self.nomeDepartamento = nome
        self.quatidadeProfessores = qtdprofessores
        self.professores = []

    def adicionar_professor(self, professor):
        self.professores.append(professor)