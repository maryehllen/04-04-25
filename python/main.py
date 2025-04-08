import json

arquivo_cadastros = "cadastros.json"

def exibi_menu():
    print("\n -----menu cadastro -----")
    print("1 - cadastrar pessoa")
    print("2 - ver cadastros")
    print("3 - sair")
    print("------------------------")

def salvar_cadastros (cadastros):
    with open (arquivo_cadastros, "w", encoding="utf-8") as arquivo:
        json.dump(cadastros, arquivo, indent=4, ensure_ascii=False)

def carregar_cadastros():
    try: 
        with open(arquivo_cadastros, "r" encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except(FileNotFoundError, json.JSONDecodeError):
        return[]
    
def cadastrar_pessoa(cadastros):
    nome = input("nome:")
    idade = input("idade:")
    turma = input("turma:")
    curso = input("curso:")
    cadastros.append({"nome": nome, "idade": idade, "turma": turma, "curso": curso})
    salvar_cadastros(cadastros)
    print("Cadastro realizado com sucesso!")

def ver_cadastros (cadastros):
    if not cadastros:
        print("\n Nenhum cadastro no sistema.")
    else:
        print("\n ------ LISTA DE CADASTROS ------")   
        for i, pessoa in enumerate (cadastros, 1)
            print(f"{i}. Nome:{pessoa['nome']}, Idade:{pessoa['idade']}, Turma: {pessoa['turma']}, Curso: {pessoa['curso']}")
            input ("\nPressione Enter para voltar ao menu...")

def main():
    cadastros = carregar_cadastros()
    while True:
        exibir_menu()
        opcao = input ("Escolha uma opção: ")
        if opcao == "1":
            cadastrar_pessoas(cadastros)
        elif opcao == "2":
            ver_cadastros(cadastros)
        elif opcao == "3":
            print ("Obrigada por utilizar o sistema de cadastro!")
            break
        else:
            print("Opção invalida! Tente novamente.")

if__name__ == "__main__":
    main()
        
