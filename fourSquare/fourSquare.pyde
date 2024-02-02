size(600,600)
noFill()
noStroke()
#red quadrant
fill('#ff0000')
rect(width/2,0,width/2,height/2)
#blue quadrant
fill('#004477')
rect(0,0,width/2,height/2)
#violet quadrant
fill('#6633ff')
rect(0,height/2,width/2,height/2)
#orange quadrant
fill('#ff9900')
rect(width/2,height/2,width/2,height/2)

x=400
y=100
#txt = '?'
if x > 0 and x < width/2 :
    if y > 0 and y < height/2 :
        txt= 'B'
    if y >= height/2 and y <= height:
        txt = 'V'
if x >= width/2 and x <= width:
    if y > 0 and y < height/2 :
        txt= 'R'
    if y >= height/2 and y <= height:
        txt = 'O'
        
        
fill('#ffffff')
textSize(40)
textAlign(CENTER,CENTER)
text(txt, x, y)
