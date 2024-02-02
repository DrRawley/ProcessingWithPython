size(1500,500)
background('#004466')
noFill()
stroke('#ffffff')
strokeWeight(3)

for i in range(12):
    line(100, 150+i*25, 400, 100+i*25)

spacing = 2.5
for i in range(8):
    line(600, 100+i*spacing, 900, 150+i*spacing)
    spacing *= 1.5

for i in range(12):
#   line(1250, 100+i*25, 1250-((-1)**i)*150, 150+i*25)    
    line(1250, 100+i*25, 1100+(i % 2)*300, 150+i*25)    
