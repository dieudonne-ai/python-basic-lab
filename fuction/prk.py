import time

def Inserssion (Name, Age):
    Name = input("Enter your name: ")
    Age = int(input("Enter your age: "))    
    
    
    print("Hey", Name, "you are so beuatiful")
    time.sleep(2)

Inserssion(Name = "", Age = 0)

def Discussion (Discussion):
    Discussion = input("What do you want to discuss about health?: ")
    print("Wow! I like to discuss about", Discussion)
    time.sleep(2)     
Discussion(Discussion = "")

def HealthTips ():
    print("Here are some health tips for you:")
    time.sleep(2)
    tips = [
        "1. Eat a balanced diet rich in fruits and vegetables.",
        "2. Exercise regularly to maintain a healthy weight.",
        "3. Get enough sleep each night.",
        "4. Stay hydrated by drinking plenty of water.",
        "5. Avoid smoking and limit alcohol consumption."
    ]
    for tip in tips:
        print(tip)
        time.sleep(2)   
HealthTips()

def Inserssion (Name, age):
    print("It was great talking to you,", Name + "!")
    time.sleep(2)
    print("Stay healthy and take care!") 

Inserssion(Name="")

