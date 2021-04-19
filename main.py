import tts

age_group = ""

tts.speak("What is your Name")
name = input("Name: ")

tts.speak("What is your age")
age = input("age: ")

tts.speak("What grade/class are you in")
grade = input("Grade/Class: ")

if 12 < int(age) < 20:
    age_group = "Teenager"
elif int(age) <= 12:
    age_group = "Adolescence"
elif int(age) >= 20:
    age_group = "Adult"
elif int(age) >= 60:
    age_group = "Senior Citizen"

tts.speak("Hello " + name)
tts.speak("You are " + age + " years of age")

if int(grade) == 1:
    print("Gideon: You are in " + grade + "st")
    tts.speak_without_print("You are in first grade")
elif int(grade) == 2:
    print("Gideon: You are in " + grade + "nd")
    tts.speak_without_print("You are in second grade")
elif int(grade) == 3:
    print("Gideon: You are in " + grade + "rd")
    tts.speak_without_print("You are in third grade")
else:
    tts.speak("You are in grade " + grade)

tts.speak("You are a " + age_group)
tts.speak("Your name has " + str(len(name)) + " characters")
