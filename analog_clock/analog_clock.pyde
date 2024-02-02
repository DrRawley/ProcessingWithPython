
def setup():
    size(600, 600)
    frameRate(1)
    noFill()
    stroke('#ffffff')
    strokeWeight(2)
    frameRate(2)
    
def draw():
    background('#004477')
    strokeWeight(4)
    circle(300, 300, 580)
    strokeWeight(2)
    fill('#ffffff')
    circle(300,300,10)
    noFill()
    resetMatrix()
    for i in range(60):
        x = cos(i*2*PI/(60))*(580/2)
        y = sin(i*2*PI/(60))*(580/2)
        translate(300+x, 300+y)
        rotate(i*2*PI/60)
        if (i % 5):
            line(0,0,-10,0)
        else:
            line(0,0,-15,0)
        
        resetMatrix()
    textSize(50)
    textAlign(CENTER, CENTER)
    for i in range(12):
        x = cos(i*2*PI/12-2*2*PI/12)*250
        y = sin(i*2*PI/12-2*2*PI/12)*250
        translate(300+x, 300+y)
        text((i+1), 0, 0)
        resetMatrix()
    translate(300,300)
    rotate(second()*2*PI/60)
    line(0,0, 0, -220)
    resetMatrix()
    translate(300,300)
    rotate(minute()*2*PI/60+second()*2*PI/(60*60))
    strokeWeight(4)
    line(0,0, 0, -210)
    resetMatrix()
    translate(300,300)
    rotate(hour()*2*PI/12+minute()*2*PI/(12*60))
    strokeWeight(6)
    line(0,0, 0, -150)
