# this funciton takes two argument
# one is the picture path used to upload picture to drop on the canvas
# another one is the path used to save the final picture
import random
def turtleImage(pictPath,savePath):
    # 1. create an image with random drawing
    # 2. use the random drawing image as the background    
    canvas = makeEmptyPicture(1280,960)
    bgTurtle = makeTurtle(canvas)
    # call the randomDrawing function to draw a random background
    randomDrawing(bgTurtle) 
    # 3. drop 4 tutles 
    ta = makeTurtle(canvas)
    tb = makeTurtle(canvas)
    tc = makeTurtle(canvas)
    td = makeTurtle(canvas)
    # move them to 4 corners without pen mark
    turtleToCorner(ta,0,0)
    turtleToCorner(tb,1280,0)
    turtleToCorner(tc,1280,960)
    turtleToCorner(td,0,960)
    # 4. turtles chase toward each other and draw linse 
    # till all converge in the center
    for i in range(0,600):
        chaseTurtle(ta,tb)
        chaseTurtle(tb,tc)
        chaseTurtle(tc,td)
        chaseTurtle(td,ta)
    # 5. another turtle drops 4 small images in a square
    my_pict = makePicture(pictPath)
    dropTurtle = makeTurtle(canvas)
    # use the turtleToCorner funciton to move the turtle
    # the square is 720*720 while the canvas is 1280*960
    # 280=(1280-720)/2,120=(960-720)/2
    turtleToCorner(dropTurtle,280,120)
    dropTurtle.turnRight()
    # 6. call the dropPicture function to drop 4 images in a square without covering the center
    dropPicture(dropTurtle,my_pict)
    # show the canvas
    show(canvas)
    # 7. write the image to disk
    writePictureTo(canvas,savePath)
        

# 1st sub-function to draw a random background    
def randomDrawing(turtle):
    turtle.setPenColor(green)
    for i in range(0,2000):
        turtle.forward(int(100*random.random()))
        turtle.turn(int(100*random.random()))
        
# 2nd sub-function to move 4 turtles to 4 corners        
def turtleToCorner(turtle,x,y):
    # leave no pen marks
    turtle.penUp()
    turtle.moveTo(x,y)
    turtle.penDown()
    
# 3rd sub-function to make turtles to chase after each other    
def chaseTurtle(t1,t2):
    t1.turnToFace(t2)
    # set the pen width as 10 pix
    t1.setPenWidth(10)
    t1.forward(4)

# 4th sub-function to drop pictures in a square 720*720   
def dropPicture(turtle,pict):
    # leave no pen marks
    turtle.penUp()
    for i in range(0,4):
        turtle.forward(480)
        turtle.drop(pict)
        turtle.forward(240)
        turtle.turnRight()