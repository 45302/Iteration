#Alexander Allan
#14/10/2014
#Iteration exercise 1-4

Number = 0
for Repeat in range(8):
    Input = int(input("Please enter number {0}: ".format(Repeat + 1)))
    Number = (Number + Input)
    Input = (Input - Input)
print("The total is {0}.".format(Number))
