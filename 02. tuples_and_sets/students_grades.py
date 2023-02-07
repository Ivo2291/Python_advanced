number = int(input())
students_dict = {}

for student in range(number):
    student_name, grade = input().split()

    if student_name not in students_dict:
        students_dict[student_name] = []
    students_dict[student_name].append(float(grade))

for current_student, grades in students_dict.items():
    average_grade = sum(grades) / len(grades)
    grades = [f"{grade:.2f}" for grade in grades]

    print(f"{current_student} -> {' '.join(grades)} (avg: {average_grade:.2f})")
