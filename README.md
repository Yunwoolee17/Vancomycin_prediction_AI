# Developing machine learning model for prediction initial dosing of Vancomycin


## Dataset
- Single ceneter (Hallym University Sacred Heart Hospital)
- Data collection period : 2020.11 ~ 2023.5
- Target : All patients who has received an injection of vancomycin
- Exclusion criteria
  - under 18 years of age;
  - peritoneal dialysis or hemodialysis
  - initial dose < 900
  - eGFR < 50
  - Missing Value

## Pre-processing

# This code is rounding certain columns to a specified decimal place using the round() function in pandas

dfVanco['BMI'] = round(dfVanco['BMI'], 1)
dfVanco['WBC'] = round(dfVanco['WBC'], 1)
dfVanco['Crcl'] = round(dfVanco['Crcl'], 1)
dfVanco['Clvanco'] = round(dfVanco['Clvanco'], 1)
dfVanco['Half_life'] = round(dfVanco['Half_life'], 1)
dfVanco['Ke'] = round(dfVanco['Ke'], 3)

# To remove outliers, remove the top and bottom 5% of the dataset

q1 = dfVanco['Initial VCM_daily_dose'].quantile(0.05)
q2 = dfVanco['Initial VCM_daily_dose'].quantile(0.5)
q3 = dfVanco['Initial VCM_daily_dose'].quantile(0.95)
iqr = q3 - q1

outlier1 = dfVanco['Initial VCM_daily_dose']>(q3+1.5*iqr)
outlier2 = dfVanco['Initial VCM_daily_dose']<(q1-1.5*iqr)

a = list(dfVanco[outlier2].index)
b = list(dfVanco[outlier1].index)
a.extend(b)
df1 = dfVanco.drop(a)

## Variable addtion

'CrCl', 'Clvanco', 'Vd', 'Ke', and 'Half-life' are added by calculating as follows.

Vd and Clvanco are calculated based on Bauer Method[1].

Ke and Half-life are calculated based on formulas[2].


 
$$ CrCl = \frac{{(140 - \text{{age}}) \times \text{{Gender(Male = 1, Female = 0.85)}} \times \text{{body weight}}}}{72 \times \text{{Scr}}}$$

$$ Clvanco =  (0.695 \times frac{\text{{CrCl}}}{BodyWeight} + 0.05) \times 0.06$$

$$Vd = 0.7 $$

$$ Ke = \(0.00083×CrCl)+0.0044$$

$$ Half-life = \frac{0.693}{Ke}$$

  
 
 
1. Bauer LA. Applied Clinical Pharmacokinetics. McGraw-Hill/Appleton & Lange; 2001.
2. website: https://derangedphysiology.com/main/cicm-primary-exam/required-reading/pharmacokinetics/Chapter%20322/half-life


# 

## Modeling

- Machine learning models




## Set-up 
