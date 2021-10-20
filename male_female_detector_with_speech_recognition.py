import speech_recognition as sr
recognizer = sr.Recognizer()
microphone = sr.Microphone()
with microphone as source:
    print("What i your name? plz speak")
    a = recognizer.adjust_for_ambient_noise(source)
    audio = recognizer.listen(source)
    response = recognizer.recognize_google(audio).lower()
name = response.capitalize()
male_names = open("male_names","r")
Write_in_males = open("male_names","a+")
female_names = open("female_names","r")
write_in_females = open("female_names","a+")

if name in male_names.read():
    print(name," You are a male")
elif name in female_names.read():
    print(name," You are a female")
else:
    if name.endswith("i") or name.endswith("a") or name.endswith("u"):
        print(name," Maybe you are a female")
        is_gender_correct = input("Is your gender correct y/n:- ")
        if is_gender_correct == "n":
            print("Thanks for your feedback we will try our best to improve ourselves")
            Write_in_males.write(name + "\n")
        else:
            print("Thanks for your feedback")
            write_in_females.write(name + "\n")
    else:
        print(name," Maybe you are male")
        is_gender_correct = input("Is your gender correct y/n:- ")
        if is_gender_correct == "n":
            print("Thanks for your feedback we will try our best to improve ourselves")
            write_in_females.write(name + "\n")
        else:
            print("Thanks for your feedback")
            Write_in_males.write(name + "\n")
