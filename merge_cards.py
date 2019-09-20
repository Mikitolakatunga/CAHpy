from PIL import Image

#opens an image:
im = Image.open("D:/PyProjects/CAHpy/Back_Cards/white_back.png")

print(im.size)
width = im.size[0]
height = im.size[1]

gap = 3
nwidth = width * 3 + 2*gap
nheight = height * 4  + 3*gap

new_im = Image.new('RGB', (nwidth , nheight))

for i in range(0, nwidth + width, width+gap):
    for j in range(0, nheight + height, height+gap):
        new_im.paste(im, (i,j))

new_im.show()
