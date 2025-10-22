import json

class game:

    def __init__(self, name, genre, platform, nota=None):
        self._name = name
        self._genre = genre
        self._platform = platform
        self.nota = nota

        self.salvar_no_arquivo()
    
    def __str__(self):
            if self.nota is None:
                return f"{self._name} - {self._genre} - {self._platform} - Sem nota"
            else: return f"{self._name} - {self._genre} - {self._platform} - Nota: {self.nota}"
    
    def to_dict(self):
        return {
            "nome": self._name,
            "genero": self._genre,
            "plataforma": self._platform,
            "nota": self.nota
        }
    
    @classmethod
    def abrir_arquivo(cls):
        try:
            with open('jogos.json', 'r') as f:
                jogos_lista = json.load(f)
                return jogos_lista
        except (FileNotFoundError, json.JSONDecodeError):
            return []
  
    def salvar_no_arquivo(self):
        jogos_lista = self.abrir_arquivo()      
        jogos_lista.append(self.to_dict())

        with open('jogos.json', 'w') as f:
            json.dump(jogos_lista, f, indent=4)

    @classmethod
    def dar_nota(cls):
        nome_jogo = input("Digite o nome do jogo que deseja avaliar: ").title()
        jogos_lista = cls.abrir_arquivo(cls)
        for jogo in jogos_lista:
            if jogo['nome'] == nome_jogo:
                nota = input(f"Digite a nota para o jogo {nome_jogo}: ")
                jogo['nota'] = nota
                with open('jogos.json', 'w') as f:
                    json.dump(jogos_lista, f, indent=4)
                print(f"Nota {nota} atribuída ao jogo {nome_jogo}.")
                return
        
        print(f"Jogo {nome_jogo} não encontrado.")

    @classmethod
    def listar_jogos(cls):
        try:
            with open('jogos.json', 'r') as f:
                jogos_lista = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            jogos_lista = []
        if jogos_lista == []:
            print("Nenhum jogo cadastrado.")
        else:
            print("\nJogos cadastrados:\n")
            for jogo in jogos_lista:
                nota = jogo['nota'] if jogo['nota'] is not None else "Sem nota"
                print(f"{jogo['nome']} - {jogo['genero']} - {jogo['plataforma']} - Nota: {nota}")
