import pandas as pd
flor1 = pd.read_csv("test1.csv")
flor2 = pd.read_csv("test2.csv")

flores = pd.merge(flor1, flor2, on="Flor")
print(flores)