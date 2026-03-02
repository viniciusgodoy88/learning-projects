import os

# Lista para armazenar os nomes dos restaurantes cadastrados
restaurantes = [{'nome':'Praça', 'categoria':'Japonesa', 'ativo':False}, 
                {'nome':'Pizza Suprema', 'categoria':'Pizza', 'ativo':True},
                {'nome':'Cantina', 'categoria':'Italiano', 'ativo':False}]


def exibir_nome_programa():
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗
╚█████╗░███████║██████╦╝██║░░██║██████╔╝
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝

███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
█████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝
""")


def exibir_opcoes():
    print("1. Cadastrar restaurante")
    print("2. Listar restaurantes")
    print("3. Ativar restaurante")
    print("4. Sair\n")

def exibir_subtitulo(texto):
    os.system('cls')
    print(texto)
    
def cadastrar_restaurante():
    exibir_subtitulo("Cadastro de novos restaurantes\n")

    nome_restaurante = input("Digite o nome do restaurante que deseja cadastrar: ")
    restaurantes.append(nome_restaurante)

    print(f"O restaurante {nome_restaurante} foi cadastrado com sucesso!")
    voltar_menu_principal()

def listar_restaurante():
    
    exibir_subtitulo("Listagem dos restaurantes\n")

    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = restaurante['ativo']
    print(f' - {nome_restaurante} | {categoria} | {ativo}')

    
    voltar_menu_principal()

def finalizar_app():
    
    exibir_subtitulo("Finalizando o programa...\n")

def voltar_menu_principal():
    input("Digite uma tecla para voltar ao menu principal...")
    main()    

def opcao_invalida():
    exibir_subtitulo("Opção inválida!\n")
    voltar_menu_principal()


def escolher_opcoes():
    try:
        opcao_escolhida = int(input("Escolha uma opção: "))

        if opcao_escolhida == 1:
            cadastrar_restaurante()

        elif opcao_escolhida == 2:
            listar_restaurante()

        elif opcao_escolhida == 3:
            print("Ativar restaurante")
            voltar_menu_principal()

        elif opcao_escolhida == 4:
            finalizar_app()

        else:
            opcao_invalida()

    except:
        opcao_invalida()


def main():
    os.system('cls')
    exibir_nome_programa()
    exibir_opcoes()
    escolher_opcoes()
    voltar_menu_principal()
    exibir_subtitulo()

if __name__ == "__main__":
    main()