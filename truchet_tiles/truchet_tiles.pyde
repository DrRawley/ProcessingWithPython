def setup():
    size(600,600)
    background('#004477')
    #noFill()
    fill('#ffffff')
    stroke('#ffffff')
    strokeWeight(3)
    noLoop()

def draw():
    background('#004477')
    for i in range(20):
        for j in range(20):
            if (random(1)<0.5):
                arc(i*30,j*30,30,30,0,PI/2)
                arc(i*30+30,j*30+30,30,30,PI,PI*1.5)
            else:
                arc(i*30+30,j*30,30,30,PI/2, PI)
                arc(i*30,j*30+30,30,30,PI*1.5,PI*2)
            
def mousePressed():
    redraw()
