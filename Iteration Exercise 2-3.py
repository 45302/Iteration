#Alexander Allan
#29/10/2014
#Iteration exercise 2-3

message = input("Please enter a sentence or a word that you want to be printed in reverse order: ")
length = len(message)
for character in message:
    for message in range(length,-1):
        print(character)
