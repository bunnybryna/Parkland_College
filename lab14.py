# this program is similar to the one in class
def patternTurtle():
    earth = makeWorld(800,800)
    cuty = squareTurtle(earth)
    cuty.setPenWidth(5)
    cuty.setPenColor(blue)
    for i in range(0,2):
        cuty.turn(45)
        for i in range(0,4):
            cuty.drawSquare()
            cuty.drawSquare(50)
            cuty.drawSquare(150)
            cuty.drawSquare(200)
            cuty.turnRight()

class squareTurtle(Turtle):
     def drawSquare(self,width=100):
         for i in range(0,4):
             self.forward(width)         
             self.turnRight()
             
  # this program is to create a little bit more complicated turtle chasing 
from time import sleep
def chase():
    earth = World(600,600)
    al = Turtle(earth)
    bo = Turtle(earth)
    cy = Turtle(earth)
    di = Turtle(earth)
    el = Turtle(earth)
    fo = Turtle(earth)
    gy = Turtle(earth)
    hi = Turtle(earth) 
    al.setPenWidth(10)
    bo.setPenWidth(10)
    cy.setPenWidth(10)
    di.setPenWidth(10)
    el.setPenWidth(10)
    fo.setPenWidth(10)
    gy.setPenWidth(10)
    hi.setPenWidth(10)    
    al.penUp()
    al.moveTo(0,0)
    al.penDown()
    bo.penUp()
    bo.moveTo(300,0)
    bo.penDown()
    cy.penUp()
    cy.moveTo(600,0)
    cy.penDown()
    di.penUp()
    di.moveTo(600,300)
    di.penDown()   
    el.penUp()
    el.moveTo(600,600)
    el.penDown()
    fo.penUp()
    fo.moveTo(300,600)
    fo.penDown()
    gy.penUp()
    gy.moveTo(0,600)
    gy.penDown()
    hi.penUp()
    hi.moveTo(0,300)
    hi.penDown()     
    for i in range(0,300):
        chaseTurtle(al,bo)
        chaseTurtle(bo,cy)
        chaseTurtle(cy,di)
        chaseTurtle(di,el)
        chaseTurtle(el,fo)
        chaseTurtle(fo,gy)
        chaseTurtle(gy,hi)
        chaseTurtle(hi,al) 
        # time.sleep(secs) suspend execution for the given time
        sleep(0.001)              

def chaseTurtle(t1,t2):
    t1.turnToFace(t2)
    t1.forward(4)
    
 # this program is a updated version of program 203
from time import sleep
def dance():
    makeSquare()

def makeSquare():
    w = makeWorld(800,800)
    evenlist = []
    oddlist = []
    for turtles in range(10):
        t = makeTurtle(w)
        t.turn(turtles * 36)
        if turtles % 2 == 0:
            evenlist = evenlist + [t]
        else:
            oddlist = oddlist + [t]
    for times in range(36):
        for sides in range(6):
            if times % 2 == 0:
            # set the even turtle features
            # pink, make squares
                for t in evenlist:
                    t.setPenWidth(3)
                    t.setPenColor(pink)
                    t.setBodyColor(pink)
                    t.forward(100)
                    t.turn(90)
                    
            else:
                for t in oddlist:
                # set the odd turtle features
                # blue, make hexagons                
                    t.setPenWidth(3)
                    t.setPenColor(blue)
                    t.setBodyColor(blue)
                    t.forward(100)
                    t.turn(36)
                sleep(0.2)
                
# this program is to create a spiral by repeating hexagon pattern
import random
def spiral():
    earth = makeWorld(900,900)
    tom = makeTurtle(earth) 
    tom.penUp()
    tom.moveTo(450,300)
    tom.penDown()
    for num in range(0,150):
        tom.turn(5)
        r = 0
        g = int(255*random.random())   
        b = 255
        # use random number to generate different kinds of blue 
        tom.setColor(makeColor(r,g,b))     
        for i in range(0,6):
            tom.forward(num)
            tom.turn(60)
        
# this program is to create a colorful pyramid
import random
def square3D():
    earth = makeWorld(600,600)
    miya = makeTurtle(earth)
    miya.moveTo(0,600)
    num = 0
    # using two for loops
    # the first loop is to increment the width of the square
    for i in range(0,600):
        num = num + 1
        # to pick up the random color
        r = int(255*random.random())
        g = int(255*random.random())   
        b = int(255*random.random())
        miya.setColor(makeColor(r,g,b))
        # the second loop is to form a square                 
        for i in range(0,4):
            miya.forward(num)
            miya.turnRight()                    
