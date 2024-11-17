from universidade import Universidade
from departamento import Departamento
from professor import Professor
from disciplina import Disciplina


def main():
    # Criar universidade
    universidade = Universidade("Universidade Exemplo")

    # Criar departamentos
    departamento1 = Departamento("Ciências Exatas")
    departamento2 = Departamento("Ciências Humanas")

    universidade.adicionar_departamento(departamento1)
    universidade.adicionar_departamento(departamento2)

    # Criar professores
    professor1 = Professor("Prof. João")
    professor2 = Professor("Prof. Maria")

    departamento1.adicionar_professor(professor1)
    departamento2.adicionar_professor(professor2)

    # Criar disciplinas
    disciplina1 = Disciplina("Matemática")
    disciplina2 = Disciplina("História")

    professor1.adicionar_disciplina(disciplina1)
    professor2.adicionar_disciplina(disciplina2)

    # Exibir estrutura
    print(universidade)
    for departamento in universidade.departamentos:
        print(departamento)
        for professor in departamento.professores:
            print(professor)
            for disciplina in professor.disciplinas:
                print(disciplina)


if __name__ == "__main__":
    main()
