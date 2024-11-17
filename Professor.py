class Professor:
    def __init__(self, nome):
        self.nome = nome
        self.disciplinas = []

    def adicionar_disciplina(self, disciplina):
        if len(self.disciplinas) < 5:
            self.disciplinas.append(disciplina)
        else:
            print("Não é possível adicionar mais de 5 disciplinas.")

    def __str__(self):
        disciplinas_nomes = [d.nome for d in self.disciplinas]
        return f"Professor: {self.nome}, Disciplinas: {disciplinas_nomes}"
