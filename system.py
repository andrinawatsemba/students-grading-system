def calculate_grade(marks):
    """Calculates the letter grade based on the given marks."""
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    else:
        return "F"

# Predefined list of subjects for each student
subjects = ["discreate math", "fundermentals of computing", "structured programing", "old testament", "writting and study skills"]

# Lists to store student data
student_names = []
student_subjects = []  # This will be a list of subjects for each student (same for all)
student_marks = []
student_grades = []

while True:
    name = input("Enter student's name (or 'finish' to quit): ")
    if name.lower() == 'finish':
        break  # Break out of the loop if 'finish' is entered for the name

    marks_for_student = []
    grades_for_student = []

    # Loop through predefined subjects and ask for marks
    for subject in subjects:
        while True:
            try:
                marks = int(input(f"Enter marks for {subject}: "))
                if marks < 0 or marks > 100:
                    print("Invalid marks! Please enter marks between 0 and 100.")
                    continue  # Go back to asking for marks again
                marks_for_student.append(marks)
                grades_for_student.append(calculate_grade(marks))
                break  # Exit the inner loop when valid marks are entered
            except ValueError:
                print("Invalid input! Please enter numeric marks.")

    # Store student data
    student_names.append(name)
    student_subjects.append(subjects)  # Store the same list of subjects for every student
    student_marks.append(marks_for_student)  # Store the marks entered for the student
    student_grades.append(grades_for_student)  # Store grades based on the marks

    print(f"Student: {name}, Marks: {marks_for_student}, Grades: {grades_for_student}")

# Display all students' data
print("\n--- Summary of Students' Grades ---")
for i in range(len(student_names)):
    print(f"\nStudent: {student_names[i]}")
    for j in range(len(student_subjects[i])):
        print(f"  {student_subjects[i][j]}: Marks = {student_marks[i][j]}, Grade = {student_grades[i][j]}")
