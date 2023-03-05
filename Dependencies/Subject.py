class Subject:
    def __init__(self):
        self.subject = None
        self.subjectID = None
        self.subjectName = None
        self.lectures_per_week = None
        self.tutorials_per_week = None
        self.practicals_per_week = None
        self.subjectCredits = None

    def get_subject(self):
        self.subject = {
            "subjectID": self.subjectID,
            "subjectName": self.subjectName,
            "lecture_per_week": self.lectures_per_week,
            "tutorials_per_week": self.tutorials_per_week,
            "practicals_per_week": self.practicals_per_week,
            "subjectCredits": self.subjectCredits
        }
        return self.subject

    def set_subject(self, sID, sName, lecture, tutorial, practical, _credits):
        self.subjectID = sID
        self.subjectName = sName
        self.lectures_per_week = lecture
        self.tutorials_per_week = tutorial
        self.practicals_per_week = practical
        self.subjectCredits = _credits
