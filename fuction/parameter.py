def introduce(name, age, grade, exam):
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))    
    exam = input("Did you take the exam? (yes/no): ").strip().lower()
    grade = int(input("Enter your grade: "))
    if exam == "yes":
        try:
            grade
        except ValueError:
            print("Invalid score. Please enter a numeric value.")
        else:
            if grade >= 90:
                grade = 'A'
                print("Excellent work!" ,{introduce})
            elif grade >= 80:
                grade = 'B'
                print("Good job!")
            elif grade >= 70:
                grade = 'C'
                print("You passed.")
            elif grade >= 60:
                grade = 'D'
                print("Just made it.")
            else:
                grade = 'F'
                print("Better luck next time.")
    else:
        print("Exam not taken. No grade assigned.")


        print(f"My name is {name}")
        print(f"I am {age} years old")
        print(f"I am in grade {grade}")

# Call with values
introduce(name="", age=0, grade=0, exam="")
