# Data
Courses = [
    {
        "id": 1,
        "course": "CSE",
        "total_semesters": 8
    },
    {
        "id": 2,
        "course": "DATA SCIENCE",
        "total_semesters": 6
    },
    {
        "id": 3,
        "course": "BCA",
        "total_semesters": 6
    }
]

Teachers = [
    {
        "teacherID": "t1",
        "teacherName": "Mr.Yogesh Chaudhari",
        "teacherSubjects": ["C Programming", "OS"],
        "teacherLoad": 5,
        "assignedSubjects": ["OS"]
    },
    {
        "teacherID": "t2",
        "teacherName": "Mr.Ashish Jani",
        "teacherSubjects": ["Data Science", "Big Data"],
        "teacherLoad": 3,
        "assignedSubjects": ["Big Data"]
    },
    {
        "teacherID": "t3",
        "teacherName": "Mrs.Kriti Jaiswal",
        "teacherSubjects": ["CN", "Python", "C", "Data Structures", "DAA"],
        "teacherLoad": 6,
        "assignedSubjects": ["CN", "Python", "C"]
    },
    {
        "teacherID": "t4",
        "teacherName": "Mrs.Sushma Vankhede",
        "teacherSubjects": ["Web Tech", "SE", "GUI"],
        "teacherLoad": 4,
        "assignedSubjects": ["Web Tech", "SE", "GUI"]
    },
    {
        "teacherID": "t5",
        "teacherName": "Mr.Jaideep Raulji",
        "teacherSubjects": ["Ad Python", "Java", "AI"],
        "teacherLoad": 6,
        "assignedSubjects": ["Ad Python", "Java", "AI"]
    },
    {
        "teacherID": "t6",
        "teacherName": "Ms.Vaibhavi Patel",
        "teacherSubjects": ["TOC", "COA", "Compiler Design"],
        "teacherLoad": 5,
        "assignedSubjects": ["TOC", "Compiler Design"]
    },
    {
        "teacherID": "t7",
        "teacherName": "Ms.Naishwita Parmar",
        "teacherSubjects": ["GUI", "Web Tech", "DBMS"],
        "teacherLoad": 3,
        "assignedSubjects": ["DBMS", "Web Tech"]
    },
    {
        "teacherID": "t8",
        "teacherName": "Mr.Tejas Patel",
        "teacherSubjects": ["IS", "CS", "CN"],
        "teacherLoad": 4,
        "assignedSubjects": ["IS", "CS"]
    }
]

Rooms = [
    {
        "roomID": 501,
        "roomCapacity": 60,
        "roomAvailability": True,
        "roomType": "l"
    },
    {
        "roomID": 502,
        "roomCapacity": 60,
        "roomAvailability": True,
        "roomType": "l"
    },
    {
        "roomID": 503,
        "roomCapacity": 60,
        "roomAvailability": True,
        "roomType": "l"
    },
    {
        "roomID": 505,
        "roomCapacity": 60,
        "roomAvailability": True,
        "roomType": "l"
    },
    {
        "roomID": 303,
        "roomCapacity": 60,
        "roomAvailability": True,
        "roomType": "p"
    },
    {
        "roomID": 207,
        "roomCapacity": 30,
        "roomAvailability": True,
        "roomType": "p"
    },
    {
        "roomID": 203,
        "roomCapacity": 30,
        "roomAvailability": True,
        "roomType": "p"
    }
]

Subjects = {
    "FY": [
        {
            "subjectID": "fy1",
            "subjectName": "Maths",
            "lectures_per_week": 0,
            "tutorials_per_week": 0,
            "practicals_per_week": 0,
            "subjectCredits": 3
        },
        {
            "subjectID": "fy2",
            "subjectName": "Chemistry",
            "lectures_per_week": 3,
            "tutorials_per_week": 0,
            "practicals_per_week": 2,
            "subjectCredits": 4
        },
        {
            "subjectID": "fy3",
            "subjectName": "Python",
            "lectures_per_week": 3,
            "tutorials_per_week": 0,
            "practicals_per_week": 2,
            "subjectCredits": 4
        },
        {
            "subjectID": "fy4",
            "subjectName": "Communication skills",
            "lectures_per_week": 2,
            "tutorials_per_week": 0,
            "practicals_per_week": 0,
            "subjectCredits": 2
        },
        {
            "subjectID": "fy5",
            "subjectName": "Physics",
            "lectures_per_week": 2,
            "tutorials_per_week": 0,
            "practicals_per_week": 2,
            "subjectCredits": 4
        },
        {
            "subjectID": "fy6",
            "subjectName": "English",
            "lectures_per_week": 2,
            "tutorials_per_week": 0,
            "practicals_per_week": 0,
            "subjectCredits": 2
        },
        {
            "subjectID": "fy7",
            "subjectName": "C Programming",
            "lectures_per_week": 2,
            "tutorials_per_week": 0,
            "practicals_per_week": 2,
            "subjectCredits": 4
        }],
    "SY": [
        {
            "subjectID": "sy1",
            "subjectName": "Data Structures",
            "lectures_per_week": 2,
            "tutorials_per_week": 0,
            "practicals_per_week": 2,
            "subjectCredits": 4
        },
        {
            "subjectID": "sy2",
            "subjectName": "Theory Of Computation",
            "lectures_per_week": 2,
            "tutorials_per_week": 0,
            "practicals_per_week": 0,
            "subjectCredits": 2
        },
        {
            "subjectID": "sy3",
            "subjectName": "Computer Organisation and Architecture",
            "lectures_per_week": 2,
            "tutorials_per_week": 1,
            "practicals_per_week": 0,
            "subjectCredits": 2.5
        },
        {
            "subjectID": "sy4",
            "subjectName": "Computer Networks",
            "lectures_per_week": 2,
            "tutorials_per_week": 1,
            "practicals_per_week": 2,
            "subjectCredits": 4
        },
        {
            "subjectID": "sy5",
            "subjectName": "OOP",
            "lectures_per_week": 2,
            "tutorials_per_week": 0,
            "practicals_per_week": 2,
            "subjectCredits": 4
        }],
    "TY": [
        {
            "subjectID": "ty1",
            "subjectName": "Artificial Intelligence",
            "lectures_per_week": 2,
            "tutorials_per_week": 0,
            "practicals_per_week": 2,
            "subjectCredits": 4
        },
        {
            "subjectID": "ty2",
            "subjectName": "Compiler Design",
            "lectures_per_week": 2,
            "tutorials_per_week": 0,
            "practicals_per_week": 2,
            "subjectCredits": 4
        },
        {
            "subjectID": "ty3",
            "subjectName": "Cloud Computing",
            "lectures_per_week": 2,
            "tutorials_per_week": 0,
            "practicals_per_week": 2,
            "subjectCredits": 4
        },
        {
            "subjectID": "ty4",
            "subjectName": "Big Data Analytics",
            "lectures_per_week": 2,
            "tutorials_per_week": 0,
            "practicals_per_week": 2,
            "subjectCredits": 4
        },
        {
            "subjectID": "ty5",
            "subjectName": "CS",
            "lectures_per_week": 2,
            "tutorials_per_week": 1,
            "practicals_per_week": 2,
            "subjectCredits": 4
        },
        {
            "subjectID": "ty6",
            "subjectName": "IS",
            "lectures_per_week": 2,
            "tutorials_per_week": 1,
            "practicals_per_week": 2,
            "subjectCredits": 4
        },
        {
            "subjectID": "ty7",
            "subjectName": "JAVA",
            "lectures_per_week": 2,
            "tutorials_per_week": 1,
            "practicals_per_week": 2,
            "subjectCredits": 4
        }]
}

Semesters = [
    {
        "Year": "FY",
        "Semester": 2,
        "Subjects": Subjects["FY"],
        "Divisions": ["A", "B"],
        "Teachers": [Teachers[0], Teachers[4], Teachers[2], Teachers[7]]
    },
    {
        "Year": "SY",
        "Semester": 4,
        "Subjects": Subjects["SY"],
        "Divisions": ["A", "B"],
        "Teachers": [Teachers[1], Teachers[3], Teachers[5]]
    },
    {
        "Year": "TY",
        "Semester": 6,
        "Subjects": Subjects["TY"],
        "Divisions": ["A", "B"],
        "Teachers": [Teachers[0], Teachers[4], Teachers[2], Teachers[7], Teachers[5], Teachers[1]]
    },
]

Students = [
    {
        "Student_Group_ID": "g1",
        "Student_Group_Name": "FYCSE_A",
        "Group_Year": "FY",
        "Course_Name": "CSE",
        "Division": "A",
        "Subjects_list": Subjects["FY"]
    },
    {
        "Student_Group_ID": "g2",
        "Student_Group_Name": "FYCSE_B",
        "Group_Year": "FY",
        "Course_Name": "CSE",
        "Division": "B",
        "Subjects_list": Subjects["FY"]
    },
    {
        "Student_Group_ID": "g3",
        "Student_Group_Name": "SYCSE_A",
        "Group_Year": "SY",
        "Course_Name": "CSE",
        "Division": "A",
        "Subjects_list": Subjects["SY"]
    },
    {
        "Student_Group_ID": "g4",
        "Student_Group_Name": "SYCSE_B",
        "Group_Year": "SY",
        "Course_Name": "CSE",
        "Division": "B",
        "Subjects_list": Subjects["SY"]
    },
    {
        "Student_Group_ID": "g5",
        "Student_Group_Name": "TYCSE_A",
        "Group_Year": "TY",
        "Course_Name": "CSE",
        "Division": "A",
        "Subjects_list": Subjects["TY"]
    },
    {
        "Student_Group_ID": "g6",
        "Student_Group_Name": "TYCSE_B",
        "Group_Year": "TY",
        "Course_Name": "CSE",
        "Division": "B",
        "Subjects_list": Subjects["TY"]
    }
]

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
