from collections import namedtuple

def average_marks(n, columns, students):
    Student = namedtuple("Student", columns)

    total = 0
    for data in students:
        student = Student(*data)
        total += int(student.MARKS)

    return f"{total / n:.2f}"