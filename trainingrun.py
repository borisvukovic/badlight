import threading
import arduino
import filelogger
import customexceptions

class TrainingRun(threading.Thread):
    def __init__(self, thread_id, beacon_list, subject_name, training_name, interval_time, ):
        super().__init__()
        self.beacon_list = beacon_list
        self.thread_id = thread_id

        self.logger = filelogger.FileLogger(subject_name)

    def run(self):
        """
        Run Training
        :return:
        """
        with arduino.Arduino() as ard:
            pass


