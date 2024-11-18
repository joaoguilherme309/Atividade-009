
class Professor:
    def __init__(self, nome, idade, email, telefone):
        self.__nome = nome
        self.__idade = idade
        self.__email = email
        self.__telefone = telefone
        self.disciplina = None

    def lista_professores(self):
        print(f"Professor(nome={self.__nome}, idade={self.__idade}, email={self.__email}, telefone={self.__telefone})")

    def set_disciplina(self, disciplina ):
        self.disciplina = disciplina

    def get_disciplina(self):
        return self.disciplina, print(f"Disciplina ministrada:{self.disciplina}")