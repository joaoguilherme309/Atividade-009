from Universidade import Universidade
from Departamento import Departamento
from Professor import Professor
from Disciplina import Disciplina


def main():
    universidade = Universidade("UEA","uea.edu@gmail.com",929939495)


    nomeDepartamento = input("Digite o nome do departamento: ")
    quatidadeProfessores = int(input("Digite a quantidade de professores do departamento: "))
    universidade.adicionar_departamento(nomeDepartamento, quatidadeProfessores)

    departamento = universidade.departamentos[0]

    nomeProfessor = input("Digite o nome do professor: ").upper()
    idadeProfessor = int(input("Digite a idade do professor: "))
    emailProfessor = input("Digite o email do professor: ")
    telefoneProfessor = int(input("Digite o telefone do professor: "))
    professor = Professor(nomeProfessor, idadeProfessor, emailProfessor, telefoneProfessor)

    departamento.adicionar_professor(professor)

    print(departamento.professores[0])


if __name__ == "__main__":
    main()
