def exibir_menu():
    print("Bem vido menu de cadastro da clinica")
    print("1 - Cadastrar")
    print("2 - Ver Cadastro")
    print("3 - Sair")
    print("------------------------")

def cadastrar_pessoas (cadastros):
    name = input("Nome:")
    idade = input("Idade:")
    doença = input("Doença mental:")
    tratamento = input("Tratamento:")
    cadastros.append({"Nome": name, "Idade": idade, "Doença mental": doença, "Tratamento": tratamento})
    print("Cadastro realizado, espere por sua busca.")




def ver_cadastros (cadastros):
    if not cadastros: 
        print("Não foi achado seu cadastro.")
    else:
        print("\n ------ LISTA DE CADASTROS -----")

        for i, pessoa in enumerate (cadastros, 1):
            print(f"{i}. Nome: {pessoa['name']}, idade: {pessoa['idade']}, Doença mental: {pessoa['doença']}, Tratamento: {pessoa['tratamento']}")
 
 
 
def main():
    cadastros = []
    while True :
        exibir_menu()
        opção = input("escolha uma opção:")
        if opção == "1":
            cadastrar_pessoas (cadastros)
        elif opção == "2":
            ver_cadastros (cadastros)
        elif opção ==3:
            print("Obrigado, por se tratar ;D") 
            break
    else:
        print("Opção incorreta! Tente novamente!")

if __name__ == "__main__": 
    main()
            


