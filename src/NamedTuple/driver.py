from util import average_marks

n = int(input())
columns = input().split()

students = []
for _ in range(n):
    students.append(input().split())

print(average_marks(n, columns, students))