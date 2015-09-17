__author__ = 'torres'
#-*- coding: utf-8-*-

import ManagementSystem

###global
loopFlag = 1
instance_ManagementSystem = ManagementSystem.BookMgr() # load class instance
BooksDoc = None # loading data(DOM)

### function
def printMenu():
    print("\n =====Book Management System=====")
    print("=========Menu==========")
    print("- l : load XML data -> DOM")
    print("- p : print raw XML <- DOM")
    print("- q : quit")
    print("=======================")

def launcherFunction(menu):
    global loopFlag
    global instance_ManagementSystem
    global BooksDoc

    if menu == 'l':
        filePath = str(raw_input('-input the XML file path that you want to load : '))
        BooksDoc = instance_ManagementSystem.LoadXMLFromFile(filePath)

    elif menu == 'q':
        loopFlag = -1  # exit program
        print("quit")

    elif menu == 'p':
        instance_ManagementSystem.PrintDOMtoXML(BooksDoc)

    else:
        print("error : unknown menu key")


while(loopFlag > 0):
    printMenu()
    selectedMenu = str(raw_input('-select menu : '))
    launcherFunction(selectedMenu)
else:
    print("Thank you!")