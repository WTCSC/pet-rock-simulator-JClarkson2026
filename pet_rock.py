print("Welcome to the pet rock simulator! You have a pet rock. what will you name it?")

rockName = input("> ")

def inputCorrect():
    inpVal = input("> ")
    if inpVal in ["1", "2", "3", "4"]:
        return inpVal
    else:
        print("Input failure, please try again")
        return inputCorrect()

def runTime():
    happyValue = 6
    hungerValue = 6

    while happyValue > 1 and hungerValue > 1:
        happyValue = happyValue - 1
        hungerValue = hungerValue - 1
        print(f"{rockName} has {happyValue} happiness and {hungerValue} hunger")
        print("What will you do?")
        print("1. Pet your rock\n2. Feed your rock\n3. Take a walk\n4. Quit")
        userInput = inputCorrect()
        if userInput == "1":
            happyValue = happyValue + 2
            print(f"{rockName} is got happier")
        elif userInput == "2":
            hungerValue =  hungerValue + 2
            print(f"{rockName} is less hungry")
        elif userInput == "3":
            print("You got your steps in! Good job!")
        elif userInput == "4":
            print("Goodbye!")
            break
    
    if happyValue <= 0:
        print(f"{rockName} has run away due to your neglect")
    elif hungerValue <= 0:
        print(f"{rockName} has died of hunger")
    else:
        print(f"{rockName} exploded")

runTime()