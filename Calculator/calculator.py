#Usefull functions:-
def add(num1, num2):
    result1 = num1 + num2
    show_result(result1)
    return
def sub(num1, num2):
    result2 = num1 - num2
    show_result(result2)
    return
def multi(num1, num2):
    result3 = num1 * num2
    show_result(result3)
    return
def divide(num1, num2):
    if(num2 == 0):
        print()
        print("========== ERROR! ==========")
        print("Cannot divide by zero!")
        print("============================")
        print()
    else:
        result4 = num1 / num2
        show_result(result4)
    return
def power(num1, num2):
    result5 = num1 ** num2
    show_result(result5)
    return
def modulus(num1, num2):
    if(num2 == 0):
        print()
        print("========== ERROR! ==========")
        print("Cannot divide by zero!\nSo modulus is not possible!")
        print("============================")
        print()
    else:
        result6 = num1 % num2
        show_result(result6)
        return
def show_result(result):
    print()
    print("========== RESULT ==========")
    print("Result =", result )
    print("============================")
    print()
    return

#Main content:-
while True:
    print("\n     ====Calculator====       ")
    print()
    print("Q.Which operation you want to take...")
    print("Addition(+)")
    print("Substraction(-)")
    print("Mutiplicatio(*)")
    print("Division(/)")
    print("Power(**)")
    print("Modulus(%)")
    print("Exit(e)")
    print()
    choice = input("Choose an option: ")
    if(choice == "e"):
            print("Thank you for using the calculator!\nGood bye!")
            break
    
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if(choice == "+"):
         add(num1, num2)
        
    elif(choice == "-"):
         sub(num1, num2)
        
    elif(choice == "*"):
         multi(num1, num2)
        
    elif(choice == "/"):
         divide(num1, num2)

    elif(choice == "**"):
         power(num1, num2)

    elif(choice == "%"):
         modulus(num1, num2)

    else:
        print("Please select a right operation!")

    print("----------------------------------------")

    ask_Again = input("Do you want another calculation? (y/n): ")
    if(ask_Again == "n"):
         break
    elif(ask_Again == "y"):
         continue
    else:
         print("Please enter y or n...")

         
    
