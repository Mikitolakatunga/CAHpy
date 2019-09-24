from PIL import Image
import glob
import os
import sys

#opens an image:
dir = os.getcwd()
type = sys.argv[1]
im = Image.open(dir + f"/Back_Cards/{type}_back.png")
images = glob.iglob(f"{dir}/{type}_cards/*.png")
# for x in images:
#     print(x)

# print(im.size)
width = im.size[0]
height = im.size[1]

bgc = {'white': 0,
       'black': 255}

gap = 1
nwidth = width * 3 + 2 * gap
nheight = height * 4  + 3 * gap

page = 1
try:
    while images:
        new_page = Image.new('L', (nwidth , nheight), bgc[type])
        for i in range(0, nwidth, width+gap):
            for j in range(0, nheight, height+gap):
                image = next(images)
                print(str(i) + "\t"+ str(j) + "\t" + image)
                card = Image.open(image)
                new_page.paste(card, (i,j))
                new_page.save(f"{dir}/{type}_cards/Merged_page/{str(page)}.png")
        # new_page.show()
        print(f"Page {str(page)} saved")
        page += 1

except StopIteration:
    print(f"Page {str(page)} saved")
    print("finished")

##new_page = Image.new('L', (nwidth , nheight), bgc[type])
##for i in range(0, nwidth, width+gap):
##    for j in range(0, nheight, height+gap):
##        new_page.paste(im, (i,j))
##new_page.save(f"{dir}/Back_Cards/Merged_back_{type}.png")
