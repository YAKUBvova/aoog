from PIL import Image,ImageDraw
import numpy as np

width = 960
height = 960
white = (255, 255, 255)
filename = "ds8_2.jpg"

def result_matrix(fi):
    x,y=480,480
    cos = round(np.cos(fi))
    sin = round(np.sin(fi))
    return np.matrix([[cos,sin,0],[-sin,cos,0],[x*(1-cos)+y*sin,y*(1-cos)-x*sin,1]])


def rotation(x,y,res):
    origin = np.matrix([[x,y,1]])
    changed = np.matmul(origin,res)
    return [changed[0,0],changed[0,1]]


image1=Image.new("RGB", (width, height), white)
draw = ImageDraw.Draw(image1)
file = open('DS8.txt', 'r')
fi = np.pi/2
res_matrix = result_matrix(fi)

while True:
    line = file.readline()
    line = line.split()
    if not line:
        break
    cords = rotation(int(line[1]),height-int(line[0]),res_matrix)
    x , y= cords[0] , cords[1]
    draw.line([x, y, x+1,y], (30,144,255))
file.close()
image1.save(filename)


