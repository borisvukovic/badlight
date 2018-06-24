import csv
from datetime import datetime

class FileLogger:
    def __init__(self, subject_name, beacon_list):

        with open('data/{name}/{timestamp:%Y%m%d_%H%M}_training.csv'.format(name=subject_name, timestamp=datetime.now())) as file:
            pass


