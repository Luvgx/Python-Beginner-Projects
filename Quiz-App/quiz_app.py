import random
print("================================")
print("           QUIZ APP")
print("================================")
questions = [
{"question" : "Which of the following physical quantities has the same dimensional formula as work?",
    "options": ["A) Power", "B) Torque", "C) Momentum", "D) Impulse"],
    "answer": "B"
    },
{"question": "What is the molecular geometry of a methane (CH4) molecule?",
    "options": ["A) Linear", "B) Trigonal planar", "C) Tetrahedral", "D) Octahedral"],
    "answer": "C"
    },
{"question": "If a matrix A has a determinant equal to zero, what is the matrix called?",
    "options": ["A) Identity matrix", "B) Singular matrix", "C) Non-singular matrix", "D) Symmetric matrix"],
    "answer": "B"
    }
]
 
score = 0
Que_no = 0 
for question in questions:
    Que_no += 1 
    print("\nQuestion", Que_no, "/", len(questions))
    print(question['question'])

    for option in question['options']: 
        print(option)
    
    user_guess = input("Enter you answer (A/B/C/D): ").upper()
    if(user_guess == question["answer"] ):
        score += 1
        print("correct")
    elif(user_guess != question["answer"] ):
        print("incorrect")
        print("Correct answer is", question["answer"])

    print("\nYour scored", score,"/", "3")
    percentage = (score / Que_no) * 100
    print("percentage :", percentage,"%")
    if(percentage >= 50):
        print("Result: PASS!")
    else:
        print('Result: FAIL!')
    print("-----------------------------------")

    ask_Again = input("Do you want another calculation? (y/n): ").lower()
    if(ask_Again == "n"):
        break
    elif(ask_Again == "y"):
        continue
    else:
        print("Please enter y or n...")   


    
    