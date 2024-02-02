def setup():
    size(800,400)
    frameRate(20)
    background('#000000')
    stroke('#ffffff')
    
def draw():
    #circle(mouseX, mouseY, 15)
    strokeWeight(15)
    colorMode(HSB, 360, 100, 100)
    h = mouseX * 360 / width
    s = mouseY * 100 / height
    b = 100
    stroke(h, s, b)
    if mousePressed and mouseButton == LEFT:
        line(mouseX,mouseY,pmouseX,pmouseY)
    
    
