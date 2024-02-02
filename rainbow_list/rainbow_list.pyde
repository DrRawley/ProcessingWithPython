size(500,500)
noStroke()
background('#004477')
bands = ['#ff0000', #red
         '#ff9900', #orange
         '#ffff00', #yellow
         '#00ff00', #green
         '#0099ff', #blue
         '#6633ff' #violet
         ]
translate(0,100)
for i, band in enumerate(bands):
    fill(band)
    rect(0,0,width,50)
    fill('#ffffff')
    textSize(25)
    text(i, 20,35)
    translate(0,50)

 
