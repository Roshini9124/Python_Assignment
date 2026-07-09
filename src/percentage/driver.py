from util import student_average

def main():
    n = int(input())

    students = {}

    for i in range(n):
        entry = input().split()

        name = entry[0]

        marks = list(map(float, entry[1:]))

        students[name] = marks

    query = input()

    score = students[query]

    average = student_average(score)

    print(f"{average:.2f}")

if __name__ == "__main__":
    main()