import pandas as pd
from bisect import bisect_left
from copy import deepcopy


def age_normalization(age):
    age_bins = [0, 13, 19, 30, 50, 65]
    return bisect_left(age_bins, age)

def simple_normalization(value, thresholds):
    return bisect_left(thresholds, value)

def crcl_normalization(crcl):
    return simple_normalization(crcl, [70])

def eGFR_normalization(egfr):
    return simple_normalization(egfr, [90])

def bun_normalization(bun):
    return simple_normalization(bun, [7])

def crp_normalization(crp):
    return simple_normalization(crp, [10])

def hb_normalization(hb, gender):
    if gender == 1: # Male
        return simple_normalization(hb, [13.5, 17.5])
    else:
        return simple_normalization(hb, [12.5, 15.5])

def plt_normalization(plt):
    return simple_normalization(plt, [150, 450])

def bmi_normalization(bmi):
    return simple_normalization(bmi, [18.5, 22.9, 24.9, 29.9])

def bmi_normalize2(bmi):
  if bmi < 18.5:
    return 0
  elif bmi < 22.9:
    return 1
  elif bmi < 24.9:
    return 2
  elif bmi < 29.9:
    return 3
  else:
    return 4

df_vanco = pd.read_csv('dataset/Vancomycin_CRF_ver11.csv')
df_vanco_norm = deepcopy(df_vanco)

df_vanco_norm['Clvanco'] = round(df_vanco['Clvanco'], 1 )
df_vanco_norm['K_e'] = round(df_vanco['K_e'], 3 )
df_vanco_norm['Clvanco'] = round(df_vanco['Clvanco'], 1 )
df_vanco_norm['Clvanco'] = round(df_vanco['Clvanco'], 1 )

df_vanco_norm['Age'] = df_vanco['Age'].apply(age_normalization)
df_vanco_norm['CrCl'] = df_vanco['CrCl'].apply(crcl_normalization)
df_vanco_norm['BUN'] = df_vanco['BUN'].apply(bun_normalization)
df_vanco_norm['CRP'] = df_vanco['CRP'].apply(crp_normalization)
df_vanco_norm['Hb'] = df_vanco.apply(lambda row: hb_normalization(row['Hb'], row['Gender']), axis=1)
df_vanco_norm['PLT'] = df_vanco['PLT'].apply(plt_normalization)
df_vanco_norm['BMI'] = df_vanco_norm['BMI'].apply(bmi_normalization)
df_vanco_norm['eGFR'] = df_vanco['eGFR'].apply(eGFR_normalization)

df_vanco.to_csv('dataset/Vancomycin_CRF_ver13.csv')
