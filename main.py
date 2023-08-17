import pandas as pd

matches_data = pd.read_csv("WorldCupMatches.csv")
# Contiene Year, Datetime,Stage,Stadium,City,Home Team Name,Home Team Goals,Away Team Goals,Away Team Name,Win conditions,Attendance,Half-time Home Goals,Half-time Away Goals,Referee,Assistant 1,Assistant 2,RoundID,MatchID,Home Team Initials,Away Team Initials

worldcups_data = pd.read_csv("WorldCups.csv")

players_data = pd.read_csv("WorldCupPlayers.csv")

def c1():
    result = matches_data[(matches_data["Away Team Name"] == "Ecuador") | (matches_data["Home Team Name"] == "Ecuador")]
    years = result["Year"].tolist()
    # print(result.to_string())
    rpta = list(set(years))
    print("C1. Ecuador participó en los años: ", end="")
    for i in range(len(rpta)):
        print(int(rpta[i]), end="")
        if i != (len(rpta) - 1):
            print(", ", end="")


    print("")


def c2():
    brazil_argentina_matchess = matches_data[
        ((matches_data['Home Team Name'] == 'Argentina') & (matches_data['Away Team Name'] == 'Brazil')) |
        ((matches_data['Home Team Name'] == 'Brazil') & (matches_data['Away Team Name'] == 'Argentina'))
        ]

    cant = len(brazil_argentina_matchess)
    # print(brazil_argentina_matchess)
    print(f"C2. Se enfrentaron {cant} veces")

def c3():
    winner = worldcups_data[(worldcups_data["Year"] == 2010)]["Winner"]
    result = winner.tolist()
    print(f"C3. El ganador de la Copa del Mundo en 2004 fue {result[0]}")

def c4():
    cant_mund_jug = players_data[(players_data['Player Name'] == 'RONALDINHO')]
    como_suplente = players_data[(players_data['Player Name'] == 'RONALDINHO') & (players_data['Line-up'] == 'N')]

    cant = len(cant_mund_jug)
    cSup = len(como_suplente)
    print(cant_mund_jug)
    print(f"RONALDINHO Participo {cant} veces al mundial")
    print(f"RONALDINHO Participo como suplente {cSup} veces al mundial")


c1()
c2()
c3()
c4()