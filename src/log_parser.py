import re

class LogParser:
    def __init__(self, log_file):
        self.log_file = log_file

    def parse_logs(self):
        logs = []
        with open(self.log_file, 'r') as f:
            for line in f:
                log = self.parse_log_line(line)
                if log:
                    logs.append(log)
        return logs

    def parse_log_line(self, line):
        # Parse log line using regular expressions
        pattern = re.compile(r'^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (\w+) (\w+): (.*)$')
        match = pattern.match(line)
        if match:
            return {'timestamp': match.group(1), 'level': match.group(2), 'message': match.group(4)}
        return None