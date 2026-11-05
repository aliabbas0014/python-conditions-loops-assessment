
# Student Scholarship Eligibility System

print("========================================")
print("     STUDENT SCHOLARSHIP SYSTEM")
print("========================================")

# Collect student information
student_name = input("Enter student name: ").strip()

# Validate academic marks
while True:
    try:
        marks = float(input("Enter academic marks (0-100): "))

        if 0 <= marks <= 100:
            break
        else:
            print("Marks must be between 0 and 100.")

    except ValueError:
        print("Please enter valid numeric marks.")

# Validate attendance
while True:
    try:
        attendance = float(input("Enter attendance percentage (0-100): "))

        if 0 <= attendance <= 100:
            break
        else:
            print("Attendance must be between 0 and 100.")

    except ValueError:
        print("Please enter a valid percentage.")

# Validate monthly family income
while True:
    try:
        family_income = float(input("Enter monthly family income (Rs.): "))

        if family_income >= 0:
            break
        else:
            print("Income cannot be negative.")

    except ValueError:
        print("Please enter a valid income.")

# Check eligibility conditions
reasons = []

if marks < 80:
    reasons.append("Academic marks are below 80%.")

if attendance < 85:
    reasons.append("Attendance is below 85%.")

if family_income > 50000:
    reasons.append("Family income exceeds Rs. 50,000.")

# Display evaluation report
print("\n========================================")
print("       SCHOLARSHIP EVALUATION REPORT")
print("========================================")

print("Student Name:", student_name)
print("Academic Marks:", marks, "%")
print("Attendance:", attendance, "%")
print("Monthly Family Income: Rs.", family_income)

print("----------------------------------------")

if len(reasons) == 0:

    print("Eligibility Status: Eligible")

    if marks >= 90:
        print("Scholarship Type: Full Scholarship")

    elif marks >= 80:
        print("Scholarship Type: Partial Scholarship")

else:
    print("Eligibility Status: Not Eligible")
    print("Reasons for Ineligibility:")

    for reason in reasons:
        print("-", reason)

print("========================================")
print("Evaluation Completed")
print("========================================")

