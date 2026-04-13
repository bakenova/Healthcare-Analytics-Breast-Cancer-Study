# Breast Cancer Treatment Response Prediction
> End-to-end Data Science project focused on predicting chemotherapy response using clinical and treatment data.

Data source: https://www.kaggle.com/datasets/waddahali/breast-cancer-treatment-journey

1. Problem

Treatment response in breast cancer patients is highly heterogeneous.
Clinicians must often choose a therapy regimen without reliable early indicators of effectiveness.

This project addresses the following question:

Can we predict patient response to chemotherapy using baseline clinical and treatment features?


2. Objective

Build a machine learning model to predict:

	•	Target: Response_Status

	•	Type: Multi-class classification

Classes:

	•	Complete

	•	Partial

	•	None


3. Data

Data is split into patient-level and treatment-level tables and later merged for analysis. The dataset contains 4980 patient-treatment records with no missing values.

Feature groups:

	•	Patient characteristics

Age_at_Diagnosis, BRCA_Mutation

	•	Tumor features

Initial_Tumor_Size_mm, Tumor_Grade, Molecular_Subtype

	•	Treatment information

Regimen, Treatment_Round

	•	Clinical indicators

CA15_3_Level, Tumor_Shrinkage_Pct


4. Analytical Approach

The project follows a standard Data Science workflow:

	1.	Data Understanding

	2.	Exploratory Data Analysis (EDA)

	3.	Preprocessing

	4.	Feature Engineering

	5.	Modeling

	6.	Evaluation


5. Key Hypotheses

	•	Higher CA15_3_Level → lower probability of complete response

	•	Larger tumors → reduced shrinkage

	•	BRCA_Mutation influences treatment effectiveness

	•	Response varies significantly across Regimen and Molecular_Subtype


6. Evaluation

Model performance will be assessed using:

	•	F1-score (primary metric)

	•	Accuracy

	•	Confusion Matrix


7. Expected Outcome

	•	Identification of key drivers of treatment response

	•	Comparative effectiveness of treatment regimens

	•	Predictive model to support clinical decision-making


8. Project Structure
```
.
├── datasets/
│   ├── patient_profiles.csv       			 # Patient-level demographic & clinical data
│   └── treatment_journey.csv      			 # Treatment cycles and outcomes
│
├── notebooks/
│   ├── 01_data_understanding.ipynb 		 # Data overview, structure, initial insights
│   ├── 02_exploratory_data_analysis.ipynb   # Exploratory data analysis & visualizations
│   ├── 03_preprocessing.ipynb      		 # Data cleaning, encoding, scaling
│   ├── 04_feature_engineering.ipynb# Feature creation & transformations
│   └── 05_modeling.ipynb           		 # Model training, evaluation, comparison
│
├── reports/
│
├── src/
│
├── README.md                     			 # Project documentation
```


## Pipeline Overview

Raw Data → Data Understanding → EDA → Preprocessing → Feature Engineering → Modeling → Evaluation