import os

restaurantes = [{"nome":"Tutti Pizza", "categoria":"Pizza", "ativo": False},
                {"nome":"Farinha e Fogo", "categoria":"Massa", "ativo": True},
                {"nome":"Sushi House", "categoria":"Japonesa", "ativo": True}]

def voltar_ao_menu_principal():
    input("\nDigite uma tecla para voltar para o menu princial ")
    main()

def opcao_invalida():
    print("Opção inválida.")
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    os.system('cls')
    print(texto)

def nome_programa():
    print("Sabor Express\n")

def opcoes():
    print("1. Cadastrar restaurante")
    print("2. Listar restaurante")
    print("3. Ativar restaurante")
    print("4. Sair\n")

def cadastrar_restaurante():
    exibir_subtitulo("Cadastrar restaurante")

    nome_restaurante = input("Digite o nome do restaurante que você deseja cadastrar: ")
    categoria = input(f"Digite a categoria do restaurante {nome_restaurante}: ")
    dados_restaurante = {"nome":nome_restaurante, "categoria":categoria, "ativo":False}
    restaurantes.append(dados_restaurante)
    
    #restaurantes.append(nome_restaurante)
    print(f"Restaurante {nome_restaurante} cadastrado com sucesso!")
    
    voltar_ao_menu_principal()

def listar_restaurantes():
    exibir_subtitulo("Lista de restaurantes:\n")
    
    for restaurante in restaurantes:    
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = restaurante['ativo']
        #print(f"- {nome_restaurante}")
        print(f"- {nome_restaurante} | {categoria} | {ativo}")

    voltar_ao_menu_principal()

def encerrar():
    os.system('cls')
    print("Encerrando o programa")


def escolher_opcao():
    try:
        numero_menu = int(input("Digite o número da operação que gostaria de realizar: "))
        #print("Você escolheu a opção", numero_menu)
        print(f"Você escolheu a opção {numero_menu}\n")

        if numero_menu == 1:
            cadastrar_restaurante()
        elif numero_menu == 2:
            listar_restaurantes()
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