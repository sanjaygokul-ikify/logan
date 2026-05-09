import argparse
import json
from src.log_parser import LogParser
from src.log_analyzer import LogAnalyzer
from src.db import Database

def main():
    parser = argparse.ArgumentParser(description='logan - Automated Log Analysis')
    parser.add_argument('--log_file', help='Path to log file')
    parser.add_argument('--db_connection', help='Database connection string')
    args = parser.parse_args()

    log_parser = LogParser(args.log_file)
    log_analyzer = LogAnalyzer(log_parser.parse_logs())
    db = Database(args.db_connection)
    db.insert_logs(log_analyzer.analyze_logs())

if __name__ == '__main__':
    main()