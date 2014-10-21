#Alexander Allan
#21/10/2014
#Iteration exercise 2-2

message = "*"
RowsOfStars = int(input("Please enter the amount of rows of stars you want: "))
ColumnsOfStars = int(input("Please enter the amount of stars you want per row (From 1-5): "))
if ColumnsOfStars == 1:
    for repeat in range(RowsOfStars):
        print("*")
if ColumnsOfStars == 2:
    for repeat in range(RowsOfStars):
        print("**")
if ColumnsOfStars == 3:
    for repeat in range(RowsOfStars):
        print("***")
if ColumnsOfStars == 4:
    for repeat in range(RowsOfStars):
        print("****")
if ColumnsOfStars == 5:
    for repeat in range(RowsOfStars):
        print("*****")
