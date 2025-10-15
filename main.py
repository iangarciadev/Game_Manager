from Modelos.game import game


def exibir_menu():
    print("\nMenu:")
    print("1. Adicionar jogo")
    print("2. Listar jogos")
    print("3. Dar nota a um jogo")
    print("4. Sair")

def adicionar_jogo():
        input_nome = input("Nome do jogo: ")
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
            nome_jogo = input("Digite o nome do jogo para dar uma nota: ")
            for jogo in game.jogos:
                if jogo._name.lower() == nome_jogo.lower():
                    try:
                        nota = float(input(f"Digite a nota para {jogo._name} (0-10): "))
                        if 0 <= nota <= 10:
                            print(jogo.dar_nota(nota))
                        else:
                            print("Nota deve ser entre 0 e 10.")
                    except ValueError:
                        print("Por favor, insira um número válido.")
                    break
            else:
                print("Jogo não encontrado.")
        elif escolha == '4':
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()