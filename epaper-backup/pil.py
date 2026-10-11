import sys
import os
from PIL import Image,ImageDraw,ImageFont
from IPython.display import display

picdir = './'
#font24 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 24)

output = Image.new( 'RGB', (480,800), "black")
#display(MyImg)
#MyImg.show()
Himage = Image.open('mrbeast4.bmp')
#draw = ImageDraw.Draw(Himage)
#draw.text((20, 20), u'Mr.Beast', font = font24, fill = 0)

pixels = Himage.load()
W = Himage.size[0]
L = Himage.size[1]
WindowLength = {
    0: W/3, #160
    1: W/15, #32
    2: W/30,
    3: W/60,
    4: W/120,
    5: W/240,
    6: W/480
}
NumRound =int(sys.argv[1])
for rnd in range(0, NumRound):
    minMatrix = {}
    for i in range(W): # 480
        xx = int(i / WindowLength[rnd])
        for j in range(L): # 800
            yy = int(j / WindowLength[rnd])
            if (xx, yy) not in minMatrix:
                minMatrix[xx, yy] = 0
            if pixels[i, j][0] > minMatrix[(xx, yy)]: 
                minMatrix[xx, yy] = pixels[i, j][0]
for i in range(W):
    for j in range(L):
        xx = int(i / WindowLength[rnd])
        yy = int(j / WindowLength[rnd])
        val = int(minMatrix[xx, yy])
        pixels[i,j] = (val, val, val)
#                         i       j
#rnd 6: 480  800,      
#rnd 5: 240  400, 
#rnd 4: 120  200, 
#rnd 3:  60  100, 
#rnd 2:  30   50,  
#rnd 1:  15   25,   32(=480/15)  32(=800/25)
#rnd 0    3    5,   160(=480/3)  160(=800/5)

display(Himage)
Himage.show()

