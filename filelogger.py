import csv
import os
from datetime import datetime
import customexceptions

class FileLogger:
    def __init__(self, subject_name, beacon_list):
        self.time_stamp = '{timestamp:%Y%m%d_%H%M'.format(timestamp=datetime.now())
        self.file_path = 'data/{name}/{timestamp}_training.csv'.format(name=subject_name,
                                                                       timestamp=self.time_stamp)
        self.hash_line = '######'

    def write_header_info(self, subject_name, training_name, interval_time):
        """
        Writes header information (subject, training_name, timestamp)
        :param subject_name: string name of the subject
        :param training_name: name of the training
        :param interval_time: time between deactivation and activation in seconds
        :return:
        """
        with open(self.file_path, 'w') as file:
            csv_writer = csv.writer(file, delimiter=':')
            csv_writer.writerow(['subject', subject_name])
            csv_writer.writerow(['training_name'], training_name)
            csv_writer.writerow(['timestamp', self.time_stamp])
            csv_writer.writerow(['interval_time', interval_time])
            csv_writer.writerow([self.hash_line])

    def write_beacon_positions(self, beacon_list):
        """
        Writes the position of the beacons
        :param beacon_list: list with beacon objects
        :return:
        """
        with open(self.file_path, 'w+') as file:
            csv_writer = csv.writer(file, delimiter=',')
            csv_writer.writerow(['beacon_id_text', 'pos_x', 'pos_y'])
            for beacon in beacon_list:
                csv_writer.writerow([beacon.id_text])

            csv_writer.writerow([self.hash_line])

    def write_waypoint(self, beacon, time_stamp):
        """
        Writes a row with beacon_id and time when the beacon is deactivated
        :param beacon: beacon object
        :param time_stamp: time stamp of the deactivation
        :return:
        """
        with open(self.file_path, 'w+') as file:
            csv_writer = csv.writer(file, delimiter=',')
            csv_writer.writerow([beacon.id_text, time_stamp])


class FileReader():
    def __init__(self, file_path):
        self.file_path = file_path

        # check if file path exists
        if not os.path.exists(file_path):
            raise customexceptions.FileNotFoundError('Could not found file under {file_path}'.format(file_path=file_path))
        


