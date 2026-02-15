exam = input("Did you take the exam? (yes/no): ").strip().lower().upper()

if exam == "yes":
    try:
        score = int(input("Enter your score: "))
    except ValueError:
        print("Invalid score. Please enter a numeric value.")
    else:
        if score >= 90:
            grade = 'A'
            print("Excellent work!")
        elif score >= 80:
            grade = 'B'
            print("Good job!")
        elif score >= 70:
            grade = 'C'
            print("You passed.")
        elif score >= 60:
            grade = 'D'
            print("Just made it.")
        else:
            grade = 'F'
            print("Better luck next time.")
else:
    print("Exam not taken. No grade assigned.")