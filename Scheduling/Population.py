from Dependencies.Subject import Subject
from Dependencies.Course import Course
from Dependencies.Timing import Timing
from Dependencies.Room import Room
from Dependencies.Lecture import Lecture
from Dependencies.Teacher import Teacher
from Dependencies.StudentGroup import StudentGroup as SG
from Dependencies.Semester import Semester
import DATA as data
import random

# Data

Times = [
    ["t1", ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"], "09:00 - 10:00"],
    ["t2", ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"], "10:00 - 11:00"],
    ["t3", ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"], "11:00 - 12:00"],
    ["t4", ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"], "12:00 - 01:00"],
    ["t5", ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"], "02:00 - 03:00"],
    ["t6", ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"], "03:00 - 04:00"],
    ["t7", ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"], "04:00 - 05:00"],
    ["t8", ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"], "05:00 - 06:00"]
]


class TimeTable:
    def __init__(self, num_courses, num_teachers, num_student_groups, num_lectures):
        self.lectureID = 0
        self.lectures = []
        self.population = []
        self.courses = []
        self.teachers = []
        self.rooms = []
        self.semesters = []
        self.students = []
        self.subjects = []
        self.times = []
        self.num_courses = num_courses
        self.num_lectures = num_lectures
        self.num_teachers = num_teachers
        self.num_students_groups = num_student_groups

    def generate_population(self):
        # for all courses
        for course in data.Courses:
            self.courses.append(course["course"])

        # for all semesters
        for semester in data.Semesters:
            self.semesters.append(semester["Semester"])

        # for all students
        for year in data.Subjects:
            for s in year:
                sub = Subject()
                sub.set_subject(s["subjectID"], s["subjectName"], s["lecture_per_week"], s["tutorials_per_week"],
                                s["practicals_per_week"], s["subjectCredits"])
                sub_details = sub.get_subject()
                self.subjects.append(sub_details[s])

        # generate random teachers
        for teacher in data.Teachers:
            teach = Teacher()
            teach.set_teacher(teacher["teacherID"], teacher["teacherName"], teacher["teacherSubjects"],
                              teacher["teacherLoad"], teacher["assignedSubjects"])
            teacher_details = teach.get_teacher()
            self.teachers.append(teacher_details["teacherName"])

        # for random Rooms
        for room in data.Rooms:
            r = Room()
            r.set_Room(room["roomID"], room["roomCapacity"], room["roomAvailability"], room["roomType"])
            r_details = r.get_Room()
            self.rooms.append(r_details["roomID"])

        # for random student groups
        for studentGroup in data.Students:
            s = SG()
            s.set_StudentGroup(studentGroup["Student_Group_ID"], studentGroup["Student_Group_Name"],
                               studentGroup["Group_Year"], studentGroup["Course_Name"], studentGroup["Division"],
                               studentGroup["Subjects_list"])
            sg_details = s.get_StudentGroup()
            self.students.append(sg_details["Student_Group_Name"])

        # for random timing--
        for time in Times:
            t = Timing()
            t.set_time(time[0], random.choice(time[1]), time[2])
            time_details = t.get_time()
            self.times.append(time_details["dayOfWeek"])
            self.times.append(time_details["timeOfDay"])

        # for random lecture
        for i in range(self.num_lectures):
            course = random.choice(self.courses)
            semester = random.choice(self.semesters)
            subject = random.choice(self.subjects)
            room = random.choice(self.rooms)
            teacher = random.choice(self.teachers)
            student_group = random.choice(self.students)
            name = str(i + 1)
            time = random.choice(self.times)
            l = Lecture()
            l.set_lecture(name, course, semester, subject, room, teacher, student_group, time)
            self.lectures.append(l.get_lecture())

    def print_population(self):
        for lecture in self.lectures:
            print("Lecture: ", lecture["lectureID"])
            print("Course: ", lecture["course"])
            print("Semester: ", lecture["semester"])
            print("Subjects: ", lecture["subject"])
            print("Room: ", lecture["room"])
            print("Teacher: ", lecture["teacher"])
            print("Student Group: ", lecture["studentGroup"])
            print("Time: ", lecture["meetingTime"])
            print("--------------------------------------\n\n")


# create a new TimeTableGenerator with 10 lectures, 5 teachers, 3 student groups and 20 students per group
ttg = TimeTable(10, 5, 3, 3)

# generate a random population
ttg.generate_population()

# print the generated population
ttg.print_population()
