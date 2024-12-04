# Development and external validation of a machine learning model to predict the initial dose of vancomycin for targeting an area under the concentration-time curve of 400–600 mg∙h/L  

## 1. Introduction
This repository contains dataset and code for predicting the initial dosing of vancomycin, an antibiotic used to treat serious bacterial infections. The code performs internal and external validation of the predictive model.
- The code is written under the assumption that it is performed in 'Google Colab'
- About Google Colab : https://github.com/WiktorJ/google-colab-tutorial/blob/master/README.md

## 2. Dependencies and Installation
To run the code, you need Python and the following libraries:
- pandas, numpy
- scikit-learn, xgboost, lightgbm, catboost, shap 
- matplotlib, seaborn
- google.colab 

You can install the required libraries using `pip`:

## 3. Dataset
The dataset required for this model can be downloaded from the `dataset` folder in this repository.

## 4. Code Overview

1. Data Upload and preparation
2. Exploratory Data Analysis (EDA)
3. Modeling
4. Internal validation
5. External vadliation & visualization
6. Summary of parameter
7. SHAP(SHapley Additive exPlanations) analysis
8. Supplemental Material - Distribution of Internal, external dataset

## 5. Results

The performance of six machine learning models and a Voting Ensemble was evaluated using root mean squared error (RMSE), mean absolute error (MAE), R-squared (R²), and 20% accuracy (predictions within ±20% of the actual dose). In internal validation, the Random Forest model demonstrated the best 20% accuracy at 56.8%. In external validation, the XGBoost model achieved the highest 20% accuracy at 74.3%. 

## 6. Contact
For any queries, you can reach out to [kunlun6798@gmail.com].
