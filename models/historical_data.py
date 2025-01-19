class HistoricalData:
    def __init__(self, data_id, date, value):
        self.data_id = data_id
        self.date = date
        self.value = value

    def __repr__(self):
        return f"<HistoricalData(data_id={self.data_id}, date={self.date}, value={self.value})>"
