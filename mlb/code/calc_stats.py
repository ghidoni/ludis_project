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

def calc_ISO(x):
    return x.SLG-x.AVG

def calc_BABIP(x):
    if (x.AB-x.SO-x.HR+x.SF)==0:
        return 0
    else:
        return (x.H+x.HR)/(x.AB-x.SO-x.HR+x.SF)

def calc_wOBA(x):
    if (x.AB+x.BB-x.IBB+x.SF+x.HBP)==0:
        return 0
    else:
        return (x.BB*0.69+x.HBP*0.72+(x.H-x['2B']-x['3B']-x.HR)*0.89+x['2B']*1.27+x['3B']*1.62+x.HR*2.1)/(x.AB+x.BB-x.IBB+x.SF+x.HBP)

def calc_RC(x):
    if (x.AB+x.BB)==0:
        return 0
    else:
        return (x.TB*(x.H+x.BB)/(x.AB+x.BB))

def calc_WHIP(x):
    if x.IPouts==0:
        return 0
    else:
        return (x.BB+x.H)/x.IPouts*3

def calc_FIP(x):
    if x.IPouts==0:
        return 0
    else:
        return (((13*x.HR)+(3*(x.BB+x.HBP))-(2*x.SO))/x.IPouts*3) + 3.17

def calc_K9(x):
    return 

def calc_BB9(x):
    return

def calc_KBB(x):
    if x.BB == 0:
        return 0
    else:
        return x.SO/x.BB

df_bat=pd.read_csv('../data/raw/Batting.csv')

df_bat['PA']=df_bat.apply(calc_PA,axis=1)
df_bat['TB']=df_bat.apply(calc_PA,axis=1)
df_bat['AVG']=df_bat.apply(calc_PA,axis=1)
df_bat['OBP']=df_bat.apply(calc_PA,axis=1)
df_bat['SLG']=df_bat.apply(calc_PA,axis=1)
df_bat['OPS']=df_bat.apply(calc_PA,axis=1)
df_bat['ISO']=df_bat.apply(calc_ISO,axis=1)
df_bat['BABIP']=df_bat.apply(calc_BABIP,axis=1)
df_bat['wOBA']=df_bat.apply(calc_wOBA,axis=1)

df_bat.to_csv('../data/processed/Batting_proc.csv',index=False)

df_pit=pd.read_csv('../data/raw/Pitching.csv')

df_pit['WHIP']=df_pit.apply(calc_WHIP,axis=1)
df_pit['FIP']=df_pit.apply(calc_FIP,axis=1)
df_pit['SO/BB']=df_pit.apply(calc_KBB,axis=1)

df_pit.to_csv('../data/processed/Pitching_proc.csv',index=False)