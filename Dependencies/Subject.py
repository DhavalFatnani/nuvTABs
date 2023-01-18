class Subject:
    def __init__(self):
        self.subject = None
        self.subjectID = None
        self.subjectName = None
        self.lecture = None
        self.tutorial = None
        self.practical = None
        self.credits = None

    def get_subject(self):
        self.subject = {
            "subjectID": self.subjectID,
            "subjectName": self.subjectName,
            "lecture_per_week": self.lecture,
            "tutorials_per_week": self.tutorial,
            "practicals_per_week": self.practical,
            "subjectCredits": self.credits
        }
        return self.subject

    def set_subject(self, sID, sName, l, t, p, c):
        self.subjectID = sID
        self.subjectName = sName
        self.lecture = l
        self.tutorial = t
        self.practical = p
        self.credits = c
