import random
import string

upper_case = list(string.ascii_uppercase)
lower_case = list(string.ascii_lowercase)
digits = list(string.digits)
specialcharacters = list(string.punctuation)

def strengthfun(strength1):
    print("Strength :", strength1)

def lengthfun(length1):
    print("Length :",length1)

while True:
    print("\n================================")
    print("PASSWORD GENERATOR")
    print("================================")
    print("Please Answer in (y/n):-")

    upper_include = input("Uppercase : ")
    lower_include = input("Lowercase : ")
    digits_include = input("Digits : ")
    special_include = input("Special : ")

    listMain = []

    if(upper_include == "y"):
        listMain.extend(upper_case)

    if(lower_include == "y"):
        listMain.extend(lower_case)

    if(digits_include == "y"):
        listMain.extend(digits)

    if(special_include == "y"):
        listMain.extend(specialcharacters)

    if not listMain:
        print("\nPlease select at least one character type.")
        try_again = input("Do you want to try again?(y/n): ")
    
        if(try_again == "y"):
            continue
        elif(try_again == "n"):
            break
        else:
            print("Please enter y or n")
            continue

    all_characters = listMain
    password = ""


    length = int(input("\nEnter the password length : "))
    if(length <= 0):
        print("Invalid, Password length must be greater than 0.")
        continue
    
    for i in range(length):
        password += random.choice(all_characters)

    print("\n=========================")

    print("\nGenerated Password :", password)
    lengthfun(length)
    if(length <= 5):
        strengthfun("Weak")
    elif(length in range(6, 11)):
        strengthfun("Medium")
    elif(length >= 11):
        strengthfun("Strong")

    print("\n=========================")

    ask_Again = input("Do you want another password? (y/n): ")
    if(ask_Again == "n"):
        break
    elif(ask_Again == "y"):
        continue
    else:
        print("Please enter y or n...")
        