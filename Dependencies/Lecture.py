class Lecture:
    def __init__(self):
        self.lecture = {}
        self.lectureID = None
        self.subject = None
        self.room = None
        self.time = None
        self.teacher = None
        self.studentgroup = None
        self.semester = None
        self.course = None

    def get_lecture(self):
        self.lecture = {
            "course": self.course,
            "semester": self.semester,
            "subject": self.subject,
            "room": self.room,
            "teacher": self.teacher,
            "studentGroup": self.studentgroup,
            "meetingTime": self.time,
            "lectureID": self.lectureID
        }
        return self.lecture

    def set_lecture(self, lID, _course, _sem, _sub, _room, _faculty, stu_group, mTime):
        self.course = _course
        self.semester = _sem
        self.subject = _sub
        self.room = _room
        self.teacher = _faculty
        self.studentgroup = stu_group
        self.time = mTime
        self.lectureID = lID
