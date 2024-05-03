
from random import randint, random, uniform
from math import sin, cos, pi

def randomTriangles(screenX, screenY, triangleSize, colorValues, numberTriangles):
    s = '<polygon points="{},{} {},{} {},{}"' + ' style="fill:rgba({},{},{},{})" />'.format(*colorValues)
    lines = []
    for _ in range(numberTriangles):
        center = randint(0,screenX), randint(0,screenY)
        angles = [random()*2*pi for _ in range(3)]
        radii = [uniform(triangleSize/2,triangleSize) for _ in range(3)]
        unit_vertices = [(radius*cos(angle), radius*sin(angle)) for radius, angle in zip(radii,angles)]
        t = str(s.format(*[round(c + vel,3) for v in unit_vertices for vel,c in zip(v,center)]))
        print(t)
        lines.append(t)

    print(''.join(lines))


# color = [90,70,270,0.63]
color = [140,160,206,0.66]
randomTriangles(1000,1000,130,color,220)
