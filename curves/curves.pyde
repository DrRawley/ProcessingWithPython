cp1x=200
cp1y=250
cp2x=320
cp2y=420


def setup():
    size(500,500)
    

    noFill()
    strokeWeight(3)

    stroke('#0099FF')
    #line(100,100,400,400)
    curve(0,0,100,100,400,400,500,500)

    curveTightness(0)
    stroke('#ffff00')
    curve(0,250,100,100,400,400,500,250)
    stroke('#ff9900')
    curve(0,250,0,250,100,100,400,400)
    curve(100,100,400,400,500,250,500,250,)
    noLoop()

def draw():
    grid = loadImage('grid.png')
    image(grid,0,0)
    stroke('#ff99ff')
    cp1x = mouseX
    cp1y = mouseY
    bezier(400,100,cp1x,cp1y,cp2x,cp2y,100,400)
    stroke('#ff0000')
    line(400,100,cp1x,cp1y)
    line(100,400,cp2x,cp2y)

def mousePressed():
    redraw()
