#Alexander Allan
#21/10/2014
#Iteration exercise 5

Number = 0
UnAveragedNumber = 0
RepeatTimer = 0
while Number >= 0:
    Number = int(input("Please enter one of the numbers you would like to be averaged: "))
    UnAveragedNumber = UnAveragedNumber + Number
    RepeatTimer = RepeatTimer + 1
AveragedNumber = UnAveragedNumber / RepeatTimer
print("The average number of all of the numbers you entered is {0}.".format(AveragedNumber))
