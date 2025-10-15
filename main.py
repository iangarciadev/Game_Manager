from Modelos.game import game




def main():
    TombRaider = game("Tomb Raider", "Action-Adventure", "PC")
    TombRaider.dar_nota(9.5)    
    GodOfWar = game("God of War", "Action", "PlayStation")
    game.listar_jogos()

if __name__ == "__main__":
    main()