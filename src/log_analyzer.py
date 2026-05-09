import numpy as np

class LogAnalyzer:
    def __init__(self, logs):
        self.logs = logs

    def analyze_logs(self):
        # Analyze logs using statistical methods
        levels = [log['level'] for log in self.logs]
        messages = [log['message'] for log in self.logs]
        return {'levels': np.unique(levels), 'messages': np.unique(messages)}