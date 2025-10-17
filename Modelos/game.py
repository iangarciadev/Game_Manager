class game:

    jogos = []

    def __init__(self, name, genre, platform):
        self._name = name.title()
        self._genre = genre
        self._platform = platform
        game.jogos.append(self)
    
    def __str__(self):
        if hasattr(self, 'nota'):
            return f"{self._name} - {self._genre} - {self._platform} - Nota: {self.nota}"
        else:
            return f"{self._name} - {self._genre} - {self._platform}"
    
    def dar_nota(self, nota):
        self.nota = nota
        return f"A nota de {self._name} é {self.nota}"
    
    @classmethod
    def listar_jogos(cls):
        for jogo in cls.jogos:
            print(jogo)
    
    @classmethod
    def adicionar_jogo():
        input_nome = input("Nome do jogo: ")
        input_genero = input("Gênero do jogo: ")
        input_plataforma = input("Plataforma do jogo: ")
        novo_jogo = game(input_nome, input_genero, input_plataforma)
        print(f'Jogo {novo_jogo._name} adicionado com sucesso!')