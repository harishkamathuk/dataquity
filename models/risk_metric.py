class RiskMetric:
    def __init__(self, metric_id, risk_score):
        self.metric_id = metric_id
        self.risk_score = risk_score

    def __repr__(self):
        return f"<RiskMetric(metric_id={self.metric_id}, risk_score={self.risk_score})>"
