import os

def opcao_invalida():
    print("Opção inválida.")
    input("Digite uma tecla para voltar para o menu princial ")
    main()

def nome_programa():
    print("Sabor Express\n")

def opcoes():
    print("1. Cadastrar restaurante")
    print("2. Listar restaurante")
    print("3. Ativar restaurante")
    print("4. Sair\n")

def encerrar():
    os.system('cls')
    print("Encerrando o programa")


def escolher_opcao():
    try:
        numero_menu = int(input("Digite o número da operação que gostaria de realizar: "))
        #print("Você escolheu a opção", numero_menu)
        print(f"Você escolheu a opção {numero_menu}\n")

        if numero_menu == 1:
            print("Cadastrar restaurante")
        elif numero_menu == 2:
            print("Listar restaurantes")
        elif numero_menu == 3:
            print("Ativar restaurante")
        elif numero_menu == 4:
            encerrar()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    os.system('cls')
    nome_programa()
    opcoes()
    escolher_opcao()

if __name__ == "__main__":
    main()