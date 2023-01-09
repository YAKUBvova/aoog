from PIL import Image,ImageDraw
import numpy as np

width = 960
height = 540
white = (255, 255, 255)
filename = "ds8_3.jpg"

def result_matrix(d):
    x,y=540 ,0
    res = np.matrix([[1,0,0,0],[0,1,0,0],[0,0,1,1/d],[0,0,0,0]])
    res = np.matmul(np.matrix([[1,0,0,0],[0,1,0,0],[0,0,1,0],[-x,-y,0,1]]),res)
    res = np.matmul(res,np.matrix([[1,0,0,0],[0,1,0,0],[0,0,1,0],[x,y,0,1]]))
    return res


def proection(x,y,res,d):
    origin = np.matrix([[x,y,100,1]])
    proectioned = np.matmul(origin,res)
    proectioned = proectioned*d/100
    return [proectioned[0,0],proectioned[0,1]]


image1=Image.new("RGB", (width, height), white)
draw = ImageDraw.Draw(image1)
file = open('DS8.txt', 'r')
d = 50
res_matrix = result_matrix(d)

while True:
    line = file.readline()
    line = line.split()
    if not line:
        break
    cords = proection(int(line[0]),int(line[1]),res_matrix,d)
    x , y= cords[0] , cords[1]
    draw.line([x, y, x+1,y], (30,144,255))
file.close()
image1.save(filename)


