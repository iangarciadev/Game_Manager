import json

class game:

    jogos = []

    def __init__(self, name, genre, platform):
        self._name = name.title()
        self._genre = genre
        self._platform = platform
        game.jogos.append(self)
        with open('jogos.json', 'w') as f:
            jogos_lista = [jogo.__dict__ for jogo in game.jogos]
            json.dump(jogos_lista, f, indent=4)
    
    def __str__(self):
        if hasattr(self, 'nota'):
            return f"{self._name} - {self._genre} - {self._platform} - Nota: {self.nota}"
        else:
            return f"{self._name} - {self._genre} - {self._platform}"
    
    def dar_nota(self, nota):
        self.nota = nota
        return f"A nota de {self._name} agora é {self.nota}"
    
    @classmethod
    def listar_jogos(cls):
        for jogo in cls.jogos:
            print(jogo)
    