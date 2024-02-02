size(800,800)
background('#ffffff')
#grid = loadImage('grid.png')
#image(grid, 0, 0)
noFill()
stroke('#ffffff')
strokeWeight(0)

startX=262
startY=238

centerX=370
centerY=140
radius=40
offset=40*0.54

fill('#004477')
beginShape()
vertex(262,238)
vertex(262,178)
bezierVertex(262,40,370,30,500,30)
bezierVertex(630,30,730,40,730,178)
vertex(730,370)
bezierVertex(730,440,690,490,630,490)
vertex(380,490)
bezierVertex(295,490,240,555,240,630)
vertex(240,740)
vertex(175,740)
bezierVertex(40,740,30,630,30,500)
bezierVertex(30,370,40,262,178,262)
vertex(500,262)
vertex(500,238)
vertex(262,238)

#to subtract, the points must go counter-clockwise
beginContour()
vertex(centerX,centerY-radius)
bezierVertex(centerX-offset,centerY-radius,centerX-radius,centerY-offset,centerX-radius,centerY)
bezierVertex(centerX-radius,centerY+offset,centerX-offset,centerY+radius,centerX,centerY+radius)
bezierVertex(centerX+offset,centerY+radius,centerX+radius,centerY+offset,centerX+radius,centerY)
bezierVertex(centerX+radius,centerY-offset,centerX+offset,centerY-radius,centerX,centerY-radius)
endContour()

endShape()
