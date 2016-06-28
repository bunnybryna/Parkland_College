def removeRed():
    my_pict = makePicture(pickAFile())
    explore(my_pict)
    for px in getPixels(my_pict):
        x = getX(px)
        y = getY(px)
        # set the boundary for left eye
        if 100 <= x <= 112 and 168 <= y <= 178:
            color_red = makeColor(170,75,120)
            # choose the gray with pickAColor()
            color_gray = makeColor(51,51,51)
            color = getColor(px)
            if distance(color,color_red) < 90:
                setColor(px,color_gray)
        # set the boundary for the right eye
        if 155 <= x <= 165 and 170 <= y <= 180:
            color_red = makeColor(170,75,120)
            color_gray = makeColor(51,51,51)
            color = getColor(px)
            if distance(color,color_red) < 90:
                setColor(px,color_gray)
    # show the final picture
    explore(my_pict)
                 