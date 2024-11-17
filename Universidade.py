class Universidade:
    def __init__(self, nome):
        self.nome = nome
        self.departamentos = []

    def adicionar_departamento(self, departamento):
        if len(self.departamentos) < 5:
            self.departamentos.append(departamento)
        else:
            print("Não é possível adicionar mais de 5 departamentos.")

    def __str__(self):
        departamentos_nomes = [d.nome for d in self.departamentos]
        return f"Universidade: {self.nome}, Departamentos: {departamentos_nomes}"

