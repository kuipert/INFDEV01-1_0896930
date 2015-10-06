import math

#this program draws squares, triangles and circles
size = input("What is the size of the shapes? \n")
draw = ""

#square
for i in range(size):
    for j in range(size):
        draw += "* "
    draw += "\n"
print(draw)
draw = ""

#hollow square
for i in range(size):
    for j in range(size):
        if i == 0 or i == size - 1 or j == 0 or j == size - 1:
            draw += "* "
        else:
            draw += "  "
    draw += "\n"
print(draw)
draw = ""

#triangle
for i in range(size):
    for j in range(size):
        if j <= i:
            draw += "* "
        else:
            draw += "  "
    draw += "\n"
print(draw)
draw = ""

#pyramid
for i in range(size):
    for j in range(size * 2 + 1):
        if j * 2 > (size - i - 1) * 2 and j * 2 < (size + i + 1) * 2:
            draw += "* "
        else:
            draw += "  "
    draw += "\n"
print(draw)
draw = ""

#circle
for i in range(size):
    for j in range(size):
        if math.sqrt(pow((j - size / 2), 2) + pow((i - size / 2), 2)) < size/2:
            draw += "* "
        else:
            draw += "  "
    draw += "\n"
print(draw)
draw = ""

#smiley (doesn't draw smiley when size is smaller than 9
skip = 0
innards = ["_       _ ", "O       O ", "          ", "\\   #   / ", "  _ _ _   "]
for i in range(size):
    for j in range(size):
        if skip > 0:
            skip -= 1
            continue
        if size > 9 and i >= size/2 - 2 and i <= size/2 + 2:
            if j == size/2 - 2:
                draw += innards[i - (size / 2 - 2)]
                skip = 5
        if math.sqrt(pow((j - size / 2), 2) + pow((i - size / 2), 2)) < size/2 and math.sqrt(pow((j - size / 2), 2) + pow((i - size / 2), 2)) > size/2 - 1:
            draw += "* "
        else:
            draw += "  "
    draw += "\n"
print(draw)
draw = ""