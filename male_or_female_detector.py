name = input("What is your name? ").capitalize() # this will capitilize the input that we get from the user
male_names = open("male_names","r")#there is a file calles male_name from which i am going to read data
Write_in_males = open("male_names","a+")#No i also want to add some data in male_name also that's why created this varible
female_names = open("female_names","r")
write_in_females = open("female_names","a+")

if name in male_names.read():# making a condition that if the user name is in the file male_names
    print("You are a male")
elif name in female_names.read(): #making a elif condition that if  name is in female_names
    print("You are a female")
else:
    if name.endswith("i") or name.endswith("a") or name.endswith("u"): 
        print("Maybe you are a female")
        is_gender_correct = input("Is your gender correct y/n:- ")
        if is_gender_correct == "n":
            print("Thanks for your feedback we will try our best to improve ourselves")
            Write_in_males.write(name + "\n")
        else:
            print("Thanks for your feedback")
            write_in_females.write(name + "\n")
    else:
        print("Maybe you are male")
        is_gender_correct = input("Is your gender correct y/n:- ")
        if is_gender_correct == "n":
            print("Thanks for your feedback we will try our best to improve ourselves")
            write_in_females.write(name + "\n")
        else:
            print("Thanks for your feedback")
            Write_in_males.write(name + "\n")
#Now we end up are full project        
