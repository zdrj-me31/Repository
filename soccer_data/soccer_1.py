import pandas as pd
import numpy as np

soccer_data = pd.read_csv('soccer_data.csv')

# print head
print(soccer_data.head())

# print info
print(soccer_data.info())

# print shape  - as attribute
print(soccer_data.shape)  # 380 rows, 22 columns

print(soccer_data.describe())  # some statistics
print(soccer_data.index)


# values sorted by number of yellow cards recieved by home team
yellow_card_home = soccer_data.sort_values('HY', ascending=False)
print(yellow_card_home)


# win home and HST is more than 4

win_home = soccer_data['FTR'] == 'H'
more_than_four = soccer_data['HST'] > 6

home_win_more_thanfourshots = soccer_data[win_home & more_than_four]
print(home_win_more_thanfourshots['HomeTeam'])  # leicester, chelsea, crystalP

# sort by number of yellow cards from home team and desc yellow by away

yellow_cards_home_away = soccer_data.sort_values(
    ['HY', 'AY'], ascending=[False, True])
print(yellow_cards_home_away.head())

home_manu = soccer_data[soccer_data['HomeTeam'] == 'Man United']
away_manu = soccer_data[soccer_data['AwayTeam'] == 'Man United']

print(home_manu.describe())

# win or draw when manchester united was a host

win_draw_home_manu = home_manu[home_manu['FTR'].isin(['H', 'D'])]
print(win_draw_home_manu)


def iqr(column):
    return column.quantile(0.75) - column.quantile(0.25)


print(soccer_data[['HS', 'HTHG']].agg(iqr))

# value counts for wins draws loses
results_home_manu_values = home_manu['HTR'].value_counts(normalize=True)
print(results_home_manu_values)


# pivot table with mediana of FTHG, HS, HST, columns as FTR, index as home teams
our_home_table = soccer_data.pivot_table(values=['FTHG', 'HST', 'HS'],
                                         index='HomeTeam',
                                         columns='FTR', fill_value=0,
                                         aggfunc=np.median)


# homeTeam as indexes
homeTeam_ind = soccer_data.set_index("HomeTeam")

# give only Man United, Arsenal, Chelsea

my_example = homeTeam_ind.loc[["Man United", "Arsenal", "Chelsea"]]

# subset by index
by_index = soccer_data[soccer_data['HomeTeam'].isin(["Man United", "Arsenal"])]
