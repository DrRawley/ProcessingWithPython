size(800,800)
background('#004477')
stroke('#ffffff')
strokeWeight(3)
noFill()
level1 = (height-50)/4
level2 = 2*(height-50)/4
level3 = 3*(height-50)/4
level4 = (height-50)

#vacation
fill('#00a500')
arc(width/2, height/2, level4, level4, 4*PI/7+PI, 5*PI/7+PI, PIE) 
#metal
fill('#ff99ff')
arc(width/2, height/2, level3, level3, PI, 2*PI/7+PI, PIE) 
#rap
fill('#ff99ff')
arc(width/2, height/2, level3, level3, 2*PI/7+PI, 4*PI/7+PI, PIE) 
#photos
fill('#4499ff')
arc(width/2, height/2, level3, level3, 4*PI/7+PI, 6*PI/7+PI, PIE) 
#work
fill('#4499ff')
arc(width/2, height/2, level3, level3, 6*PI/7+PI, 7*PI/7+PI, PIE) 
#music
fill('#ff3399')
arc(width/2, height/2, level2, level2, 0*PI/7+PI, 4*PI/7+PI, PIE) 
#docs
fill('#aa33aa')
arc(width/2, height/2, level2, level2, 4*PI/7+PI, 7*PI/7+PI, PIE)
#videos
fill('#ff0000')
arc(width/2, height/2, level2, level2, 0*PI/7, 0*PI/7+PI, PIE)
#HDD
fill('#004477')
circle(width/2, height/2, level1)
