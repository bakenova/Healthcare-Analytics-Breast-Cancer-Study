# \\src/data_loader.py

import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def load_data():
    patient_path = os.path.join(BASE_DIR, "datasets", "patient_profiles.csv")
    treatment_path = os.path.join(BASE_DIR, "datasets", "treatment_journey.csv")

    patient_df = pd.read_csv(patient_path)
    treatment_df = pd.read_csv(treatment_path)

    return patient_df, treatment_df


def merge_data(patient_df, treatment_df):
    return treatment_df.merge(patient_df, on="Patient_ID", how="left")