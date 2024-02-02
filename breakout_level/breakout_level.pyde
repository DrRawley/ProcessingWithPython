size(600,600)
noStroke()
background('#000000')
#ball and paddle
fill('#ffffff')
circle(350,440,18)
rect(300,520,190,40)

r = '#ff0000' #red
o = '#ff9900' #orange
y = '#ffff00' #yellow
g = '#00ff00' #green
b = '#0099ff' #blue
p = '#6633ff' #violet

bricks = [[[r,1],[o,1],[y,1],[g,1]],
          [[o,1],[y,1],[g,1],[b,1]],
          [[y,1],[g,1],[b,1],[p,1]],
          [[g,1],[b,2],[p,2],[b,1]],
          [[b,1],[p,2],[   ],[g,1]],
          [[p,1],[   ],[   ],[y,1]],
          [[   ],[   ],[   ],[o,1]],
          [[g,1],[   ],[   ],[   ]]]

translate(0,height/15)
for row in bricks:
    print(len(row))
    for brick in row:
        if len(brick) == 2:
            print(brick[0])
            fill(brick[0])
            rect(0,0,width/4,height/15)      
            if brick[1] == 2:
                strokeWeight(4)
                stroke('#ffffff')
                line(6,6,width/4-6,6)
                line(6,6,6,height/15-6)
                noStroke()
        else:
            print("Empty")

        translate(width/4,0)
    translate(-width,height/15)
