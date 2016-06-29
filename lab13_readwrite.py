# the first function is to create and write an empty file
def writeEmptyFile(filePath):
    handle = open(filePath,"wt")
    # clear all the data in the file
    handle.write("")
    handle.close()

# the second function is to add three new strings(lines) to the same file
def writeFile(filePath,firstLine,secondLine,thirdLine):
    handle = open(filePath,"wt")
    handle.write(firstLine)
    # add \n between strings to make it clearer
    handle.write("\n")
    handle.write(secondLine)
    handle.write("\n")
    handle.write(thirdLine)
    handle.close()

# the third function is to read and print the file
def readFile(filePath):
    handle = open(filePath,"rt")
    lines = handle.read()
    print lines
    handle.close()