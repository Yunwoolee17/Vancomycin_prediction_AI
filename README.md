# Developing machine learning model for prediction initial dosing of Vancomycin

## 0. Set-up
- The code is written under the assumption that it is performed in 'Google Colab'
- Note : After creating a folder named 'data' under MyDrive, we put the dataset there.
  - pd.read_excel('/content/drive/MyDrive/data/original_dataset.xlsx')
- About Google Colab : https://github.com/WiktorJ/google-colab-tutorial/blob/master/README.md

## 1. Dataset
### 1-1. Data Collection
- Single ceneter (Hallym University Sacred Heart Hospital)
- Data collection period : 2020.11 ~ 2023.4
- Target : All patients who has received an injection of vancomycin
  - not on dialysis
  - underwent TDM within 5 days
- Exclusion criteria
  - under 18 years of age;
  - peritoneal dialysis or hemodialysis
  - initial dose < 900
  - eGFR < 50
  - Missing Value

### 1-2. Dataset Description
- original_dataset : n = 166
  - Patients with an AUC value between 400 and 600 who did not meet the exlcusion criteria.
  - 99 patients, 60% of patients, received 2000 mg of VCM.
  
- augmented_dataset : n = 424
  - Removed 2 outliers out of 166 in original_dataset: n = 164
  - 4-fold amplification after excluding 99 patients who received 2000mg out of 164 patients : n = 260 ( (164-99) * 4 )
  - Combining the above data with the existing 164 people : n = 424 (164 + 260)
  
- Log transformed_dataset : n = 424
  - A dataset that takes the 'Natural Logarithm' of the target value 'Initial VCM_daily_dose'
  - Code : df1['Initial VCM_daily_dose_log'] = df1['Initial VCM_daily_dose'].apply(lambda x: math.log(x))
  - Example)
    - 1000mg of VCM --> 6.9077
    - 1500mg of VCM --> 7.3132
    - 2000mg of VCM --> 7.6009
    - 3000mg of VCM --> 8.0063

## 2. Variable addtion

### 5 variables are added by calculating as follows.
- CrCl : Creatinine Clearance
- Clvanco : Vancomycin Clearance
- Vd : Voulme of distribution
- Ke : Elemination rate constant
- Half-life : The time it takes for the concentration of the drug to decrease by half (1/2)


 
$$ CrCl = \frac{{(140 - \text{{age}}) \times \text{{Gender(Male = 1, Female = 0.85)}} \times \text{{body weight}}}}{72 \times \text{{Scr}}}$$

$$ Clvanco =  (0.695 \times {{CrCl}}/{TotalBW} + 0.05) \times TotalBW \times 0.06$$

$$Vd = 0.7 L/kg $$

$$ Ke = \(0.00083×CrCl)+0.0044$$

$$ Half-life = \frac{0.693}{Ke}$$



- Clvanco and Vd are calculated based on Bauer Method [1].
- Ke and Half-life are calculated based on popular formulas, sometimes called the Creighton equation. [2].
- ---
1. Bauer LA. Applied Clinical Pharmacokinetics. McGraw-Hill/Appleton & Lange; 2001.
2. Matzke GR, McGory RW, Halstenson CE, Keane WF. Pharmacokinetics of vancomycin in patients with various degrees of renal function. Antimicrob Agents Chemother. 1984 Apr;25(4):433-7. PMID 673221

## 3. Pre-processing

### 3-1. This code is rounding certain columns to a specified decimal place using the round() function in pandas

- dfVanco['BMI'] = round(dfVanco['BMI'], 1)
- dfVanco['WBC'] = round(dfVanco['WBC'], 1)
- dfVanco['Crcl'] = round(dfVanco['Crcl'], 1)
- dfVanco['Clvanco'] = round(dfVanco['Clvanco'], 1)
- dfVanco['Half_life'] = round(dfVanco['Half_life'], 1)
- dfVanco['Ke'] = round(dfVanco['Ke'], 3)

### 3-2. To remove outliers, remove the top and bottom 5% of the dataset

- q1 = dfVanco['Initial VCM_daily_dose'].quantile(0.05)
- q2 = dfVanco['Initial VCM_daily_dose'].quantile(0.5)
- q3 = dfVanco['Initial VCM_daily_dose'].quantile(0.95)
- iqr = q3 - q1

----
- outlier1 = dfVanco['Initial VCM_daily_dose']>(q3+1.5*iqr)
- outlier2 = dfVanco['Initial VCM_daily_dose']<(q1-1.5*iqr)
----
- a = list(dfVanco[outlier2].index)
- b = list(dfVanco[outlier1].index)
- a.extend(b)
- df1 = dfVanco.drop(a)


## 4. Modeling

- Machine learning models : We use 'Pycaret', An open-source, low-code auto-machine learning library in Python
- About Pycaret : https://github.com/pycaret/pycaret/blob/master/README.md


## 5. Feature importance & Selection
- Variables marked as important in pycaret and variables marked as important in SHAP were combined.
  - Pycaret_Feature_importance = ['Weight', 'Vd', 'Age', 'BUN', 'Half_life', 'eGFR', 'Height','Clvanco', 'Ke', 'ACEi' ]
  - SHAP_Feature_importance = ['Clvanco', 'CRP', 'eGFR', 'ARB', 'Age', 'PLT','SCr', 'Weight', 'Hb','Gender']
 
    
- union_set = set(Pycaret_Feature_importance) | set(SHAP_Feature_importance)
  - union_list = list(union_set)
  - union_list = ['Gender', 'Age', 'Weight', 'Height', 'Hb', 'PLT', 'CRP', 'eGFR', 'BUN', 'SCr','ACEi', 'ARB', 'Clvanco', 'Vd', 'Ke', 'Half_life']
