import numpy as np
from sklearn.metrics import accuracy_score

def monitor_model_performance(
        model,
        x_new,
        y_new,
        baseline_metrics,
        accuracy_drop_threshold=0.10,
        confidence_threshold=0.80

):
    """
    Monitors model performance against baseline metrics."""
    #predictions
    preds=model.predict(x_new)
    probabilities=model.predict_proba(x_new)
    #metrics
    current_accuracy=accuracy_score(y_new,preds)
    current_confidence=np.max(probabilities,axis=1).mean()

    performance_report = {
        "current_accuracy": round(current_accuracy, 4),
        "current_avg_confidence": round(current_confidence, 4),
        "accuracy_decay": False,
        "confidence_decay": False
    }
    #accuracy decay
    if current_accuracy<(1 - accuracy_drop_threshold)*baseline_metrics["accuracy"]:
        performance_report["accuracy_decay"]=True
    if current_confidence < confidence_threshold:
        performance_report["confidence_decay"]=True
    return performance_report

