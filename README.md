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

## Variable addtion
- Cockcroft-Gault CrCl, mL/min = (140 – age) × (weight, kg) × (0.85 if female) / (72 × Cr, mg/dL)
- CLvanco : (0.695∗CrCl/TotalBW+0.05)∗TotalBW∗0.06 , 'Bauer Method'
- Vd :  0.7 L/kg , 'Bauer Method'
- Ke : (0.00083×CrCl)+0.0044
- Half_life : 0.693 / Ke

# 

## Modeling

- Machine learning models




## Set-up 
