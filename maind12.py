# ------quiz game
questions= ("what is your name ?",
            "which grade are you ?",
            "which subject is your favourite ? ",
            "what is your future wish".title())
options = (("A.bereket",'B.abel ',"C. robel ","D.ermiyas") ,
           ("A.----",'B.----',"C.---","D.----"),
           ("A.----",'B.----',"C.----","D.----"),
           ("A.----",'B.----',"C.----","D.----"),)
guesses = []
question_number = 0
solutions= ("A","B","C","D")
score = 0
for question in questions:
    print("--------------------")
    print(question)
    for option in options[question_number]:
        print(option)

    guess=input("Enter (A, B, C, D) : ").upper()
    if guess == solutions[question_number]:
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
        print(f"{solutions[question_number]} is correct answer")
    guesses.append(guess)
    question_number += 1
    print(" ")

print(f"Total guesses : {guesses}")
print(f"solutions are : {solutions}")
print(f"Total score by %: {score*100/len(questions)}%")




