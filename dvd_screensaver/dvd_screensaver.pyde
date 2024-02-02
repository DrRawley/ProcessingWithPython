y = 100
x = 100
xspeed=2
yspeed=2
txt = 'DVD'
dvdHeight = 0
dvdWidth = 0


def setup():
    global dvdHeight, dvdWidth
    size(800,600)
    fill('#0099ff')
    textSize(50)
    dvdHeight = int(textAscent() + textDescent())
    dvdWidth = int(textWidth(txt))
    print(dvdHeight, dvdWidth) 
    
def draw():
    global y, yspeed
    global x, xspeed
    background('#000000')
    y += yspeed
    x += xspeed
    text('DVD', x,y)
    if y >= height or y <= dvdHeight:
        yspeed *= -1
        print("y:", y)
    if x >= width - dvdWidth or x <= 0:
        xspeed *= -1
        print("x:", x)
        
