# this program is to create a pink flower using turtles of 3 subclasses

def patternTurtle(filename):
    # what makeWorld makes isn't pictures therefore cann't be written to disk
    # use makeEmptyPicture here for saving later 
    world = makeEmptyPicture(1000,1000)
    # first turtle draws green leaves, belongs to the greenTurtle subclass
    outT = greenTurtle(world)
    outT.drawLeaf()
    # second turtle draws pink petals,belongs to the pinkTurtle subclass     
    middleT = pinkTurtle(world)
    middleT.drawFlower()
    # third turtle draws the center of the flower,belongs to the redTurtle subclass
    centerT= redTurtle(world)
    centerT.drawHeart()
    explore(world)
    # set the media path to save the file with a given name
    setMediaPath("C:/Temp/")
    writePictureTo(world,getMediaPath(filename))

# draw triangles 20 times, used as the center of the flower 
class redTurtle(Turtle):
    def drawHeart(self):
        for i in range(0,20):
            self.turn(18)
            for i in range(0,3):
                self.setPenWidth(3)
                self.setPenColor(red)
                self.setBodyColor(red)
                self.forward(25)
                self.turn(120)

# draw hexagons 10 times, used as the petals                                
class pinkTurtle(Turtle):
    def drawFlower(self):
        for i in range(0,10):
            self.turn(36)
            for i in range(0,6):
                self.setPenWidth(5)
                self.setPenColor(pink)
                self.setBodyColor(pink)
                self.forward(100)
                self.turn(60)

# draw squares 5 times, used as the leaves
class greenTurtle(Turtle):
    def drawLeaf(self):
        for i in range(0,5):
            self.turn(72)
            for i in range(0,4):
                self.setPenWidth(3)
                self.setPenColor(green)
                self.setBodyColor(green)
                self.forward(200)
                self.turn(90)