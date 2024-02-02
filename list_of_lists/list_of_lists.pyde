size(500,380)
background('#004477')
noFill()
stroke('#ffffff')
strokeWeight(3)
h=50
translate(100, 40)
bands=6
rect(0,0,40,h*bands)
bands1 = ['#ff0000', #red
         '#ff9900', #orange
         '#ffff00', #yellow
         '#00ff00', #green
         '#0099ff', #blue
         '#6633ff'] #violet
for band in bands1:
    fill(band)
    rect(0,0,40,h)
    translate(0,h)
    
bands2 = [[100,0,0,'red'],
          [100,60,0,'orange'],
          [100,100,0,'yellow'],
          [0,100,0,'green'],
          [0,60,100,'blue'],
          [40,20,100,'violet']]
colorMode(RGB,100)
resetMatrix()
translate(100,40)
for band in bands2:
    #r = band[0] * 0.64
    #g = band[1] * 2.15
    #b = band[2] * 0.22
    r = band[0]
    g = band[1]
    b = band[2]
    sum = r + b + g
    avg = sum / 3
    #fill(avg,avg,avg)
    #rect(0,0,sum, h)
    fill('#ff0000')
    rect(0,0,r,h)
    fill('#00ff00')
    rect(r,0,g,h)
    fill('#0000ff')
    rect(r+g,0,b,h)
    fill('#ffffff')
    textAlign(RIGHT)
    text(band[3],-20,30)
    translate(0,h)
    
