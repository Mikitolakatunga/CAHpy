import glob
import os
from PIL import Image, ImageOps, ImageDraw


pathtocopy = "cahpy\\mazos\\Base_exp\\"
path_parent = os.getcwd()
images = glob.glob(path_parent+r"\IMPRIMIR_CAH\MAZO_2\Blancas\*.png")
images_with_border = []
for idx, image in enumerate(images):
    with open(image, 'rb') as file:
        img = Image.open(file)
        # img.show()
        cutimg = img.crop([13,900,700,1000])
        print(image)
        # cutimg.show()
        imgdraw = ImageDraw.Draw(img)
        imgdraw.rectangle([13,900,700,1000],outline='white',fill='white')
        img.paste(cutimg,[35,900])
        # img.show()
        # break
        img.save(image)