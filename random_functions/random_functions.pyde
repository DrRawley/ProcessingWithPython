randomSeed(213)
size(600,250)
background('#004477')
noFill()
stroke('#ffffff')
strokeWeight(9)

#print(random(5))
#print(random(5,10))
#print(int(random(5,10)))


for i in range(50):
    point(random(width), i*height/50)
    
