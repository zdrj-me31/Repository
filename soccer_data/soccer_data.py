#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

soccer_data = pd.read_csv("soccer_data.csv", index_col=0)

home_fauls = soccer_data[["HomeTeam", "HF"]]

# home teams
home_teams = soccer_data["HomeTeam"]

# away teams
away_teams = soccer_data["AwayTeam"]

# home matches for Manu

manu_home = soccer_data[soccer_data.HomeTeam == "Man United"]
manu_away = soccer_data[soccer_data.AwayTeam == "Man United"]


home_fauls_commited = manu_home["HF"].sum()
away_fauls_commited = manu_away["AF"].sum()
print(home_fauls_commited)
print(away_fauls_commited)

if home_fauls_commited > away_fauls_commited:
    print("United fouled more times at Home.")
else:
    print("United fouled more times when they played away.")


home_won_manu = soccer_data[
    (soccer_data.HomeTeam == "Man United") & (soccer_data.FTR == "H")
]

print(home_won_manu)

# copy of dataframe

soccer_data_copy = soccer_data.copy()


def count_entries(csv_file, c_size, colname):
    """Return dict with counts of occurrenc as value for each key"""
    count_dict = {}
    for chunk in pd.read_csv(csv_file, chunksize=c_size):
        for entry in chunk[colname]:
            if entry in count_dict.keys():
                count_dict[entry] += 1
            else:
                count_dict[entry] = 1
    return count_dict


count_ref = count_entries("soccer_data.csv", 100, "Referee")
print(count_ref)

ref_list = list(soccer_data["Referee"].unique())
print(ref_list)
