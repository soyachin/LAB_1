import pandas as pd

matches_data = pd.read_csv("WorldCupMatches.csv")

worldcups_data = pd.read_csv("WorldCups.csv")

players_data = pd.read_csv("WorldCupPlayers.csv")


def c1():
    result = matches_data[(matches_data["Away Team Name"] == "Ecuador") | (matches_data["Home Team Name"] == "Ecuador")]
    years = result["Year"].tolist()
    colum_mos = ["Year", "Away Team Name", "Home Team Name"]
    pp = result[colum_mos]
    print(pp.to_string())
    rpta = sorted(list(set(years)))

    print("C1. Ecuador participó en los años: ", end="")
    for i in range(len(rpta)):
        print(int(rpta[i]), end="")
        if i != (len(rpta) - 1):
            print(", ", end="")

    print("\n")

    show = pd.DataFrame(result).drop_duplicates(subset="Year", keep="first").loc[:, ["Year", "Home Team Name", "Away Team Name"]]
    print(show, "\n")


def c2():
    brazil_argentina_matches = matches_data[
        ((matches_data['Home Team Name'] == 'Argentina') & (matches_data['Away Team Name'] == 'Brazil')) |
        ((matches_data['Home Team Name'] == 'Brazil') & (matches_data['Away Team Name'] == 'Argentina'))
        ]

    cant = len(brazil_argentina_matches)
    colum_mos = ["Year", "Away Team Name", "Home Team Name"]
    pp = brazil_argentina_matchess[colum_mos]
    print(pp.to_string())
    print(f"C2. Se enfrentaron {cant} veces\n")
    show = pd.DataFrame(brazil_argentina_matches).drop_duplicates(subset="Year", keep="first").loc[:, ["Year", "Home Team Name", "Away Team Name"]]
    print(show, "\n")


def c3():
    show_winner = pd.DataFrame(worldcups_data[(worldcups_data["Year"] == 2010)].loc[:, ["Year", "Country", "Winner"]])
    consulta_winner = show_winner["Winner"]
    winner = consulta_winner.tolist()
    winner = str(winner[0])  # spain

    # year = 2010, stage = final, match id = 300061509
    # team initials ESP, search for Player Name

    consulta_id = matches_data[(matches_data["Year"] == 2010) & (matches_data["Stage"] == "Final")]
    consulta_id = consulta_id["MatchID"].tolist()[0]

    teamtable = players_data[(players_data["Team Initials"] == "ESP") & (players_data["MatchID"] == consulta_id) & (players_data["Line-up"] == "S")]
    show = pd.DataFrame(teamtable).drop_duplicates(subset="Player Name", keep="first").loc[:, ["Team Initials", "Player Name", "Line-up"]]

    print(f"C3.1. El ganador de la Copa del Mundo en 2004 fue {winner}\n")
    print(show_winner, "\n")

    print("C3.2. Los 11 jugadores titulares fueron: ")
    teamlist = teamtable["Player Name"].tolist()

    for i in range(len(teamlist)):
        print(teamlist[i], end="")
        if i != (len(teamlist) - 1):
            print(", ", end="")

    print("\n")

    print(show, "\n")


def c4():
    veces_jugadas = players_data[(players_data['Player Name'] == 'RONALDINHO')]
    aniosjugados = []
    for id in veces_jugadas["MatchID"]:
        anio = matches_data[matches_data["MatchID"] == id]["Year"].values[0]
        if anio not in aniosjugados:
            aniosjugados.append(anio)
    como_suplente = players_data[(players_data['Player Name'] == 'RONALDINHO') & (players_data['Line-up'] == 'N')]

    cant = len(aniosjugados)
    cSup = len(como_suplente)
    print(veces_jugadas.to_string())
    print(f"RONALDINHO Participo {cant} veces al mundial")
    print(f"RONALDINHO Participo como suplente {cSup} veces al mundial")

    

c1()
c2()
c3()
c4()