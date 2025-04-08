import json

arquivo_cadastros = "cadastros.json"

def exibir_menu():
    print("\n ----- MENU CADASTRO -----")
    print("1 - Cadastrar pessoa")
    print("2 - Ver cadastros")
    print("3 - Sair")
    print("------------------------")

def salvar_cadastros(cadastros):
    with open(arquivo_cadastros, "w", encoding="utf-8") as arquivo:
        json.dump(cadastros, arquivo, indent=4, ensure_ascii=False)

def carregar_cadastros():
    try: 
        with open(arquivo_cadastros, "r", encoding="utf-8") as arquivo: 
            return json.load(arquivo)
    except (FileNotFoundError, json.JSONDecodeError): 
        return []
    
def cadastrar_pessoa(cadastros):
    nome = input("Nome: ")
    idade = input("Idade: ")
    turma = input("Turma: ")
    curso = input("Curso: ")
    cadastros.append({"nome": nome, "idade": idade, "turma": turma, "curso": curso})
    salvar_cadastros(cadastros)
    print("Cadastro realizado com sucesso!")

def ver_cadastros(cadastros):
    if not cadastros:
        print("\nNenhum cadastro no sistema.")
    else:
        print("\n------ LISTA DE CADASTROS ------")   
        for i, pessoa in enumerate(cadastros, 1):  
            print(f"{i}. Nome: {pessoa['nome']}, Idade: {pessoa['idade']}, Turma: {pessoa['turma']}, Curso: {pessoa['curso']}")
        input("\nPressione Enter para voltar ao menu...")  

def main():
    cadastros = carregar_cadastros()
    while True:
        exibir_menu() 
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            cadastrar_pessoa(cadastros) 
        elif opcao == "2":
            ver_cadastros(cadastros)  
        elif opcao == "3":
            print("Obrigado por utilizar o sistema de cadastro!")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":  
    main()
        
