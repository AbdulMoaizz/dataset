import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os

# raw data file
df_raw = pd.read_csv('Data Set/Temperature_change.csv', encoding='cp1252')

df = df_raw.dropna()
# After applying-interpolate on raw data file
df = df.fillna(df.ffill())

# Adding 2020,2021 and 2022 by interpolate method
df['Y2020'] = df['Y2000'].interpolate()
df['Y2021'] = df['Y2001'].interpolate()
df['Y2022'] = df['Y2002'].interpolate()

# Drop Useless Rows from Area
drop_Area = ['Least Developed Countries',
             'Land Locked Developing Countries',
             'Small Island Developing States',
             'Low Income Food Deficit Countries',
             'Net Food Importing Developing Countries',
             'Annex I countries',
             'Non-Annex I countries',
             'OECD',
             'USSR',
             'Belgium-Luxembourg',
             'China, mainland',
             'Czechoslovakia',
             'Netherlands Antilles (former)',
             'Pacific Islands Trust Territory',
             'Saint Helena, Ascension and Tristan da Cunha',
             'South Georgia and the South Sandwich Islands',
             ]

for i in range(0, len(drop_Area)):
    drop_itemsA = df[df['Area'] == drop_Area[i]].index
    df = df.drop(drop_itemsA)
# print(df)

# Drop Useless Rows from Element
drop_Element = ['Standard Deviation']

for i in range(0, len(drop_Element)):
    drop_itemsE = df[df['Element'] == drop_Element[i]].index
    df = df.drop(drop_itemsE)
# print(df)

"""# Saving Cleaned File
df.to_csv('D:\\Uni\Big Data\Data Set\cleaned_data.csv', index=False)
"""

