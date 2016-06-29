# this program is help you to create New Year cards for friends
def happyNewYear():
    # make an empty list for future use
    nameList = list()
    while(True):
        name = requestString("Please enter a name or enter 'done' to finish")
        # let the user to stop the loop
        if name == "done": break
        # append the names to the end of the list
        nameList.append(name)
    # use for loop to print each name and "Happy New Year"
    for friend in nameList:
        print friend, ", Happy New Year!"		

# this program is simply demonstrate all kinds of list-manipulated methods
def listOperations():
    choice = requestString("Choose from add, multiply,delete,slice,count,or sort")
    a = ["a","b","c"]
    b = ["1","2","3"]
    print "a", a
    print "b", b
    if choice == "add":
        add(a,b)
    elif choice == "multiply":
        multiply(a)
    elif choice == "delete":
        delete(b)
    elif choice == "slice":
        slice(a+b)
    elif choice == "count":
        count(a)
    elif choice == "sort":
        sort(a+b)
    
def add(x,y):
    print "a+b: ", x + y
    
def multiply(x):
    print "a*3: ", x * 3
    
def delete(x):
    del x[0]
    print "b remove the first element: ", x

def slice(x):
    print "a+b", x
    print "a+b from 3rd to 5th element: ", x[2:5]

def split(x):
    print "a+b", x
    print x.split(",")
    
def count(x):
    print "the number of 'a' in the list a is", x.count("a")
    
def sort(x):
    x.sort()
    print "a+b after sorted: ", x
    
# these two programs are to calculate average of numbers that user enters
# the first program is using list-related method 
def average1():
    # make an empty list
    numberlist = list()
    # use while loop to collect numbers 
    while(True):
        input = raw_input("Enter a number to calculate average or enter 'done' to stop: ")
        # give users the choice to stop the calculation
        if input == "done": break
        # convert strings to float numbers to do division
        value = float(input)
        numberlist.append(value)
    average = sum(numberlist) / len(numberlist)
    print "Average is ", average
	
# the second one is only use variables and auto-increments
def average2():
# make two variables to do increment later
    total = 0
    count = 0
    while(True):
        input = raw_input("Enter a number to calculate average or enter 'done' to stop: ")
        if input == "done": break
        value = float(input)
        total = total + value
        count = count + 1
    average = total / count
    print "Average is ", average

# this program is an updated version of Mad Lib Games 
# please use animal=mouse,food=soysauce,person=soldier,verb=jump to run the myStory function
# 1st run myStory, then replaceWord, at last use readFile to check out the result
# myStory function is to create a Mad Lib story
def myStory(filePath,animal, food, person, verb):
    line1 = "Once upon a time, there was a " + person + ","
    line2 = " who was the bodyguard for a " + animal + "."
    line3 = "The " + animal + " loves to eat Mcdonalds cheeseburger, pina coladas mixed with " + food + ","
    line4 = "although it will feast on nearly anything sweet. "
    line5 = "The " + person + " admires the " + animal
    line6 = " because it can " + verb + " to unbelievable levels and rock his(her) world."
    print line1 + line2
    print line3 + line4
    print line5 + line6
    handle = open(filePath,"wt")
    handle.write(line1)
    handle.write(line2)
    handle.write("\n")
    handle.write(line3)
    handle.write(line4)
    handle.write("\n")    
    handle.write(line5)
    handle.write(line6)
    handle.close()

# replace two words and let users to put their own words, food and verb
# use .find() and .write() methods         
def replaceWord(filePath,newPath,food,verb):
    handle = open(filePath,"rt")
    content = handle.read()
    handle.close()
    pos1 = content.find("soysauce")
    len1 = len("soysauce")
    pos2 = content.find("jump")
    len2 = len("jump")
    handleNew = open(newPath,"wt")
    # copy the content right before the word "soysauce"
    handleNew.write(content[:pos1])
    # add the new food argument
    handleNew.write(food)
    # skip the replaced word and continue to copy the rest till the word "jump"
    handleNew.write(content[pos1+len1:pos2])
    # add the new verb argument
    handleNew.write(verb)
    # skil the replaced word and continue to copy the rest till the end
    handleNew.write(content[pos2+len2:])
    handleNew.close()
    
# make sure to pass the new file path into the function   
# readFile function is to help user to read and print the files
def readFile(filePath):
    handle = open(filePath,"rt")
    lines = handle.read()
    print lines
    handle.close()    
    
# This program is to make a simple and searchable inventory
# using the same structure of the phonebook program from textbook.
# create the text inventory 
def inventoryRawData():
    return"""
Hopewell, Inc.:Port Moody:BC:hopewell@emcp.net:404-555-0106
Bryna Corporation:Champaign:IL:brynacorp@emcp.net:217-555-0162
Bayside Supplies:Bellingham:WA:bside@emcp.net:202-555-0184
Langley Company:Burnaby:BC:langley@emcp.net:404-555-0187
Sound Products:Seattle:WA:ssupplies@emcp.net:202-555-0199"""

# double split, first use "\n" as the delimiter to create the main list
def structuredText():
    inventory = inventoryRawData()
    list = inventory.split("\n")
    newList = []
    for i in list:
        # then use ":" as the delimiter to make sub lists under the main list
        newList = newList + [i.split(":")]
    # remove first element which is a blank list
    del newList[0]
    return newList
    

def search(input):
# in this program, you can search any items from the five variables
# using if X 1 and elif X 4 to search through each index value of those sub lists
    for list in structuredText():
        if input == list[0]:
            city = list[1]
            state = list[2]
            email = list[3]
            number = list[4]
            print "The email and number for ", input, "in", city,state,"is", email, "and", number
        elif input == list[1]:
            companyName = list[0]
            state = list[2]
            email = list[3]
            number = list[4]
            print "The email and number for ", companyName, "in", input, state,"is", email, "and", number
        elif input == list[2]:
            companyName = list[0]
            city = list[1]
            email = list[3]
            number = list[4]
            print "The email and number for ", companyName, "in", city, input,"is", email, "and", number
        elif input == list[3]:
            companyName = list[0]
            city = list[1]
            state = list[2]
            number = list[4]
            print "The email and number for ", companyName, "in", city, state,"is", input, "and", number
        elif input == list[4]:
            companyName = list[0]
            city = list[1]
            state = list[2]
            email = list[3]
            print "The email and number for ", companyName, "in", city, state,"is", email, "and", input
    
