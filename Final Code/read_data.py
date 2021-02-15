import PIL.Image, PIL.ImageDraw
import math
angles = []
radius = []
file_name = input('Enter the file name (with ".txt") : ')
txt = open(file_name)
#txt = open('SONAR_DATA.txt')
Lines = txt.readlines()
total_lines = 0
for i in Lines:
    pre_values = i.split('\n')
    values = pre_values[0].split(' ')
    #print(values)
    total_lines = total_lines + 1
    angles.append(int(values[0]))
    radius.append(int(values[1]))
    #print(values[0]+ "  " +values[1])

print(angles)
print(radius)

circle_graph = PIL.Image.new("RGB", (1500,1500), (0,0,0))
draw = PIL.ImageDraw.Draw(circle_graph)
draw.point((750,750),(0,255,0))
draw.point(( 500*math.cos(math.radians(30)) + 750, 500*math.sin(math.radians(30)) + 750 ),(0,255,0))
draw.point(( 500*math.cos(math.radians(60)) + 750, 500*math.sin(math.radians(60)) + 750),(0,255,0))
draw.point(( 500*math.cos(math.radians(90)) + 750, 500*math.sin(math.radians(90)) + 750),(0,255,0))
draw.point(( 500*math.cos(math.radians(120)) + 750, 500*math.sin(math.radians(120)) + 750),(0,255,0))
draw.point(( 500*math.cos(math.radians(150)) + 750, 500*math.sin(math.radians(150)) + 750),(0,255,0))
draw.point(( 500*math.cos(math.radians(180)) + 750, 500*math.sin(math.radians(180)) + 750),(0,255,0))
draw.point(( 500*math.cos(math.radians(210)) + 750, 500*math.sin(math.radians(210)) + 750),(0,255,0))
draw.point(( 500*math.cos(math.radians(240)) + 750, 500*math.sin(math.radians(240)) + 750),(0,255,0))
draw.point(( 500*math.cos(math.radians(270)) + 750, 500*math.sin(math.radians(270)) + 750),(0,255,0))
draw.point(( 500*math.cos(math.radians(300)) + 750, 500*math.sin(math.radians(300)) + 750),(0,255,0))
draw.point(( 500*math.cos(math.radians(330)) + 750, 500*math.sin(math.radians(330)) + 750),(0,255,0))
draw.point(( 500*math.cos(math.radians(360)) + 750, 500*math.sin(math.radians(360)) + 750),(0,255,0))
for i in range(0,total_lines):
    x1 = round(radius[i]*math.cos(math.radians(angles[i])))
    y1 = round(radius[i]*math.sin(math.radians(angles[i])))
    print("Point "+str(i+1)+" : (" + str(x1) + " , "+str(y1) + " ) "  )
    #print(radius[i]*math.sin(math.radians(angles[i])))
    #print(radius[i]*math.cos(math.radians(angles[i])))
    draw.point((round(radius[i]*math.cos(math.radians(angles[i])))+750,round(radius[i]*math.sin(math.radians(angles[i])))+750),(255,255,255))

circle_graph.show()