class Disciplina:
    def __init__(self, nome):
        self.__nome = nome
        self.professor = None

    def __str__(self):
        return f"Disciplina: {self.nome}"

    def set_professor(self, professor):
        self.professor = professor

    def get_professor(self):
        return self.professor
