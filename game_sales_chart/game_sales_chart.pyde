size(800,1000)
background('#004477')
tsv = loadStrings('list_of_best-selling_video_games.tsv')

color = ['#ff0000', #red
         '#ff9900', #orange
         '#ffff00', #yellow
         '#00ff00', #green
         '#0099ff', #blue
         '#6633ff'] #violet
         

noStroke()
maxValue = float(tsv[1].split('\t')[2]) #get max value from the minecraft entry
numGames = len(tsv)-1
rowHeight = height / numGames
textSize(rowHeight-4)


for i, game in enumerate(tsv[1:]):
    entry = game.split('\t')
    name = entry[1]
    sales = float(entry[2])
    
    barWidth = int((sales / maxValue) * width)
    
    fill(color[i%6])
    rect(0,0,barWidth,rowHeight)
    fill('#000000')
    text(name, 5, rowHeight-4)
    noFill()
    print(i)
    translate(0,rowHeight)
    #print(name, barWidth)
