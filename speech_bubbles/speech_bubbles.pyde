size(561,768)
art = loadImage('arnolfini_portrait.jpg')
image(art,0,0,width,height)

def speechBubble(x = 190, y = 150, txt = "Hello.", type = "speech"):
    noStroke()
    pushMatrix()
    translate(x,y)
    if (type == 'speech'):
        #tip of speech bubble
        fill('#ffffff')
        beginShape()
        vertex(0,0)
        vertex(15,-40)
        vertex(35,-40)
        endShape(CLOSE)
    elif type == 'thought':
        fill('#ffffff')
        circle(0,0,8)
        circle(10,-20,20)
    #bubble
    textSize(15)
    by=-85
    bw=textWidth(txt)
    pad=20
    rect(0,by,bw+pad*2,45,10)
    fill('#000000')
    textAlign(LEFT, CENTER)
    text(txt,pad,by+pad)
    popMatrix()

def shout(txt):
    return txt.upper() + '!!!'
            
speechBubble(190,150,shout('Check out my peen'))
speechBubble(445,125,'Meh...','thought')
speechBubble(315,650,'Kill me.')
