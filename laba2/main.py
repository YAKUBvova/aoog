from PIL import Image,ImageDraw

width = 960
height = 540
white = (255, 255, 255)
filename = "ds8.jpg"

image1=Image.new("RGB", (width, height), white)
draw = ImageDraw.Draw(image1)
file = open('DS8.txt', 'r')
while True:
    line = file.readline()
    line = line.split()
    if not line:
        break
    x = int(line[1])
    y = int(line[0])
    draw.line([x, height-y, x+1,height-y], (0,0,0))
file.close()
image1.save(filename)
