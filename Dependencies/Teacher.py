
class Teacher:
    def __init__(self):
        self.teacher = None
        self.teacherID = None
        self.teacherName = None
        self.teacherSubjects = None
        self.teacherload = None
        self.assigned_subjects = None

    def get_teacher(self):
        self.teacher = {
            "teacherID": self.teacherID,
            "teacherName": self.teacherName,
            "teacherSubjects": self.teacherSubjects,
            "teacherLoad": self.teacherload,
            "assignedSubjects": self.assigned_subjects
        }
        return self.teacher

    def set_teacher(self, tID, tName, tSubjects, tLoad, assigned_sub):
        self.teacherID = tID
        self.teacherName = tName
        self.teacherSubjects = tSubjects
        self.teacherload = tLoad
        self.assigned_subjects = assigned_sub
