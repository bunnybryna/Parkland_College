# this program is to show how to concatenate strings with integers and use variables to do simple math
def car():
    cars = 30
    space_in_a_car = 4
    drivers = 10
    passengers = 35
    # these variables are integers, can do +-*/ directly
    cars_not_driven = cars - drivers
    cars_driven = drivers
    carpool_capacity = cars_driven * space_in_a_car
    average_passengers_per_car = passengers / cars_driven
    #  concatenate string and integer useing "," instead of "+"
    print "There are", cars, "cars avaialbe."
    print "There are only", drivers, "drivers available."
    print "There will be", cars_not_driven, "empty cars today."
    print "We can transport", carpool_capacity, "people today."
    print "We have", passengers, "people to carpool today."
    print "We need to put more than", average_passengers_per_car, "in each car."
    
    # this program is similar to program 13 which is multiplying strings to create shapes
def footprint():
    dot = ". "
    toe1 = "o"
    toe2 = "O"
    paren1 = "("
    paren2 = ")"
    slash = "/"
    backslash = "\\"
    forwardslash = "/"
    underscore = "_"
    print toe1 * 3, toe2, dot * 13
    print paren1, dot * 4, paren2, dot * 3, toe2, toe1 * 3, dot * 3
    print dot, backslash, dot * 2, paren1, dot * 4, paren1, dot * 4, paren2, dot * 3
    print dot * 2, backslash, underscore, paren2, dot * 5, paren2, dot * 2, slash, dot * 4
    print dot * 11, paren1, underscore, slash, dot * 5
    print "Bryna can draw with codes!"
    
# this program is to use for loop to count numbers
def countNum():
    # 1st for loop, i=1,2,3,4,5
    count = [1, 2, 3, 4, 5]
    for i in count:
        print "This is count %d." % i
    # 2nd for loop using "range" method, i=0~5
    for i in range(0,6):
        print "Adding %d to the total, we have %d. " % (i, i+5) 
    pet = ["dogs", "cats", "horses"]
    # 3rd for loop, i=strings 
    for i in pet:
        print "One type of my pets: %s." % i
        print "I have 10 %s, " % i 
    print "In total, I have 30 pets."
    
# this program is to practice using if function to make simple statement
def ifFunction():
    numberStr = requestString("Hey, Sean!  Please enter a number: ")
    # to convert a string to an integer
    numberInt = int(numberStr)
    if numberInt == 0:
        print "Ah, you entered zero."
    if numberInt > 0:
        print "Ah, you entered a positive number. "
    if numberInt < 0:
        print "Ah, you entered a negative number."
        
# this program is to show how funcitons and arguments work together
def wings_and_beer(wings, cans_of_beer):
	print "You have %d chicken wings!" % wings
	print "You have %d cans of beer!" % cans_of_beer
	print "Oh, yeah, that's enough!"
	print "Super Bowl is on!!!\n"

# each time, we pass a set of arguments to the cheese_and_crackers functions
# 1st run, we can pass straight numbers to the function, the arguments are 30 & 24,
wings_and_beer(30, 24)

# 2nd run, we create a set of variablesthe wings_num & beer_num and assign the value of 20 & 12 to them
# Note that we name the varaibles different from the main argument "wings" to avoid the confusion
wings_num = 20
beer_num = 12
wings_and_beer(wings_num, beer_num)	

# 3rd run we do  math inside the parentheses
wings_and_beer(30 + 20, 24 + 12)

# 4th run, we combine variables and calculations
wings_and_beer(wings_num + 100, beer_num + 120)
