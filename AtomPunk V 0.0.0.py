import time
import random

##variables
logCount = 0
logCollectionRate = 0.5
activity = []
woodCount = 0
woodCuttingRate = 1
menuToken = 1
forestToken = 1
logToken = 1

##global
##tutorial functions
def tutMenu():
    global menuToken
    global forestToken
    print("1. go to forest")
    print("2. go to town")
    print("3. go to river")
    if menuToken == 1:
        print("this is the menu, you'll be able to access it by pressing the m button, you can use it to travel places")
        print("let's go to the forest!")
    if logToken == 0:
        print("great job!")
        print("now we have to cut these trees into logs")
    menuInput = input()
    menuToken = menuToken-1
    if menuInput == "1":
        tutForest()
    if menuInput == "2":
        print("unaviable")
        tutMenu()
    if menuInput == "3":
        print("unaviable")
        tutMenu()
def tutForest():
    global forestToken
    print("1. cut down trees")
    print("2. cut logs")
    print("press m to go to menu")
    if forestToken == 1:
        print("we need to cut down some trees first")
    if forestToken == 0:
        print("great job! now we need to cut those logs into wood!")
    forestInput = input()
    forestToken = forestToken-1
    if forestInput == "1":
        tutLogCollection()
    if forestInput == "2":
        tutLogCutting()
    if forestInput == "m":
        tutMenu()
def tutLogCollection():
    global logToken
    print("Press enter to cut down a tree! later on you can upgrade and even automate the process! Press '1' to exist once you have five logs.")
    while True:
        global logCount
        user_input = input()
        logToken = logToken-1
        if user_input == "1":
            user_input = 0
            tutForest()
        elif user_input == "m":
            tutMenu()
        else:
            logCount = logCount + (1*logCollectionRate)
            print("Timber! you now have:", logCount, "logs.")
def tutLogCutting():
    global logCount
    global woodCount
    print("Cutting logs is a lot like cutting trees! Cut all your logs and then press '1' to exit.")
    print("Logs in inventory:", logCount)
    while True:
       
        user_input = input()
        if user_input == "1":
            tutForest()
        else:
            if logCount < 1:
                print("you don't have any logs to cut silly!")
                tutForest()
            logCount = logCount - 1
            woodCount = woodCount +1
            print("chop! you have", logCount, "logs left, and", woodCount, "pieces of wood!")
            
    
##atompunk
print("welcome to the wastelands")
print("press enter to continue")
start = input()
print("you've just awoken in a barren wasteland, you can't remember how you got here, or anything really. You look around you, there's not much though, to your west there's a forest of dead tress, to your east there is what looks to be the ruins of a suburbean neighbourhood. You can hear running water nearby.")
print("enter y to start tutorial")
tutorialTrue = input()
    
if tutorialTrue == "y":
    print("welcome to the tutorial, to start, let's show you around")
    tutMenu()

    
    
