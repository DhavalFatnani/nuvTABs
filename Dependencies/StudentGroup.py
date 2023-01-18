class StudentGroup:
    def __init__(self):
        self.studentgroup = None
        self.sgroupID = None
        self.sgroupName = None
        self.year = None
        self.courseName = None
        self.division = None
        self.subjects = None

    def get_StudentGroup(self):
        self.studentgroup = {
            "Student_Group_ID": self.sgroupID,
            "Student_Group_Name": self.sgroupName,
            "Group_Year": self.year,
            "Course_Name": self.courseName,
            "Division": self.division,
            "Subjects_list": self.subjects
        }
        return self.studentgroup

    def set_StudentGroup(self, sgID, sgName, sgyear, sgcName, sgdiv, sgsub_list):
        self.sgroupID = sgID
        self.sgroupName = sgName
        self.year = sgyear
        self.courseName = sgcName
        self.division = sgdiv
        self.subjects = sgsub_list
