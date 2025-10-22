from Modelos.game import game


teste = game.abrir_arquivo()
input_nome = input("Nome do jogo: ").capitalize()
if any(jogo['nome'] == input_nome for jogo in teste):
    print(f"O jogo {input_nome} já está cadastrado.")
else:
    input_genero = input("Gênero do jogo: ")
    input_plataforma = input("Plataforma do jogo: ")
    novo_jogo = game(input_nome, input_genero, input_plataforma)
    print(f'Jogo {novo_jogo._name} adicionado com sucesso!')




