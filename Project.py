# Function to calculate grade based on average marks


def calculate_grade(average):
    if average >= 90:
        return "A"
    elif average >= 75:
        return "B"
    elif average >= 60:
        return "B"
    elif average >= 40:
        return "D"
    else:
        return "F"

# Function to summarize each student's performannce
def summarize_students(students_data):
    summary = []   # List to store final summary of all student

    # Loop through each student in the list
    for student in students_data:
        # Calculate total marks by summing the subject marks 
        Total = sum(student["marks"])

        # Calculate average marks   
        average = Total / len(student["marks"])

        # Determine the grade using the above fundtion
        grade = calculate_grade(average)

        # Store the result in summary list
        summary.append({
            "Name": student["Name"],
            "Total": Total,
            "average": round(average, 2),
            "grade": grade
        })
    return summary

# Sample student data
students = [
    {"Name": "Shikha", "marks":[85, 79, 92]},
    {"Name": "Fiza", "marks":[89, 98, 68]},
    {"Name": "Avik", "marks":[84, 73, 91]},
    {"Name": "Lakhvir", "marks":[83, 79, 93]},
    {"Name": "Neeraj", "marks":[82, 77, 94]},
    {"Name": "Hartik", "marks":[88, 76, 95]},
    {"Name": "Sandeep", "marks":[83, 75, 96]},
]

# Call the summary function to process the data
summary = summarize_students(students)
summary

# Print formatted output
print("\nStudent Summary Report:")
print("{:<10} {:<6} {:<8} {:<5}".format("Name", "Total", "Average", "Grade"))

# Display each student's results
for s in summary:
    print("{:<10} {:<6} {:<8} {:<5}".format(s["Name"], s["Total"], s["average"], s["grade"]))

