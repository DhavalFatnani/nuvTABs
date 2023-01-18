class Timing:
    def __init__(self):
        self.time = None
        self.timeID = None
        self.dayOfWeek = None
        self.timeOfDay = None

    def get_time(self):
        self.time = {
            "timeID": self.timeID,
            "dayOfWeek": self.dayOfWeek,
            "timeOfDay": self.timeOfDay
        }
        return self.time

    def set_time(self, tid, dow, tod):
        self.timeID = tid
        self.dayOfWeek = dow
        self.timeOfDay = tod