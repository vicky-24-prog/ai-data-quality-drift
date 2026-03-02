import pandas as pd

NUMERIC_COLUMNS = [
    "AMT_INCOME_TOTAL",
    "AMT_CREDIT",
    "DAYS_BIRTH"
]

def detect_anomalies(df):
    anomaly_report={}

    for column in NUMERIC_COLUMNS:
        q1=df[column].quantile(0.25)
        q3=df[column].quantile(0.75)
        iqr=q3-q1

        lower_bound=q1 - 1.5 * iqr
        upper_bound=q3+1.5*iqr

        anomaly_count=int(((df[column]< lower_bound) | (df[column]> upper_bound)).sum())

        anomaly_report[column]={
            "lower bound":round(lower_bound,2),
            "upper_bound": round(upper_bound, 2),
            "anomaly_count": anomaly_count

        }
    return anomaly_report
if __name__ == "__main__":
    df = pd.read_csv("./data/application_train.csv")

    anomalies = detect_anomalies(df)

    print("ANOMALY DETECTION REPORT")
    for col, info in anomalies.items():
        print(f"{col}: {info}")

