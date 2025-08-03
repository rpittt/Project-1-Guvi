# 📊 Student Marks Summary & Grading System

This Python project is designed to process student marks, calculate their total and average scores, and assign grades based on their performance. It takes multiple students' data as input and provides a summarized report of each student’s performance.

---

## 📁 Project Structure

```
📦 student-grading-system/
├── student_grades.py       # Main script file containing the functions
├── README.md               # This file
```

---

## 🚀 Features

- Takes input as a list of student names with their marks.
- Calculates:
  - Total marks
  - Average marks (rounded to 2 decimal places)
  - Grade based on average
- Displays a well-formatted summary report for all students.

---

## 🧠 Grading Logic

| Average Marks | Grade |
|---------------|-------|
| 90 and above  | A     |
| 75 - 89       | B     |
| 60 - 74       | B     |
| 40 - 59       | D     |
| Below 40      | F     |

> 🔁 Note: Both 75-89 and 60-74 currently return grade "B". You can modify the logic in `calculate_grade()` to distinguish them further if needed.

---

## 📌 Requirements

- Python 3.6 or above

No external libraries required. Pure Python used.

---

## ▶️ How to Run

1. **Clone the repository**  
   ```bash
   git clone https://github.com/yourusername/student-grading-system.git
   cd student-grading-system
   ```

2. **Run the script**
   ```bash
   python student_grades.py
   ```

---

## ✅ Sample Output

```
Student Summary Report:
Name       Total  Average  Grade
Shikha     256    85.33    B    
Fiza       255    85.0     B    
Avik       248    82.67    B    
Lakhvir    255    85.0     B    
Neeraj     253    84.33    B    
Hartik     259    86.33    B    
Sandeep    254    84.67    B    
```

---

## 🛠 Future Improvements

- Accept user input via command line or UI
- Export summary report to CSV or Excel
- Implement finer grading system (e.g., A+, B+)

---

## 👨‍💻 Author

**Arpit Dhuriya**  
[GitHub](https://github.com/rpittt).
