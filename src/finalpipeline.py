import pandas as pd
from schema_validation import validate_schema, load_schema
from step2_data_quality import data_quality_check
from step3_anomaly_detection import detect_anomalies
from step4_drift_detection import detect_data_drift
from step5_drift_reporting import generate_drift_report
from step6_alerting import generate_alerts
from step7_model_training import train_baseline_model
from step8_model_monitoring import monitor_model_performance


def run_pipeline():
    print("starting at data and model monitoring pipeline")

    reference_df=pd.read_csv("./data/application_train.csv")
    incoming_df=reference_df.copy()
    incoming_df["AMT_INCOME_TOTAL"] *= 1.25
    print("data loaded")
    #schema
    schema=load_schema("./config/schema.yaml")
    validate_schema(reference_df, schema)
    print("schema validation passed")
    #data quality
    quality_report=data_quality_check(reference_df)
    print("data quality check completed")
    #anomaly detection
    anomaly_report=detect_anomalies(reference_df)
    print("anomaly detection completed")
    #data drift
    drift_results=detect_data_drift(reference_df,incoming_df)
    print("data drift detection completed")
    #drift explanations
    final_drift_report=generate_drift_report(drift_results)
    print("\nfinal report")
    for feature,details in final_drift_report.items():
        print(feature)
        for k,v in details.items():
            print(f"{k}:{v}")
    #alerts
    alerts=generate_alerts(final_drift_report)
    print("\n ALERTS")
    if not alerts:
        print("No alerts. System stable ")
    else:
        for alert in alerts:
            print(alert)

    #model training
    model, baseline_metrics = train_baseline_model(reference_df)
    print("\n🤖 BASELINE MODEL METRICS")
    for k, v in baseline_metrics.items():
        print(f"{k}: {v}")
    #Step 8: Model Performance Monitoring
    # -------------------------------
    X_new = incoming_df[["AMT_INCOME_TOTAL", "AMT_CREDIT", "DAYS_BIRTH"]]
    y_new = incoming_df["TARGET"]

    performance_report = monitor_model_performance(
        model,
        X_new,
        y_new,
        baseline_metrics
    )

    print("\n MODEL PERFORMANCE REPORT")
    for k, v in performance_report.items():
        print(f"{k}: {v}")
    if (
        performance_report["accuracy_decay"]
        or performance_report["confidence_decay"]
        or any(alert["severity"] == "HIGH" for alert in alerts)
    ):
        print("\n🔁 RETRAINING RECOMMENDED")
    else:
        print("\n✅ Model performance stable. No retraining needed.")

    print("\n🏁 PIPELINE COMPLETED SUCCESSFULLY")


if __name__ == "__main__":
    run_pipeline()
