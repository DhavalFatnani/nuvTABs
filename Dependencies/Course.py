class Course:
    def __init__(self, courseID, courseName, coursePeriod):
        self.course = None
        self.courseID = None
        self.courseName = None
        self.coursePeriod = None

    def get_Course(self):
        self.course = {
            "courseID": self.courseID,
            "courseName": self.courseName,
            "coursePeriod": self.coursePeriod
        }
        return self.course

    def set_Course(self, cID, cName, cPeriod):
        self.courseID = cID
        self.courseName = cName
        self.coursePeriod = cPeriod