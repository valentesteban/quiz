print("Welcome to my quiz!")

questionToStart = input("Do you want to play the game?: ")

if(questionToStart != "yes"):
    quit()

print("Okey! Now let's play..")
score = 0

questionOne = input("What is the name of the first president of Argentina? ")
if questionOne == "bartolome mitre":
    print("Correct!")
    score += 1
else:
    print("Incorrect.. Next question")

questionTwo = input("How many secondary colors exist?: ")
if questionTwo == str(3):
    print("Correct!")
    score += 1
else:
    print("Incorrect.. Next question")

questionThree = input("How many people exist on the world?: ")
if questionThree == "8 billion":
    print("Correct!")
    score += 1
else:
    print("Incorrect.. Next question")

print("Thanks for playing my quiz!")
print("You got " + str((int(score / 3) * 100)) + "%" " of questions correct.")





