import pandas as pd
def data_quality_check(df):
    report = {}
    # identifyinng Missing value percentage per column
    missing_percent=(df.isnull().sum()/len(df))*100
    report["missing_percentage"]=missing_percent.round(2).to_dict()
    # critical rnage checking

    report["invalid_income"]=int((df["AMT_INCOME_TOTAL"]<=0).sum())
    report["invalid_credit"]=int((df["AMT_CREDIT"]<=0).sum())
    report["invalid_birth_days"]=int((df["DAYS_BIRTH"]>=0).sum())
    # data health flag
    CRITICAL_COLUMNS = [
    "AMT_INCOME_TOTAL",
    "AMT_CREDIT",
    "DAYS_BIRTH"
]





    report["quality_status"]="pass"
    critical_misiing=missing_percent[CRITICAL_COLUMNS]
    if critical_misiing.max()>20:
        report["quality_status"]="fail"
    return report

if __name__ == "__main__":
    df = pd.read_csv("./data/application_train.csv")
    quality_report = data_quality_check(df)

    print("DATA QUALITY REPORT")
    for key, value in quality_report.items():
        print(f"{key}: {value}")
# What Your Data Actually Looks Like (Key Insight)

# From your output, some columns have huge missing values:

# OWN_CAR_AGE → 65.99% missing

# OCCUPATION_TYPE → 31.35% missing

# EXT_SOURCE_1 → 56.38% missing

# Many housing-related columns → 50–70% missing

# 👉 This is normal for this dataset.
# 👉 Kaggle itself documents this.