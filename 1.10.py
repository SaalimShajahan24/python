N = int(input("Enter the number of students: "))

students = {}

for i in range(N):
    name = input("Enter student's name: ")
    roll_no = int(input("Enter student's roll number: "))
    total_mark = float(input("Enter student's total mark: "))
    
    students[name] = {"roll_no": roll_no, "total_mark": total_mark}

max_mark = max(students, key=lambda x: students[x]["total_mark"])

print("Student with the highest total mark:")
print("Name:", max_mark)
print("Roll No:", students[max_mark]["roll_no"])
print("Total Mark:", students[max_mark]["total_mark"])