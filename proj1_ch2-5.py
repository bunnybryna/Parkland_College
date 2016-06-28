def colorProject():
    # allow user to pick a file using mouse
    my_pict = makePicture(pickAFile())
    # display the original picture
    explore(my_pict)
    for px in getPixels(my_pict):
        x = getX(px)
        y = getY(px)
        # set the boundary
        if 45 <= x <= 75 and 140 <= y <= 180:
            # call a function below            
            purpleGreen(px)
        if 180 <= x <= 210 and 35 <= y < 70:
            purpleGreen(px)
        if 440 <= x <= 470 and 35 <= y <= 70:
            purpleGreen(px)
        if 110 <= x <= 150 and 45 <= y <= 85:
            pinkRed(px)
        if 340 <= x <= 390 and 90 <= y <= 140:
            pinkRed(px)
        if 100 <= x <= 225 and 125 <= y <= 220:
            redBlack(px)
        if 180<= x <= 405 and 185 <= y <= 310:
            orangeBlue(px)
        if 0 <= x <= 300 and 215 <= y <= 353:
            blueGray(px)
        if 310 <= x <= 420 and 170 <= y <= 265:
            brownBlue(px)
        if 480 <= x <= 520 and 155 <= y <= 180:
            brownBlue(px)
        if 394 <= x <= 486 and 165 <= y <= 200:
            blackRed(px)
        # getWidth(my_pict)/2=268,getHeight(my_pict)/2=178
        if 0 <= x <= 268 and 0 <= y <= 178:
            lighten(px)
    # display the final picture
    explore(my_pict)
    # write it to disk
    writePictureTo(my_pict,"C:/temp/bzhao1_pro1.jpg")
    
# the argument is px instead of my_pict, cause you're testing px 
def purpleGreen(px):  
    color = getColor(px)
    color_purple = makeColor(200,191,230)
    color_green = makeColor(51,153,0)
    if distance(color,color_purple) < 25:
        setColor(px,color_green)

def pinkRed(px):
    color = getColor(px)
    color_pink = makeColor(255,175,201)
    color_red = makeColor(102,0,0)
    if distance(color,color_pink) < 25:
        setColor(px,color_red)
        
def redBlack(px):
    color = getColor(px)
    color_red = makeColor(237,27,36)
    if distance(color,color_red) < 25:
        setColor(px,black)

def orangeBlue(px):
    color = getColor(px)
    color_orange = makeColor(255,127,38)
    color_blue = makeColor(0,255,255)
    if distance(color,color_orange) < 50:
        setColor(px,color_blue)
        
def blueGray(px):
    color = getColor(px)
    color_blue = makeColor(154,217,234)
    color_gray = makeColor(102,102,102)
    if distance(color,color_blue) < 75:
        setColor(px,color_gray)

def brownBlue(px):
    color = getColor(px)
    color_brown = makeColor(105,45,25)
    if distance(color,color_brown) < 35:
        setColor(px,blue)

def blackRed(px):
    color = getColor(px)
    color_black = makeColor(48,48,48)
    color_red = makeColor(255,0,51)
    if distance(color,color_black) < 75:
        setColor(px,color_red)

def lighten(px):
    color = getColor(px)       
    # lighten once is not obvious enough, I choose to do three times
    color1 = makeLighter(color)
    color2 = makeLighter(color1)
    color3 = makeLighter(color2)
    setColor(px,color3)