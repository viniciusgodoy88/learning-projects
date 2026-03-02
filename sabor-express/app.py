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
    """Exibe as opções disponíveis no menu principal """
    print("1. Cadastrar restaurante")
    print("2. Listar restaurantes")
    print("3. Alternar estado do restaurante")
    print("4. Sair\n")

def exibir_subtitulo(texto):
    """
    Exibe um subtítulo estilizado na tela 
    
    Inputs:
    - texto: str - O texto do subtítulo
    
    """
    os.system('cls')
    linha = "*" * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print ()
    
    
def cadastrar_restaurante():
    """
    Essa função é responsavel por cadastrar por um novo restaurante 
    
    Inputs: 
    - Nome do restaurante
    - Categoria
    
    Outputs: 
    - Adiciona um novo restaurante a lista de restaurantes
    """
    exibir_subtitulo("Cadastro de novos restaurantes\n")
    nome_restaurante = input("Digite o nome do restaurante que deseja cadastrar: ")
    categoria = input(f" Digite o nome da categoria do restaurante: {nome_restaurante}:")
    dados_restaurante = {"nome": nome_restaurante, "categoria":categoria, "ativo":False}    
    restaurantes.append(dados_restaurante)
    print(f"O restaurante {nome_restaurante} foi cadastrado com sucesso!")
    voltar_menu_principal()

def listar_restaurante():
    """
    Lista os restaurantes presentes na lista 
    
    Outputs:
    - Exibe a lista de restaurantes na tela
    """
    
    
    exibir_subtitulo("Listagem dos restaurantes\n")

    print(f'{'Nome do restaurante'.ljust(23)} | {'Categoria'.ljust(20)} | Status')    
    
    for restaurante in restaurantes:
        nome_restaurante = restaurante["nome"]
        categoria = restaurante["categoria"]
        #ternário = condicional em uma linha
        ativo = "ativado" if restaurante["ativo"] else "desativado"
        print(f" - {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}")

    voltar_menu_principal()

def finalizar_app():
    """Exibe mensagem de finalização do aplicativo """
    exibir_subtitulo("Finalizando o programa...\n")

def voltar_menu_principal():
    """
    Solicita uma tecla para voltar ao menu principal 
    
    Outputs:
    - Retorna ao menu principal
    """
    input("Digite uma tecla para voltar ao menu principal...")
    main()    

def opcao_invalida():
    """
    Exibe mensagem de opção inválida e retorna ao menu principal 
    
    Outputs:
    - Retorna ao menu principal
    
    """
    exibir_subtitulo("Opção inválida!\n")
    voltar_menu_principal()

def alternar_estado_restaurante():
    """
    Altera o estado ativo/desativado de um restaurante 
    
    Outputs:
    - Exibe mensagem indicando o sucesso da operação
    
    """
    
    exibir_subtitulo("Alternando estado do restaurante")
    nome_restaurante = input("Digite o nome do restaurante que deseja alternar o estado: ")
    restaurante_encontrado = False
    
    for restaurante in restaurantes: 
        if nome_restaurante == restaurante["nome"]:
            restaurante_encontrado = True
            restaurante["ativo"] = not restaurante ["ativo"]
            mensagem = f"O restaurante {nome_restaurante} foi ativado com sucesso " if restaurante["ativo"]else f"O restaurante foi desativado com sucesso"
            print(mensagem)
    
    if not restaurante_encontrado: 
        print("O restaurante não foi encontrado !")    
    voltar_menu_principal()

def escolher_opcoes():
    """
    Solicita e executa a opção escolhida pelo usuário 
    
    Outputs:
    - Executa a opção escolhida pelo usuário
    """
    
    try:
        opcao_escolhida = int(input("Escolha uma opção: "))

        if opcao_escolhida == 1:
            cadastrar_restaurante()

        elif opcao_escolhida == 2:
            listar_restaurante()

        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
            voltar_menu_principal()

        elif opcao_escolhida == 4:
            finalizar_app()

        else:
            opcao_invalida()

    except:
        opcao_invalida()


def main():
    """
    Função principal que inicia o programa
    """
    os.system('cls')
    exibir_nome_programa()
    exibir_opcoes()
    escolher_opcoes()
    voltar_menu_principal()
    exibir_subtitulo()

if __name__ == "__main__":
    main()