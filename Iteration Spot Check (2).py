# Alexander Allan
# 11/11/2014
# Iteration Spot Check (2)

TimesTableChosen = int(input("Please enter an interger: "))
print()
print("Times table for {0}:".format(TimesTableChosen))
print()
for Count in range(12):
    Multiplied = Count + 1
    Answer = (Multiplied * TimesTableChosen)
    print("{0:>2} * {1:>2} = {2:>2}".format(Multiplied,TimesTableChosen,Answer))
