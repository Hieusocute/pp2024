class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.marks = {}

class Course:
    def __init__(self, course_id, name):
        self.course_id = course_id
        self.name = name

def input_student():
    student_id = input("Input Student ID: ")
    name = input("Name: ")
    return Student(student_id, name)

def input_course():
    course_id = input("Course ID: ")
    name = input("Course name: ")
    return Course(course_id, name)

def input_mark(students, courses):
    student_id = input("Student ID: ")
    course_id = input("Course ID: ")
    mark = float(input("Mark: "))

    student = next((s for s in students if s.student_id == student_id), None)
    course = next((c for c in courses if c.course_id == course_id), None)

    if student and course:
        student.marks[course_id] = mark
        print("Inputed Mark.")
    else:
        print("Can't find.")

def list_students(students):
    if not students:
        print("No Student.")
    else:
        print("Student List:")
        for i, student in enumerate(students, start=1):
            print(f"{i}. {student.student_id} - {student.name}")
            if student.marks:
                print("Mark (course ID - Mark): ", end="")
                for course_id, mark in student.marks.items():
                    print(f"{course_id} - {mark}", end=", ")
                print()

def list_courses(courses):
    if not courses:
        print("No Course.")
    else:
        print("Course list:")
        for i, course in enumerate(courses, start=1):
            print(f"{i}. {course.course_id} - {course.name}")

def print_summary(students, courses):
    for student in students:
        print(f"\nStudent ID: {student.student_id}")
        print(f"Name: {student.name}")
        print("Marks:")
        for course_id, mark in student.marks.items():
            print(f"{course_id} - {mark}")

# Initialize data structures
students = []
courses = []

# Example usage
student1 = input_student()
student2 = input_student()
course1 = input_course()
course2 = input_course()

students.extend([student1, student2])
courses.extend([course1, course2])

input_mark(students, courses)
list_students(students)
list_courses(courses)
print_summary(students, courses)
