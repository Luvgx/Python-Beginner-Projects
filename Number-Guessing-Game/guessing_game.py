import random
print("\n===== Number Guessing Game =====")

def main(secret_number, max_range):
    attempts = 1
    while True:
        
        print("\nAttempt #", attempts)
        guess = int(input("Enter you guess : "))
        if(guess > max_range):
            print("\nInvalid input! Enter a number between 1 and", max_range, ".\nThat's why it will not count in attempts.")
            continue
        elif(guess < 1):
            print("\nInvalid input! Enter a number between 1 and", max_range, ".\nThat's why it will not count in attempts.")
            continue
        attempts += 1
        
        if(guess == secret_number):
            print("Congratulations!\nYou guessed the number in", attempts, "attempts.")
            break

        elif(guess < secret_number):
            diff1 = secret_number - guess

            if(diff1 <= 5):
                print("Very Close!")
            else:
                print("Too Low!")

        elif(guess > secret_number):
            diff2 = guess - secret_number
            if(diff2 >= 50):
                print("Far Away!")
            else:
                print("Too High!")

def game1():
    
    print("\nPlease enter a number between 1 and 50.")
    secret_number1 = random.randint(1, 50)
    main(secret_number1, 50)

def game2():
    
    print("\nPlease enter a number between 1 and 100.")
    secret_number2 = random.randint(1, 100)
    main(secret_number2, 100)

def game3():
    
    print("\nPlease enter a number between 1 and 500.")
    secret_number3 = random.randint(1, 500)
    main(secret_number3, 500)

def mode_selector():
    while True:
        print("\n---Select difficulty---")

        print("Easy(1 to 50) = e")
        print("Medium(1 to 100) = m")
        print("Hard(1 to 500) = h")
        mode = input("Enter mode: ")
        if(mode == "e"):
            game1()
            break
        elif(mode == "m"):
            game2()
            break
        elif(mode == "h"):
            game3()
            break
        else:
            print("\nInvalid mode!\nTry again.")

mode_selector()

while True:
    play_Again = input("Play Again? (y/n) : ")
    if(play_Again == "y"):
        mode_selector()
    elif(play_Again == "n"):
        print("Thanks for playing")
        break
    else:
        print("please answer in (y/n)")
    



   