import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, roc_auc_score
def train_baseline_model(df):

    # """
    # Trains a baseline model and returns:
    # - trained model
    # - baseline accuracy
    # - baseline prediction confidence
    # """
    x = df[["AMT_INCOME_TOTAL", "AMT_CREDIT", "DAYS_BIRTH"]]
    y = df["TARGET"]

    #splitting the data
    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
    #model tarining
    model=LogisticRegression(max_iter=1000)
    model.fit(x_train,y_train)
    #predict
    predictions=model.predict(x_test)
    probabilities=model.predict_proba(x_test)
    #metrics
    accuracy=accuracy_score(y_test,predictions)
    avg_confidence=np.max(probabilities,axis=1).mean()
    baseline_metrics={
        "accuracy": round(accuracy,4),
        "avg_confidence": round(avg_confidence,4)
    }
    return model,baseline_metrics

if __name__ == "__main__":
    df = pd.read_csv("./data/application_train.csv")
    model, metrics = train_baseline_model(df)

    print("BASELINE MODEL METRICS")
    for k, v in metrics.items():
        print(f"{k}: {v}")