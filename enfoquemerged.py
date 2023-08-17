import pandas as pd
matches_data = pd.read_csv("WorldCupMatches.csv")
worldcups_data = pd.read_csv("WorldCups.csv")
players_data = pd.read_csv("WorldCupPlayers.csv")

merged = matches_data.merge(worldcups_data, on="Year")
merged = merged.merge(players_data, on="MatchID")

merged.to_csv("merged_data")

def c1():
    result