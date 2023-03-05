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
            _course = Course()
            _course.set_Course(course['id'], course['course'], course['total_semesters'])
            course_details = _course.get_Course()
            self.courses.append(course_details['courseName'])

        # for all semesters
        for semester in data.Semesters:
            sem = Semester()
            sem.set_Semester(semester['Year'], semester['Semester'], semester['Subjects'], semester['Divisions'],
                             semester['Teachers'])
            sem_details = sem.get_Semester()
            self.semesters.append(sem_details['Semester'])

        # for all subjects
        for year in data.Subjects:
            _list = data.Subjects[year]
            for subjects in _list:
                sub = Subject()
                sub.set_subject(subjects['subjectID'], subjects["subjectName"], subjects["lectures_per_week"],
                                subjects["tutorials_per_week"], subjects["practicals_per_week"],
                                subjects["subjectCredits"])
                sub_details = sub.get_subject()
                self.subjects.append(sub_details['subjectName'])

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
        for time_id in data.Times:
            t = Timing()
            t.set_time(time_id, random.choice(data.Days), data.Times[time_id])
            time_details = t.get_time()
            self.times.append([time_details["dayOfWeek"], time_details["timeOfDay"]])

        # for random lecture
        for i in range(self.num_lectures):
            course = random.choice(self.courses)
            semester = random.choice(self.semesters)
            teacher = random.choice(self.teachers)
            subject = random.choice(self.subjects)
            room = random.choice(self.rooms)
            student_group = random.choice(self.students)
            name = str(i + 1)
            time = random.choice(self.times)
            lec = Lecture()
            lec.set_lecture(name, course, semester, subject, room, teacher, student_group, time)
            self.lectures.append(lec.get_lecture())

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
NUM_COURSE = 3
NUM_TEACH = 8
NUM_SG = 6
create_tt = TimeTable(NUM_COURSE, NUM_TEACH, NUM_SG, data.POP_SIZE)

# generate a random population
create_tt.generate_population()

# print the generated population
create_tt.print_population()
