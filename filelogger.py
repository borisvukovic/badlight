import csv
import os
from datetime import datetime
import customexceptions


class FileLogger:
    def __init__(self, subject_name):
        self.time_stamp = '{timestamp:%Y%m%d_%H%M}'.format(timestamp=datetime.now())
        self.file_path = 'data/{name}/{timestamp}_training.csv'.format(name=subject_name.replace(' ', '_'),
                                                                       timestamp=self.time_stamp)
        os.makedirs(os.path.dirname(self.file_path), exist_ok=True)
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
            csv_writer = csv.writer(file, delimiter=',', quotechar='"')
            csv_writer.writerow(['subject', subject_name])
            csv_writer.writerow(['training_name', training_name])
            csv_writer.writerow(['timestamp', self.time_stamp])
            csv_writer.writerow(['interval_time', interval_time])
            csv_writer.writerow([self.hash_line])

    def write_beacon_positions(self, beacon_list):
        """
        Writes the position of the beacons
        :param beacon_list: list with beacon objects
        :return:
        """
        with open(self.file_path, 'a') as file:
            csv_writer = csv.writer(file, delimiter=',', quotechar='"')
            for beacon in beacon_list:
                csv_writer.writerow([beacon.id_text, beacon.pos[0], beacon.pos[1]])

            csv_writer.writerow([self.hash_line])

    def write_waypoint_row(self, beacon, time_stamp):
        """
        Writes a row with beacon_id and time when the beacon is deactivated
        :param beacon: beacon object
        :param time_stamp: time stamp of the deactivation
        :return:
        """
        with open(self.file_path, 'a') as file:
            csv_writer = csv.writer(file, delimiter=',', quotechar='"')
            csv_writer.writerow([beacon.id_text, time_stamp])


class FileReader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.hash_line = '######'

        # Check if file path exists
        if not os.path.exists(file_path):
            raise customexceptions.FileNotFoundError('Could not found file under {file_path}'.format(file_path=file_path))

    def get_data(self):
        """
        Gets data out of the file
        :return: string dictionary header, float tuple dictionary pos, string list waypoints
        """
        header_data = {}
        position_data = {}
        waypoint_data = []

        with open(self.file_path, 'r') as file:
            csv_reader = csv.reader(file, delimiter=',', quotechar='"')

            current_section = 0
            for curr_row in csv_reader:
                # Check for hash line
                if curr_row == [self.hash_line]:
                    current_section += 1
                elif current_section == 0:
                    # Header
                    header_data[curr_row[0]] = curr_row[1]
                elif current_section == 1:
                    # Position Data
                    position_data[curr_row[0]] = (float(curr_row[1]), float(curr_row[2]))
                elif current_section == 2:
                    # Waypoint Data
                    waypoint_data.append((curr_row[0], curr_row[1]))
                else:
                    break

        return header_data, position_data, waypoint_data


if __name__ == '__main__':
    class TestBeacon:
        def __init__(self, id_text, pos):
            self.id_text = id_text
            self.pos = pos

    subject = 'Boris Vukovic'
    beacon_list = [TestBeacon('beacon_A', (1, 2)), TestBeacon('beacon_B', (3.1, 4.1))]
    fl = FileLogger(subject)

    """
    fl.write_header_info(subject, '4 Ecken', 0.8)
    fl.write_beacon_positions(beacon_list)

    fl.write_waypoint_row(beacon_list[0], '{timestamp:%Y%m%d_%H%M%S}'.format(timestamp=datetime.now()))
    fl.write_waypoint_row(beacon_list[1], '{timestamp:%Y%m%d_%H%M%S}'.format(timestamp=datetime.now()))
    """

    rd = FileReader('/home/boris/dev/badlight/data/Boris_Vukovic/20180822_1606_training.csv')
    head, pos, waypoint = rd.get_data()
    print(head)
    print(pos)
    print(waypoint)
