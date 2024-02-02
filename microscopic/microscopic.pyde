from amoeba import Amoeba

amoebas = []
#a1 = Amoeba(400, 200, 100, 0.3, -0.1)
for i in range(8):
    diameter=random(50,200)
    speed=1000/(diameter*50)
    x,y=random(800),random(400)
    amoebas.append(Amoeba(x,y,diameter,speed,speed))

def setup():
    size(800,800)
    frameRate(120)

current = PVector(0.1, -0.2)

def draw():
    background('#004477')

    pointer = PVector(mouseX, mouseY)
    print(mousePressed)
    
    for i, a in enumerate(amoebas):
        
        #collision detection
        for j, b in enumerate(amoebas):
            if a is b:
                continue #skip if it's the same amoeba
            distance = a.location.dist(b.location)
            minDistance = (a.d + b.d)/2
            BtoA = a.location - b.location
            BtoA.normalize()
            if (distance <= minDistance*1.05):
                a.location += BtoA.limit(a.maxpropulsion*2) 
            if  distance >= minDistance*1.05 and distance <= minDistance*1.5:
                a.location += BtoA.limit(a.maxpropulsion*0.5)                
        
        #wrap around code
        r = a.d / 2
        if a.location.x - r > width:
            a.location.x = 0 - r
        if a.location.x + r < 0:
            a.location.x = width + r
        if a.location.y - r > height:
            a.location.y = 0 - r
        if a.location.y + r < 0:
            a.location.y = height + r
        
        if mousePressed:
            difference = pointer - a.location
            a.propulsion += difference.limit(a.maxpropulsion/100)
        
        a.location += a.propulsion.limit(a.maxpropulsion)
        a.location += current
        a.display()
    

    
