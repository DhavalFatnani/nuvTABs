class Semester:
    def __init__(self):
        self.semester = None
        self.year = None
        self.sem = None
        self.subjects = None
        self.divisions = None
        self.teachers = None

    def get_Semester(self):
        self.semester = {
            "Year": self.year,
            "Semester": self.sem,
            "Subjects": self.subjects,
            "Divisions": self.divisions,
            "Teachers": self.teachers
        }
        return self.semester

    def set_Semester(self, _year, _sem, sub_list, div_list, teacher_list):
        self.year = _year
        self.sem = _sem
        self.subjects = sub_list
        self.divisions = div_list
        self.teachers = teacher_list
