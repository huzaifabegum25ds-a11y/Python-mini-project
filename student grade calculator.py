print("===== Student Grade Calculator =====")

name = input("Enter student name: ")
marks = float(input("Enter marks (0-100): "))

if marks >= 90:
    grade = "A"
elif marks >= 75:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks >= 50:
    grade = "D"
else:
    grade = "F"

print("\n===== Result =====")
print("Student:", name)
print("Marks:", marks)
print("Grade:", grade)
