def setup():
    size(500,500)
    background('#004477')
    noFill()
    stroke('#ffffff')
    strokeWeight(3)
    frameRate(25)

def draw():
    background('#004477')
    for i in range(7):
        x = cos((i-frameCount%8)*2*PI/8)
        y = sin((i-frameCount%8)*2*PI/8)
        circle(x*170+250, y*170+250, 80)
    
            
