# Simple CGPA Program

semester = input("Enter Semester: ")
subjects = int(input("No Of subjects: "))

total = 0

for i in range(subjects):
    name = input("Subject Name: ")
    gpa = float(input("GPA of " + name + ": "))
    
    total = total + gpa

cgpa = total / subjects

print("Semester:", semester)
print("Your CGPA is:", cgpa)