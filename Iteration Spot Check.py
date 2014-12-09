# Alexander Allan
# 11/11/2014
# Iteration Spot Check

Number = 0
Total = 0

while Number is not -1:
    Number = int(input("Please enter a number: "))
    Total = Total + (Number * Number)
Total = Total - 1
print("The total is {0}.".format(Total))
