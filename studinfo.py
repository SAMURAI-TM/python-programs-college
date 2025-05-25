# Get the number of students
n = int(input("Enter the number of students: "))

# Initialize an empty list to store student information
students = []

# Input student info for each student
for _ in range(n):
    student_data = input("Enter student info (name roll_no marks): ")
    student_info = student_data.split()
    students.append({
        "name": student_info[0],
        "roll_no": int(student_info[1]),
        "marks": float(student_info[2])  # Assuming marks are floating-point numbers
    })

# Print the student information
for student in students:
    print(f"Name: {student['name']}, Roll No: {student['roll_no']}, Marks: {student['marks']}")
