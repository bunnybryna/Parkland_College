# please use the file named "flowers.jpg"
def skyChange():
    my_pict = makePicture(pickAFile())
    explore(my_pict)
    color_blue = makeColor(10,110,180)
    for px in getPixels(my_pict):
        x = getX(px)
        y = getY(px)
        # limit to the sky area
        # getWidth(my_pict)=450,getHeight(my_pict)=282
        if 0 <= x <= 450 and 0 <= y <= 200:
                color = getColor(px)
                if distance(color, color_blue) < 90:
                    # use "makeDarker"
                    new_color = makeDarker(color)
                    setColor(px,new_color)
    explore(my_pict)
    
# please use the file named "flowers.jpg"
def flowerChange():
    my_pict = makePicture(pickAFile())
    explore(my_pict)
    color_yellow = makeColor(245,230,0)
    for px in getPixels(my_pict):
        x = getX(px)
        y = getY(px)
        # limit the change to the middle one
        if 250 <= x <= 275 and 100 <= y <= 120:
            color = getColor(px)
            if distance(color,color_yellow) < 50:
                # set the color to read
                setColor(px,makeColor(255,0,0))
    explore(my_pict)
    
# Reference, program 51 @ page 121
def sepiaTint():
    my_pict = makePicture(pickAFile())
    explore(my_pict)
    grayScale(my_pict)
    explore(my_pict)
    for px in getPixels(my_pict):
        r = getRed(px)
        g = getGreen(px)
        b = getBlue(px)
        # tint shadows
        if r < 63:
            r = r * 1.1
            b = b * 0.9
        # tint midtones
        if r > 62 and r < 192:
            r = r * 1.15
            b = b * 0.85
        # tint highlights
        if r > 191:
            r = r * 1.08
            if r > 255:
                r = 255
            b = b * 0.93
        setRed(px,r)
        setBlue(px,b)
    explore(my_pict)

def grayScale(my_pict):
    for px in getPixels(my_pict):
        r = getRed(px)
        g = getGreen(px)
        b = getBlue(px)
        gy = (r+g+b) / 3
        setColor(px,makeColor(gy,gy,gy))   
        
def halfPosterize():
    my_pict = makePicture(pickAFile())
    for px in getPixels(my_pict):
        x = getX(px)
        y = getY(px)
        # use x to make a range
        if x >= (getWidth(my_pict)/2):
            r = getRed(px)
            g = getGreen(px)
            b = getBlue(px)
            luminance = (r+g+b)/3
            if luminance < 100:
                setColor(px,black)
            if luminance >= 100:
                setColor(px,white)
    explore(my_pict)
    
def mirrorVertical():
    my_pict = makePicture(pickAFile())
    explore(my_pict)
    width = getWidth(my_pict)
    height = getHeight(my_pict)
    for y in range(0,height):
        for x in range(0,width/2):
            leftpx = getPixel(my_pict,x,y)
            # that last x = width-1, just like the last index = len-1
            rightpx = getPixel(my_pict,width-1-x,y)
            # set the color of the left to the right
            color = getColor(leftpx)
            setColor(rightpx,color)
    explore(my_pict)  
