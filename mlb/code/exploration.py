import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df_bat=pd.read_csv('../data/Batting.csv')
print(df_bat.shape)
df_bat2=df_bat[df_bat['yearID']>1990]
print(df_bat2.shape)

