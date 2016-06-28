def flowerChange():
# Please use the flowerbutterfly picture thanks
# this program is to change the color while copying
    col = makeColor(255,204,0)
    my_pict = makePicture(pickAFile())
    explore(my_pict)
    width = getWidth(my_pict)
    height = getHeight(my_pict)
    # copy to a blank canvas same size with the original picture
    canvas = makeEmptyPicture(width,height)
    targetX = 0
    for sourceX in range(0,width):
        targetY = 0
        for sourceY in range(0,height):
            color = getColor(getPixel(my_pict,sourceX,sourceY))
            # change the color while copying
            if distance(color,col)<60:
                # change the yellow color to blue
                setColor(getPixel(canvas,targetX,targetY),blue)
            # only change the yellow, the other remains the same
            else:
                setColor(getPixel(canvas,targetX,targetY),color)
            targetY = targetY + 1
        targetX = targetX + 1
    explore(canvas)
    
def doubleMirror():
# this program is to copy the bottom left quadrant to the whole picture
# we will first mirror vertical and then mirror horizontal
    my_pict = makePicture(pickAFile())
    width = getWidth(my_pict)
    height = getHeight(my_pict)
    # differentiate 2 mirror points
    mirrorPoint1 = width/2
    mirrorPoint2 = height/2
    # 1. mirror from left to right, right half gone
    for x in range(0,mirrorPoint1):
        for y in range(0,height):
            px1 = getPixel(my_pict,x,y)
            px2 = getPixel(my_pict,width-1-x,y)
            color1=getColor(px1)
            setColor(px2,color1)
    # 2. mirror from bottom to top, top half gone
    for x in range(0,width):
        for y in range(0,mirrorPoint2):
            px1 = getPixel(my_pict,x,y)
            px2 = getPixel(my_pict,x,height-1-y)
            # note we're flipping from bottom to top
            color2 = getColor(px2)
            setColor(px1,color2)
            
  def ghostImage():
# this program is to put the enlarged ghost image in the center of the new canvas
    my_pict = makePicture(pickAFile())
    width = getWidth(my_pict)
    height = getHeight(my_pict)
    myPink = makeColor(255,0,153)
    # the width and height of the canvas must be larger than 2 times of width and height of the picture 
    canvas = makeEmptyPicture(800,800,myPink)
    # after x and y gets incremented by 2, the picture is enlarged 2 times
    # the center point will be canvasWidth - width*2 
    targetX = (800-width*2)/2
    print width,height
    print targetX
    for sourceX in range(0,width):
        targetY = (800-height*2)/2
        for sourceY in range(0,height):
            px = getPixel(my_pict,sourceX,sourceY)
            cx = getPixel(canvas,targetX,targetY)
            setColor(cx,getColor(px))
            # note that +2 will require you a larger canvas than +1
            # or, an "out of range" error will occur
            targetY = targetY + 2
        targetX = targetX + 2
    explore(canvas)

def justButterfly():
# this program is to copy just the butterfly(150X150)to a canvas(450X450) 
# how to contruct the for loop:
# pic1:x=0,y=0;pic2:x=150,y=0;pic3:x=300,y=0:
# pic4:x=0,y=150;pic5:x=150,y=150;pic6:x=300,y=150; 
# pic7:x=0,y=300;pic8:x=150,y=300;pic9:x=300,y=300; 
# so,i from 0 to 8,x=150*(i%3),y=150*int(i/3)
    my_pict = makePicture(pickAFile())
    canvas = makeEmptyPicture(450,450)
    # we need copy butterfly 9 times
    for i in range(0,9):
        # notes above explains the formula that links targetX(x) to i
        targetX = 150*(i%3)
        for sourceX in range(90,240):
            # notes above explains the formula that links targetY(y) to i
            targetY = 150*int(i/3)
            for sourceY in range(0,150):
                px = getPixel(my_pict,sourceX,sourceY)
                cx = getPixel(canvas,targetX,targetY)
                setColor(cx,getColor(px))
                targetY = targetY + 1
            targetX = targetX + 1
    explore(canvas)    
    explore(my_pict)  
    
def flowerCollage(n):
# this program is to create a collage by copying the same picture any times you want
# you need to pass the argument "n" into the function to state how many copies you want horizontally or vertically
# the program will run very slowly, please carefully choose the value of n(n<=4 is highly recommended)
# the final collage will give you n*n copies of the original picture
    my_pict = makePicture(pickAFile())
    width = getWidth(my_pict)
    height = getHeight(my_pict)
    # the size of the canvas will be n times of the picture
    canvas = makeEmptyPicture(width*n,height*n)
    for i in range(0,n*n):
        # please refer to the justButterfly program to find out how I get the formula
        # targetX = width*(i%n)
        targetX = width*(i%n)
        for sourceX in range(0,width):
            # also refer to the justButterfly program
            targetY = height*(int(i/n))
            for sourceY in range(0,height):
                px = getPixel(my_pict,sourceX,sourceY)
                cx = getPixel(canvas,targetX,targetY)
                setColor(cx,getColor(px))
                targetY = targetY + 1
            targetX= targetX + 1                 
    explore(canvas)    
