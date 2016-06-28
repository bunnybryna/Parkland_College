# Lab 8 is a program to slip strings and digits
def split(entStr):
    print entStr
    # create two holder to split the strings
    holderNum = ""
    holderChar = ""
    # the iteration variable is index number
    for i in range(len(entStr)):
        value = entStr[i]
        # compare each value to 0~9, in other words, numbers
        if value in "0123456789":
            holderNum = holderNum + value
    print "The Digits Were: ", holderNum
    for i in range(len(entStr)):
        value = entStr[i]
        # compare each value to a~z, in other words, alphabet
        if value.lower() in "abcdefghijklmnopqrstuvwxyz":
            holderChar = holderChar + value
    print "The Alpha Characters Were: ", holderChar
    # using a for loop to sum numbers
    sumNum = 0
    for i in range(len(holderNum)):
        sumNum = int(holderNum[i]) + sumNum
    print "The Sum of the Digits is: ", sumNum

# Try to accomplish the same result with a different approach:
def split2(entStr):
    print entStr
    holderNum = ""
    holderChar = ""
    # ord("0")=48,ord("9")=57
    for i in range(len(entStr)):
        value = entStr[i]
        ordValue = ord(value)
        if ordValue >= 48 and ordValue <= 57:
            holderNum = holderNum + value
    print "The Digits Were: ", holderNum
    # ord("a")=97,ord("z")=122,ord("A")=65,ord("Z")=90
    for i in range(len(entStr)):
        value = entStr[i]
        ordValue = ord(value)
        if ordValue >= 65 and ordValue <= 90 or (ordValue >=97 and ordValue <= 122):
            holderChar = holderChar + value
    print "The Alpha Characters Were: ", holderChar
    # using a for loop to sum numbers
    sumNum = 0
    for i in range(len(holderNum)):
        sumNum = int(holderNum[i]) + sumNum
    print "The Sum of the Digits is: ", sumNum