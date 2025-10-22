from Modelos.game import game


def exibir_menu():
    print("\nMenu:")
    print("1. Adicionar jogo")
    print("2. Listar jogos")
    print("3. Dar nota a um jogo")
    print("4. Buscar jogo")
    print("5. Deletar jogo")
    print("6. Sair")

def adicionar_jogo():
    input_nome = input("Nome do jogo: ")
    if any(jogo['nome'] == input_nome for jogo in game.abrir_arquivo()):
        print(f"O jogo {input_nome} já está cadastrado.")
    else:
        input_genero = input("Gênero do jogo: ")
        input_plataforma = input("Plataforma do jogo: ")
        novo_jogo = game(input_nome, input_genero, input_plataforma)
        print(f'Jogo {novo_jogo._name} adicionado com sucesso!')

def main():
    while True:
        exibir_menu()
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            adicionar_jogo()
        elif escolha == '2':
            game.listar_jogos()
        elif escolha == '3':
            game.dar_nota()
        elif escolha == '4':
            input_nome = input("Nome do jogo que deseja buscar: ")
            resultado = game.buscar_jogo(input_nome)
            print(resultado)
        elif escolha == '5':
            input_nome = input("Nome do jogo que deseja deletar: ")
            resultado = game.deletar_jogo(input_nome)
            print(resultado)
        elif escolha == '6':
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()