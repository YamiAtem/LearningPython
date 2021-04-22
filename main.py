from read_file import read_file_info
from user_info import *
import tts

name, age, grade = start()
age_group = get_age_group(age)

tts.speak("Hello " + name)
tts.speak("You are " + age + " years of age")

tell_grade(grade)

tts.speak("You are a " + age_group)
tts.speak("Your name has " + str(len(name)) + " characters")

file = create_file(name, age, grade, age_group)

read_file_info(name + ".txt")
