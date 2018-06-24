import threading

class TrainingRun(threading.Thread):
    def __init__(self, thread_id, beacon_list, ):
        super().__init__()
        self.beacon_list = beacon_list
        self.thread_id = thread_id

    def run(self):
        pass