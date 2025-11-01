import colorgram

rgb_color123=[]
colors = colorgram.extract("messi.jpg", 10)

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b

    new_color = (r,g,b)
    rgb_color123.append(new_color)

print(rgb_color123)
