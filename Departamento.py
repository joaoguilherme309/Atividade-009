class Departamento:
    def __init__(self, nome):
        self.nome = nome
        self.professores = []

    def adicionar_professor(self, professor):
        if len(self.professores) < 5:
            self.professores.append(professor)
        else:
            print("Não é possível adicionar mais de 5 professores.")

    def __str__(self):
        professores_nomes = [p.nome for p in self.professores]
        return f"Departamento: {self.nome}, Professores: {professores_nomes}"
