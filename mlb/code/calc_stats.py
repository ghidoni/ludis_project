import pandas as pd

def calc_PA(x):
    return x.AB+x.BB+x.HBP+x.SF+x.SH

def calc_TB(x):
    return x.H+x['2B']+(x['3B'])*2+(x.HR)*3

def calc_AVG(x):
    return x.H/x.AB

def calc_OBP(x):
    return (x.H+x.BB+x.HBP)/(x.AB+x.BB+x.HBP+x.SF)

def calc_SLG(x):
    return x.TB/x.AB  

def calc_OPS(x):
    return x.OBP+x.SLG

df_bat=pd.read_csv('../data/raw/Batting.csv')

df_bat['PA']=df_bat.apply(calc_PA,axis=1)
df_bat['TB']=df_bat.apply(calc_PA,axis=1)
df_bat['AVG']=df_bat.apply(calc_PA,axis=1)
df_bat['OBP']=df_bat.apply(calc_PA,axis=1)
df_bat['SLG']=df_bat.apply(calc_PA,axis=1)
df_bat['OPS']=df_bat.apply(calc_PA,axis=1)

df_bat.to_csv('../data/processed/Batting_proc.csv',index=False)