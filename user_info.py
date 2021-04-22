import tts


def start():
    tts.speak("What is your Name")
    name = input("Name: ")

    tts.speak("What is your age")
    age = input("age: ")

    tts.speak("What grade/class are you in")
    grade = input("Grade/Class: ")

    return name, age, grade


def get_age_group(age: str):
    age_group = ""

    if 12 < int(age) < 20:
        age_group = "Teenager"
    elif int(age) <= 12:
        age_group = "Adolescence"
    elif int(age) >= 20:
        age_group = "Adult"
    elif int(age) >= 60:
        age_group = "Senior Citizen"

    return age_group


def tell_grade(grade: str):
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


def create_file(name: str, age: str, grade: str, age_group: str):
    file = open(name + ".txt", "x")

    file.write("Name: " + name + "\n")
    file.write("Age: " + age + "\n")
    file.write("Grade/Class: " + grade + "\n")
    file.write("You are a " + age_group + "\n")
    file.write("Your name has " + str(len(name)) + " characters")

    file.close()

    return file
