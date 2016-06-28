def changeYellow():
    my_pict = makePicture(pickAFile())
    explore(my_pict)
    for pixel in getPixels(my_pict):
        valueRed = getRed(pixel)
        setRed(pixel,valueRed * 1.5)
    for pixel in getPixels(my_pict):
        valueGreen = getGreen(pixel)
        setGreen(pixel,valueGreen * 1.5)
    explore(my_pict)

def halfGray():
    my_pict = makePicture(pickAFile())
    explore(my_pict)
    pixels = getPixels(my_pict)
    for i in range(0,len(pixels)/2):
        pixel = pixels[i]
        red_px = getRed(pixel)
        green_px = getGreen(pixel)
        blue_px = getBlue(pixel)
        my_gray = (red_px + green_px + blue_px)/3
        setColor(pixel,makeColor(my_gray,my_gray,my_gray))
    explore(my_pict)
    
def neg_img():
    my_pict = makePicture(pickAFile())
    explore(my_pict)
    for pix in getPixels(my_pict):
        red_px = getRed(pix)
        green_px = getGreen(pix)
        blue_px = getBlue(pix)
        neg_pict = setColor(pix,makeColor(255-red_px, 255-green_px,255-blue_px))
    explore(my_pict)
    
def pink_img():
    my_pict = makePicture(pickAFile())
    explore(my_pict)
    red_fn(my_pict)
    lighten_fn(my_pict)
    explore(my_pict)

def red_fn(my_pict):
    for pix in getPixels(my_pict):
        valueRed = getRed(pix)
        setRed(pix,valueRed * 1.5)
        
def lighten_fn(my_pict):
    for pix in getPixels(my_pict):
        current_value = getColor(pix)
        new_value = makeLighter(current_value)
        setColor(pix,new_value)
        
def copyAndMirror():
    my_pict= makePicture(pickAFile())
    explore(my_pict)
    copyhalf_fn(my_pict)
    mirrorhalf_fn(my_pict)
    explore(my_pict)
        
def copyhalf_fn(my_pict):
    explore(my_pict)
    pixels = getPixels(my_pict)
    for i in range (0,(len(pixels))/2):
        pixel1 = pixels[i]
        color1 = getColor(pixel1)
        color1 = getColor(pixel1)
        pixel2 = pixels[i+(len(pixels))/2]
        setColor(pixel2,color1)
    explore(my_pict)

def mirrorhalf_fn(my_pict):
    pixels = getPixels(my_pict)
    target = len(pixels)-1
    for i in range(0,len(pixels)/2):
        pixel1 = pixels[i]
        color1 = getColor(pixel1)
        pixel2 = pixels[target]
        setColor(pixel2,color1)
        target = target-1        
