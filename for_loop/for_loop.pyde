size(500,500)
background('#004466')
noFill()
stroke('#ffffff')
strokeWeight(3)

#for i in range(24):
for i in range(3,13,3):  #third argument is step size
    print(i)
    circle(width/2, height/2, 30*i)
    
