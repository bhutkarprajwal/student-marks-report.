# Student Marks Report

## Overview
This Python script collects student details, validates input data, calculates total marks, percentage, and assigns a grade based on performance.

## Features
- Validates student number (must be a number >= 100).
- Validates student name (only alphabets allowed).
- Validates subject marks (must be between 0 and 100).
- Calculates total marks, percentage, and assigns a grade.
- Displays a structured marks report.

## Grading Criteria
- **Distinction:** Total marks ≥250
- **First Class:** Total marks ≥200
- **Second Class:** Total marks ≥150
- **Third Class:** Total marks <150
- **Fail:** If marks in any subject are below 40

## How to Run the Script
1. Ensure you have Python installed (Python 3 recommended).
2. Save the script as `student_marks.py`.
3. Run the script using:
   ```sh
   python student_marks.py
   ```
4. Follow the on-screen prompts to enter student details and view the report.

## Example Output
```
==================================================
STUDENT MARKS REPORT
==================================================
	Student Number: 101
	Student Name: John Doe
	Marks in C: 85
	Marks in C++: 78
	Marks in Python: 90
--------------------------------------------------
	Total Marks: 253
	Percentage: 84.33%
	Grade: DISTINCTION
==================================================
```

## License
This project is open-source and available for modification and distribution.


