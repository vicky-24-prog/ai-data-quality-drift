import pandas as pd
from scipy.stats import ks_2samp

DRIFT_COLUMNS = [
    "AMT_INCOME_TOTAL",
    "AMT_CREDIT",
    "DAYS_BIRTH"
]

def detect_data_drift(reference_df, incoming_df, threshold=0.05):
    drift_report={}
    for column in DRIFT_COLUMNS:
        stat,p_value=ks_2samp(
            reference_df[column].dropna(),
            incoming_df[column].dropna()
        )
        drift_report[column]={
            "p_value":round(p_value,6),
            "drift_detected": p_value < threshold
        }
    return drift_report

if __name__ == "__main__":
    reference_df = pd.read_csv("../data/application_train.csv")
    incoming_df = reference_df.copy()
    incoming_df["AMT_INCOME_TOTAL"] *= 1.25  # simulate income shift

    drift_results = detect_data_drift(reference_df, incoming_df)

    print("DATA DRIFT REPORT")
    for col, result in drift_results.items():
        print(f"{col}: {result}")