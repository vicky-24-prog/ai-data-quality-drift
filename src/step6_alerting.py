def  generate_alerts(report):
    alerts=[]

    for feature,details in report.items():
        severity=details["severity"]

        if severity=="HIGH":
           alerts.append({
                "feature": feature,
                "severity": severity,
                "action": "Immediate investigation and model retraining recommended"
            })

        elif severity == "MEDIUM":
            alerts.append({
                "feature": feature,
                "severity": severity,
                "action": "Monitor closely and validate downstream impact"
            })

    return alerts