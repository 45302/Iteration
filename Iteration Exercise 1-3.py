#Alexander Allan
#20/10/2014
#Iteration exercises 1-3

UnAveragedNumber = 0
AmountOfAveragedNumbers = int(input("How many numbers need to be averaged: "))
for repeat in range(AmountOfAveragedNumbers):
    InputNumber = int(input("Please enter a number that needs to be averaged: "))
    UnAveragedNumber = (UnAveragedNumber + InputNumber)
AverageResult = UnAveragedNumber / AmountOfAveragedNumbers
print("The average of the numbers you have entered is {0}.".format(AverageResult))
