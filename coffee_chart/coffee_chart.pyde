import json
jsondata = open('coffees.json')
coffees = json.load(jsondata)

size(800,800)
background('#004477')
mug=120
spacing=230
col = 1
translate(100,100)
for coffee in coffees:
    
    noStroke()
    ingBase = mug
    for ingredient in coffee['ingredients']:
        fill(ingredient['color'])
        qty = ingredient['quantity']
        rect(0,ingBase,mug,-qty)
        ingBase -= qty
    
    #draw mug
    stroke('#ffffff')
    strokeWeight(5)
    noFill()
    square(0,0,mug)
    arc(mug,mug/2,40,40,-PI/2,PI/2)
    arc(mug,mug/2,65,65,-PI/2,PI/2)
    #label
    fill('#ffffff')
    textSize(16)
    label=coffee['name']
    text(label,mug/2-textWidth(label)/2,mug+40)

    if col == 3:
        translate(spacing*-2,spacing)
        col = 1
    else:
        translate(spacing, 0)
        col += 1  
