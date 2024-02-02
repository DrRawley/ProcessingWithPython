def setup():
    size(600,600)
    background('#004477')
    ernest = createFont('Ernest.ttf', 20)
    textFont(ernest)
    noLoop()

swatches = ['#ff0000','#ff9900','#ffff00','#00ff00','#0099ff','#6633ff']
brushcolor = swatches[2]
brushshape = ROUND
brushsize =3
painting = False
paintmode = 'free'
palette = 60

def draw():
    #print(frameCount)
    global painting, paintmode
    
    if mouseX < palette:
        paintmode = 'select'
    
    #black panel
    noStroke()
    fill('#000000')
    rect(0,0,palette,height)
    for i, swatch in enumerate(swatches):
        sx = int(i%2)*palette/2
        sy = int(i/2)*palette/2
        fill(swatch)
        square(sx,sy,palette/2)
    
    #clear button
    fill('#ffffff')
    text('CLEAR', 10, height-12)
    
    if paintmode == 'free':
        if painting:
            #colorMode(HSB, 360, 100, 100)
            #stroke((frameCount) % 360, 100, 100)
            #stroke(swatches[frameCount % 6])
            stroke(brushcolor)
            strokeCap(brushshape)
            strokeWeight(brushsize)
            line(mouseX,mouseY,pmouseX,pmouseY)
        elif frameCount > 1:
            painting = True

    #brush preview
    fill(brushcolor)
    if brushshape == ROUND:
        noStroke()
        circle(palette/2,123,brushsize)
        paintmode = 'free'

def mousePressed():
    if mouseButton == LEFT:
        loop()
    #swatch seslect
    if mouseButton == LEFT and mouseX < palette and mouseY < 90:
        global brushcolor
        brushcolor = get(mouseX,mouseY)

def mouseReleased():
    if mouseButton == LEFT:
        global painting
        painting = False
        noLoop()

def mouseWheel(e):
    global brushsize, paintmode
    paintmode = 'select'
    brushsize -= e.count
    if brushsize < 3:
        brushsize = 3
    if brushsize > 45:
        brushsize = 45
    redraw()

def keyPressed():
    global brushcolor, paintmode
    paintmode = 'select'
    if str(key).isdigit():
        k = int(key) - 1
        if k < len(swatches):
            brushcolor = swatches[k]
    redraw()

def mouseClicked():
    #detect clear button click
    if mouseX >= 10 and mouseX < 50 and mouseY > height-25 and mouseY < height-10:
        fill('#004477')
        noStroke()
        rect(palette, 0, width, height)

    
