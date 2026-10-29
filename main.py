from pyswip import Prolog

def main():
    print("---- Sistema de Recomendação de Jogos ----")

    prolog = Prolog()
    prolog.consult("jogos.pl")

    genero = input("Digite o gênero (ex: rpg, simulacao): ").strip().lower()
    modo = input("Digite o modo (ex: single_player, multiplayer): ").strip().lower()
    plataforma = input("Digite a plataforma (ex: pc, playstation): ").strip().lower()

    query = f"recomendar({genero}, {modo}, {plataforma}, Jogo)"
    resultados = list(prolog.query(query))

    print("\n---- Jogos Recomendados ----")

    if len(resultados) > 0:
        for resultado in resultados:
            print(f"- {resultado['Jogo']}")
    else:
        print("Nenhum jogo encontrado com esses critérios.")

if __name__ == "__main__":
    main()