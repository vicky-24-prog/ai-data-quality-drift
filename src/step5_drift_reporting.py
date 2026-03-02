def classify_drift_severity(p_value):
    if p_value < 0.01:
        return "HIGH"
    elif p_value < 0.05:
        return "MEDIUM"
    else:
        return "LOW"


def generate_drift_report(drift_results):
    report = {}

    for feature, result in drift_results.items():
        p_value = float(result["p_value"])
        drift_detected = bool(result["drift_detected"])

        severity = classify_drift_severity(p_value)

        if drift_detected:
            explanation = (
                f"Significant distribution shift detected in {feature}. "
                f"Severity level: {severity}. Model reliability may be impacted."
            )
        else:
            explanation = (
                f"No significant drift detected in {feature}. "
                f"Data distribution remains stable."
            )

        report[feature] = {
            "p_value": round(p_value, 6),
            "drift_detected": drift_detected,
            "severity": severity,
            "explanation": explanation
        }

    return report
