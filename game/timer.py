import time


class Timer:

    def __init__(self, time_in_seconds):
        self.time_in_seconds = time_in_seconds
        self.time_started = None

    def start(self):
        self.time_started = time.time()
        return self

    def is_stopped(self):
        return (time.time() - self.time_started) >= self.time_in_seconds


