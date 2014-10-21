#Alexander Allan
#21/10/2014
#Iteration exercise 1-6

print("All of the values are rounded to the nearest full interger.")
print("Kg's | Pounds")
print("-------------")
for repeat in range(20):
    AlmostPounds = ((repeat + 1) * 2.2)
    Pounds = AlmostPounds // 1
    print("{0:>4} | {1:>2}".format(repeat+1,Pounds))
