import pandas as pd
from step4_drift_detection import detect_data_drift
from step5_drift_reporting import generate_drift_report
from step6_alerting import generate_alerts

reference_df = pd.read_csv("./data/application_train.csv")
incoming_df = reference_df.copy()
incoming_df["AMT_INCOME_TOTAL"] *= 1.25

drift_results = detect_data_drift(reference_df, incoming_df)
final_report = generate_drift_report(drift_results)
alerts = generate_alerts(final_report)

print("\nFINAL DRIFT REPORT")
for feature, details in final_report.items():
    print(feature)
    for k, v in details.items():
        print(f"  {k}: {v}")

print("\nALERTS")
if not alerts:
    print("No alerts. System stable ✅")
else:
    for alert in alerts:
        print(alert)
# Why Step 5 & Step 6 Are Run in the Pipeline (4–5 lines)

# Step 5 and Step 6 depend on outputs from earlier steps, especially drift detection, 
# so they are naturally executed as part of the pipeline flow. Running them in the pipeline ensures consistent data flow, correct context, and automated decision-making. In production systems, explanation and alerting are triggered only after drift is detected, not manually.
# This design avoids human error and enables reliable end-to-end monitoring.
# “Can These Steps Run Individually?” (7–8 lines)

# Yes, Step 5 and Step 6 are designed to be modular and independently executable for debugging and validation, using a __main__ block. However,
#     in real production environments they are typically invoked through the pipeline to ensure correct sequencing and data consistency. Individual execution is mainly useful during development, testing, or incident investigation. The pipeline orchestrates these steps automatically, ensuring explanations and alerts are always generated in response to real drift events. 
# This approach balances reusability, debuggability, and production reliability.