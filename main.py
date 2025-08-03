# Let's build a simple Python project to calculate and summarize student marks and grades.
# The program will:
# - Take input for student names and marks
# - Calculate total and average
# - Assign grades based on average
# - Store data for multiple students
# - Print a summary

# First, define helper functions and main execution logic

def calculate_grade(avg):
    if avg >= 90:
        return 'A'
    elif avg >= 75:
        return 'B'
    elif avg >= 60:
        return 'C'
    elif avg >= 40:
        return 'D'
    else:
        return 'F'

def summarize_students(student_data):
    summary = []
    for student in student_data:
        total = sum(student['marks'])
        avg = total / len(student['marks'])
        grade = calculate_grade(avg)
        summary.append({
            'name': student['name'],
            'total': total,
            'average': avg,
            'grade': grade
        })
    return summary

# Sample data
students = [
    {'name': 'Alice', 'marks': [85, 78, 92]},
    {'name': 'Bob', 'marks': [65, 70, 60]},
    {'name': 'Charlie', 'marks': [95, 88, 90]},
    {'name': 'David', 'marks': [40, 42, 38]},
    {'name': 'Eva', 'marks': [55, 58, 53]}
]

# Get summary
summary = summarize_students(students)
summary


print(summary)