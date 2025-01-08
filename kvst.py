def validate_marks(subject):
    while True:
        marks = input(f"Enter Marks in {subject}: ")
        if marks.isdigit() and 0 <= int(marks) <= 100:
            return int(marks)
        print(f"\t{marks} is Invalid Marks in {subject} - try again.")


def validate_name():
    while True:
        name = input("Enter Your Name: ").strip()
        if all(word.isalpha() for word in name.split()) and name:
            return name
        print("\tInvalid Name - try again.")


def Details():
    while True:
        sno = input("Enter Student Number: ")
        if sno.isdigit() and int(sno) >= 100:
            break
        print(f"\t{sno} is Invalid Student Number - try again.")

    name = validate_name()
    cm = validate_marks("C")
    cppm = validate_marks("C++")
    pym = validate_marks("Python")

    # Calculate total marks, percentage, and grade
    totmarks = cm + cppm + pym
    percent = (totmarks / 300) * 100
    grade = "FAIL" if cm < 40 or cppm < 40 or pym < 40 else \
        "DISTINCTION" if totmarks >= 250 else \
            "FIRST" if totmarks >= 200 else \
                "SECOND" if totmarks >= 150 else \
                    "THIRD"

    # Print the report
    print("=" * 50)
    print("STUDENT MARKS REPORT")
    print("=" * 50)
    print(f"\tStudent Number: {sno}")
    print(f"\tStudent Name: {name}")
    print(f"\tMarks in C: {cm}")
    print(f"\tMarks in C++: {cppm}")
    print(f"\tMarks in Python: {pym}")
    print("-" * 50)
    print(f"\tTotal Marks: {totmarks}")
    print(f"\tPercentage: {percent:.2f}%")
    print(f"\tGrade: {grade}")
    print("=" * 50)


Details()
