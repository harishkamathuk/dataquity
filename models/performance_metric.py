class PerformanceMetric:
    def __init__(self, metric_id, return_on_investment):
        self.metric_id = metric_id
        self.return_on_investment = return_on_investment

    def __repr__(self):
        return f"<PerformanceMetric(metric_id={self.metric_id}, return_on_investment={self.return_on_investment})>"
