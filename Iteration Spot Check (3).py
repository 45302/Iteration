# Alexander Allan
# 11/11/2014
# Iteration Spot Check (3)

Guessed = "False"
Number = 36 #Don't know how to randomise
NumberOfTurns = 0
while Guessed is "False":
    UsersGuess = int(input("Enter your guess for the number: "))
    if UsersGuess is Number:
        Guessed = "True"
    elif UsersGuess > Number:
        print("The number you guessed is too high.")
    else:
        print("The number you guessed was too low.")
    NumberOfTurns = (NumberOfTurns + 1)
print()
print("You took {0} turns to guess the number.".format(NumberOfTurns))
print()
print("The number was {0}.".format(Number))
