import names
genderChoice = input("What gender do you want your names to be? (male, female, both) ")

nameCount = int(input("How many names do you want to generate? "))

if genderChoice.lower() == "male": #creates male names

    for i in range(nameCount):
        print(names.get_full_name(gender="male"))

elif genderChoice.lower() == "female": #creates female names

    for i in range(nameCount):
        print(names.get_full_name(gender="female"))

elif genderChoice.lower() == "both": #creates non gender-specific names
    for i in range(nameCount):
        print(names.get_full_name())

elif nameCount < 0:
    print("Error, cannot print a negative amount of names")
else:
    print("Error, invalid gender")

