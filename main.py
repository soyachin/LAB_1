import pandas as pd

matches_data = pd.read_csv("WorldCupMatches.csv")
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




c1()
c2()
c3()
