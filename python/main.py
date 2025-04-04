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
