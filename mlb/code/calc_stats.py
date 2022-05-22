import pandas as pd

def calc_PA(x):
    return x.AB+x.BB+x.HBP+x.SF+x.SH

def calc_TB(x):
    return x.H+x['2B']+(x['3B'])*2+(x.HR)*3

def calc_AVG(x):
    if x.AB==0:
        return 0
    else:
        return x.H/x.AB

def calc_OBP(x):
    if (x.AB+x.BB+x.HBP+x.SF)==0:
        return 0
    else:
        return (x.H+x.BB+x.HBP)/(x.AB+x.BB+x.HBP+x.SF)

def calc_SLG(x):
    if x.AB==0:
        return 0
    else:
        return x.TB/x.AB  

def calc_OPS(x):
    return x.OBP+x.SLG

def calc_WHIP(x):
    if x.IPouts==0:
        return 0
    else:
        return (x.BB+x.H)/x.IPouts*3

df_bat=pd.read_csv('../data/raw/Batting.csv')

df_bat['PA']=df_bat.apply(calc_PA,axis=1)
df_bat['TB']=df_bat.apply(calc_PA,axis=1)
df_bat['AVG']=df_bat.apply(calc_PA,axis=1)
df_bat['OBP']=df_bat.apply(calc_PA,axis=1)
df_bat['SLG']=df_bat.apply(calc_PA,axis=1)
df_bat['OPS']=df_bat.apply(calc_PA,axis=1)

df_bat.to_csv('../data/processed/Batting_proc.csv',index=False)

df_pit=pd.read_csv('../data/raw/Pitching.csv')

df_pit['WHIP']=df_pit.apply(calc_WHIP,axis=1)

df_pit.to_csv('../data/processed/Pitching_proc.csv',index=False)