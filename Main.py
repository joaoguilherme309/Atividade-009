from Universidade import Universidade
from Professor import Professor


def main():
    metodo = input("Digite o que você quer deletar: ")

    if metodo == "nada" or metodo != "universidade":
        universidade = Universidade("UEA","uea.edu@gmail.com",929939495)
    elif metodo == "universidade":
        try:
            universidade.motrar_universidade()
        except:
            print("Universidade foi removida")
            pass

    if metodo == "nada" or metodo != "departamento" :
        nomeDepartamento = input("Digite o nome do departamento: ")
        quatidadeProfessores = int(input("Digite a quantidade de professores do departamento: "))
        universidade.adicionar_departamento(nomeDepartamento, quatidadeProfessores)
        departamento = universidade.departamentos[0]
    elif metodo == "departamento":
        try:
            print(departamento.nomeDepartamento)
        except:
            print("Departamento foi removido")
            pass

    if metodo == "nada" or metodo != "professor":
        nomeProfessor = input("Digite o nome do professor: ").upper()
        idadeProfessor = int(input("Digite a idade do professor: "))
        emailProfessor = input("Digite o email do professor: ")
        telefoneProfessor = int(input("Digite o telefone do professor: "))
        professor = Professor(nomeProfessor, idadeProfessor, emailProfessor, telefoneProfessor)
        professor.set_disciplina(input("Digite o nome da disciplina ministrada: "))
        if metodo != "departamento":
            departamento.adicionar_professor(professor)
        elif metodo == "departamento":
            professor.lista_professores()
    elif metodo == "professor":
        try:
            professor.lista_professores()
        except:
            print("Professor foi removido")
            pass

    universidade.motrar_universidade()
    if metodo != "departamento":
        departamento.listar_professores()
    universidade.listar_departamentos()

if __name__ == "__main__":
    main()
