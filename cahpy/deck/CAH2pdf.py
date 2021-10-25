import glob
import os
from PIL import Image, ImageOps

path_parent = os.getcwd()
images = glob.glob(path_parent+r"\IMPRIMIR_CAH\MAZO_2\Blancas\*.png")
images_with_border = []
for idx, image in enumerate(images):
    with open(image, 'rb') as file:
        img = Image.open(file)
        border = int(3.2*300/25.4)
        img_with_border = ImageOps.expand(img,border=border,fill='white')
        img_with_border.save('imaged-with-border.png')
        images_with_border.append(img_with_border)
        print(image)
        # img.show()

im1 = images_with_border.pop(0)
im1.save(os.path.join(path_parent,"EXP1_BLANCAS")+".pdf", "PDF", resolution=300.0, save_all=True, append_images=images_with_border)