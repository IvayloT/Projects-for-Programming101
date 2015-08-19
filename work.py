#1. Да си вземем джейсън с requests
#2.Да си направим таблиците + релациите
#3.Да ходим по курсистите +вмъкване в данните
#4.Край


table = sqlite3.connect("table.db")
cursor = table.cursor()


"""course_name -> id """
course_name_to_id = {}


def create_student(student):
    insert_query = """
    INSERT INTO student(name,github)
    VALUES(?, ?)
"""


def create_course(course):
    insert_query = """
    INSERT INTO Courses(name)
    VALUES(?)
"""
cursor.execute(insert_query)

def create_relation(table, cursor, student_id, course_id):
    pass

import sqlite3
import requests
from tables import table

API_URL = "https://hackbulgaria.com/api/students/"
students = requests.get(API_URL).json()


for student in students:
    student_id = create_student(table, cursor.student)
    courses = student["courses"]

    for course in courses:
        if course in course_name_to_id:
            course_id = course_name_to_id[table, cursor, course]
        else:
            course_id = create_course(course)
            course_name_to_id[course["name"]] = course_id

        create_relation(student_id, course_id)

    """1.Insert student in database
       2.for each Courses
       3.if not in database,insert in database
       4. insert student-course raltion
"""
