def project2():
    #1. use mouth click to choose two images
    butterfly = makePicture(pickAFile())
    plant = makePicture(pickAFile())
    #explore(butterfly)
    #explore(plant)
    print "step1 done"
    width = getWidth(butterfly)
    height = getHeight(butterfly)
    canvas = makeEmptyPicture(width * 5,height * 3)
    #2. copy the butterfly to the center of the canvas
    # the collage will copy the butterfly 5X3
    # so startX and startY of the center one(3X2) will be w*2,h*1
    copy(butterfly,canvas,width*2,height)
    print "step2 done"
    #3.creat the heart of the collage by double mirror
    # copy the bottom right pattern to the other quadrants       
    mirrorVertical(canvas)
    mirrorHorizontal(canvas)
    print "step3 done"
    #4. copy the butterfly to the position 2X1,4X1,2X3,4X3
    copy(butterfly,canvas,width,0)
    copy(butterfly,canvas,width*3,0)
    copy(butterfly,canvas,width,height*2)
    copy(butterfly,canvas,width*3,height*2)
    print "step4 done"
    #5. change butterfly color while copy to 3X1 and 3X3
    myblue = makeColor(102,153,255)
    changeColorCopy(butterfly,canvas,width*2,0,myblue)
    changeColorCopy(butterfly,canvas,width*2,height*2,myblue)
    print "step5 done"
    #6. change the color while copy to 2X2 and 4X2
    mypurple = makeColor(102,0,102)
    changeColorCopy(butterfly,canvas,width,height,mypurple)
    changeColorCopy(butterfly,canvas,width*3,height,mypurple)
    print "step6 done"
    #7. copy and blend to get the bottom right corner
    blend(butterfly,plant,canvas,width*4,height*2)
    print "step7 done"
    #8. rotate and blend to get the bottom left corner
    rotateBlend(butterfly,plant,canvas,0,height*2)
    print "step8 done"
    #9. rotate and blend to get the top left corner
    rotateBlend2(butterfly,plant,canvas,0,0)
    print "step9 done"
    #10. rotate and blend to get the top right corner
    rotateBlend3(butterfly,plant,canvas,width*4,0)
    print "step10 done"
    #11. copy the plant to the rest position 1X2,5X2
    copy(plant,canvas,0,height*1)
    copy(plant,canvas,width*4,height*1)
    print "step11 done"	
    explore(canvas)
    
def copy(my_pict,canvas,startX,startY):
    targetX = startX
    for sourceX in range(0,getWidth(my_pict)):
        targetY = startY
        for sourceY in range(0,getHeight(my_pict)):
            px = getPixel(my_pict,sourceX,sourceY)
            cx = getPixel(canvas,targetX,targetY)
            setColor(cx,getColor(px))
            targetY = targetY + 1
        targetX = targetX + 1
    
def mirrorVertical(my_pict):
# mirror from left to right, right half gone
    width = getWidth(my_pict)
    height = getHeight(my_pict)
    mirrorPoint1 = width/2
    for x in range(0,mirrorPoint1):
        for y in range(0,height):
            px1 = getPixel(my_pict,x,y)
            px2 = getPixel(my_pict,width-1-x,y)
            color1 = getColor(px1)
            setColor(px2,color1)
            
def mirrorHorizontal(my_pict):
# mirror from bottom to top, top half gone
    width = getWidth(my_pict)
    height = getHeight(my_pict)
    mirrorPoint2 = height/2
    for x in range(0,width):
        for y in range(0,mirrorPoint2):
            px1 = getPixel(my_pict,x,y)
            px2 = getPixel(my_pict,x,height-1-y)
            color2 = getColor(px2)
            setColor(px1,color2)
            
def changeColorCopy(my_pict,canvas,startX,startY,newColor):
    targetX=startX
    for sourceX in range(0,getWidth(my_pict)):
        targetY = startY
        for sourceY in range(0,getHeight(my_pict)):
            color = getColor(getPixel(my_pict,sourceX,sourceY))
            mypink = makeColor(255,204,0)
            if distance(color,mypink)<60:
                setColor(getPixel(canvas,targetX,targetY),newColor)
            else:
                setColor(getPixel(canvas,targetX,targetY),color)
            targetY = targetY + 1
        targetX = targetX + 1

def blend(my_pict,my_pict2,canvas,startX,startY):
    targetX = startX
    for sourceX in range(0,getWidth(my_pict)):
        targetY = startY
        for sourceY in range(0,getHeight(my_pict)):
            px1 = getPixel(my_pict,sourceX,sourceY)
            px2 = getPixel(my_pict2,sourceX,sourceY)
            nr = 0.5* getRed(px1) + 0.5* getRed(px2)
            ng = 0.5* getGreen(px1) + 0.5* getGreen(px2)
            nb = 0.5* getBlue(px1) + 0.5* getBlue(px2)
            color = makeColor(nr,ng,nb)
            setColor(getPixel(canvas,targetX,targetY),color)
            targetY = targetY + 1
        targetX = targetX + 1
        
def rotateBlend(my_pict,my_pict2,canvas,startX,startY):
# this function has combined the rotating and blending programs from the book 
    width = getWidth(my_pict)
    targetX = startX
    for sourceX in range(0,getWidth(my_pict)):
        targetY = startY
        for sourceY in range(0,getHeight(my_pict)):
            # flip across the Y-axis
            px1 = getPixel(my_pict,width-1-sourceX,sourceY)
            px2 = getPixel(my_pict2,sourceX,sourceY)
            nr = 0.5* getRed(px1) + 0.5* getRed(px2)
            ng = 0.5* getGreen(px1)+ 0.5* getGreen(px2)
            nb = 0.5* getBlue(px1) +0.5* getBlue(px2)
            color = makeColor(nr,ng,nb)
            setColor(getPixel(canvas,targetX,targetY),color)
            targetY = targetY + 1
        targetX = targetX + 1  

def rotateBlend2(my_pict,my_pict2,canvas,startX,startY):
    width = getWidth(my_pict)
    height = getHeight(my_pict)
    targetX = startX
    for sourceX in range(0,getWidth(my_pict)):
        targetY = startY
        for sourceY in range(0,getHeight(my_pict)):
            # rotate 180 degree
            px1 = getPixel(my_pict,width-1-sourceX,height-1-sourceY)
            px2 = getPixel(my_pict2,sourceX,sourceY)
            nr = 0.5* getRed(px1) + 0.5* getRed(px2)
            ng = 0.5* getGreen(px1)+ 0.5* getGreen(px2)
            nb = 0.5* getBlue(px1) +0.5* getBlue(px2)
            color = makeColor(nr,ng,nb)
            setColor(getPixel(canvas,targetX,targetY),color)
            targetY = targetY + 1
        targetX = targetX + 1  
        
def rotateBlend3(my_pict,my_pict2,canvas,startX,startY):
    width = getWidth(my_pict)
    height = getHeight(my_pict)
    targetX = startX
    for sourceX in range(0,getWidth(my_pict)):
        targetY = startY
        for sourceY in range(0,getHeight(my_pict)):
            # flip across the X-axis
            px1 = getPixel(my_pict,sourceX,height-1-sourceY)
            px2 = getPixel(my_pict2,sourceX,sourceY)
            nr = 0.5* getRed(px1) + 0.5* getRed(px2)
            ng = 0.5* getGreen(px1)+ 0.5* getGreen(px2)
            nb = 0.5* getBlue(px1) +0.5* getBlue(px2)
            color = makeColor(nr,ng,nb)
            setColor(getPixel(canvas,targetX,targetY),color)
            targetY = targetY + 1
        targetX = targetX + 1  