# Development and external validation of a machine learning model for predicting initial vancomycin dose to target the area under the concentration-time curve of 400–600 mg∙h/L 

## 1. Introduction
This repository contains dataset and code for predicting the initial dosing of vancomycin, an antibiotic used to treat serious bacterial infections. The code performs internal and external validation of the predictive model.
- The code is written under the assumption that it is performed in 'Google Colab'
- About Google Colab : https://github.com/WiktorJ/google-colab-tutorial/blob/master/README.md

## 2. Dependencies and Installation
To run the code, you need Python and the following libraries:
- pandas
- numpy
- scikit-learn
- xgboost
- matplotlib
- seaborn

You can install the required libraries using `pip`:

## 3. Dataset
The dataset required for this model can be downloaded from the `dataset` folder in this repository.

## 4. Code Overview
- 1 Upload training dataset
- 2 Analysis of training dataset
  - 2-1 Description of training dataset
  - 2-2 Distributions of all variables
- 3 Modeling
  - 3-1 Data Splitting
  - 3-2 Random Forest Model
  - 3-3 XGBoost Model
  - 3-4 Ensemble Model
  - 3-5 Model Performance Comparison
- 4 Internal validation
  - 4-1 Internal dataset load
  - 4-2 Predictions using trained models
  - 4-3 Evaluation : Calculate accuracy based on the 20% threshold
- 5 External validation
  - 5-1 External dataset load
  - 5-2 Predictions using trained models
  - 5-3 Evaluation : Calculate accuracy based on the 20% threshold
- 6 Model Performance Summary
- 7 Feature importance analysis
  - Random Forest
  - XGBoost
  - Ensemble Model
- 8 supplementary materials
  - 8-1 Distributions of internal training dataset
  - 8-2 Distributions of external training datase



## 5. Results
Random Forest, XGBoost, and Ensemble models were evaluated using MSE, RMSE, R², and an accuracy measure with a ±20% threshold of the actual dose.

- Internal Validation Results:
Dataset Size: 44 patients
Model Accuracy:
Random Forest : 56.8%
25 out of 44 (Number of Correct Predictions)
XGBoost : 54.5%
24 out of 44 (Number of Correct Predictions)
Ensemble : 59.0%
26 out of 44 (Number of Correct Predictions)

- External Validation Results:
Dataset Size: 35 patients
Model Accuracy:
Random Forest : 71.4%
25 out of 35 (Number of Correct Predictions)
XGBoost : 62.8%
22 out of 35 (Number of Correct Predictions)
Ensemble : 65.7%
23 out of 35 (Number of Correct Predictions)

## 6. Contact
For any queries, you can reach out to [kunlun6798@gmail.com].
