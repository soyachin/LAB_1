import pandas as pd

matches_data = pd.read_csv("WorldCupMatches.csv")
players_data = pd.read_csv("WorldCups.csv")
worldcups_data = pd.read_csv("WorldCupPlayers.csv")


def c1():
    result = matches_data[(matches_data["Away Team Name"] == "Ecuador") | (matches_data["Home Team Name"] == "Ecuador")]
    years = result["Year"].tolist()
    print(result.to_string())
    print(set(years))

def c2():
    brazil_argentina_matchess = matches_data[
        ((matches_data['Home Team Name'] == 'Argentina') & (matches_data['Away Team Name'] == 'Brazil')) |
        ((matches_data['Home Team Name'] == 'Brazil') & (matches_data['Away Team Name'] == 'Argentina'))
        ]

    cant = len(brazil_argentina_matchess)
    print(brazil_argentina_matchess)
    print(f"Se enfrentaron {cant} veces")

c1()
c2()