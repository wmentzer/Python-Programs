# Asks user for a number and responds with either odd or even
run = int

while (run != 0):
    num = input("Please enter a number: ")

    if int(num) % 2 == 0:
        print(num + " is even")
    else:
        print(num + " is odd")
    print("Would you like to try again?")
    run = input("If yes, enter 1, if no, enter 0: ")
    
