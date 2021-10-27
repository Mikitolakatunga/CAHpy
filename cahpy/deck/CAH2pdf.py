import glob
import os
from PIL import Image, ImageOps, ImageDraw

sangria = int(6*300/25.4)
margen = int(2.2*300/25.4)
m_total = sangria+margen
width_in = 1
width_out = 2

def DrawHorizontalMark(mark_y, mark_lenght,side,img):

    img_draw = ImageDraw.Draw(img)
    width, height = img.size
    print(width)
    print(width-mark_lenght)
    if side == 'left':  
        img_draw.line([0,mark_y-2,mark_lenght,mark_y-2],fill='white',width=width_out)
        img_draw.line([0,mark_y+2,mark_lenght,mark_y+2],fill='white',width=width_out)
        img_draw.line([0,mark_y,mark_lenght,mark_y],fill='black',width=width_in)
    elif side == 'right':  
        img_draw.line([width-mark_lenght,mark_y-2,width,mark_y-2],fill='white',width=width_out)
        img_draw.line([width-mark_lenght,mark_y+2,width,mark_y+2],fill='white',width=width_out)
        img_draw.line([width-mark_lenght,mark_y,width,mark_y],fill='black',width=width_in)
    return img

def DrawVerticalMark(mark_x, mark_lenght,side,img):

    img_draw = ImageDraw.Draw(img)
    width, height = img.size
    print(width)
    print(width-mark_lenght)
    if side == 'top':  
        img_draw.line([mark_x-2,0,mark_x-2,mark_lenght],fill='white',width=width_out)
        img_draw.line([mark_x+2,0,mark_x+2,mark_lenght],fill='white',width=width_out)
        img_draw.line([mark_x,0,mark_x,mark_lenght],fill='black',width=width_in)
    elif side == 'bottom':  
        img_draw.line([mark_x-2,height-mark_lenght,mark_x-2,height],fill='white',width=width_out)
        img_draw.line([mark_x+2,height-mark_lenght,mark_x+2,height],fill='white',width=width_out)
        img_draw.line([mark_x,height-mark_lenght,mark_x,height],fill='black',width=width_in)
    return img
    

if __name__ == '__main__':
    path_parent = os.getcwd()
    images = glob.glob(path_parent+r"\IMPRIMIR_CAH\MAZO_1\Negras\*.png")
    images_with_border = []
    for idx, image in enumerate(images):
        with open(image, 'rb') as file:
            img = Image.open(file)
            # img.show()
            img_with_border = ImageOps.expand(img,border=margen,fill='black')
            # img_with_border.show()
            img_with_border = ImageOps.expand(img_with_border,border=sangria,fill='white')
            # img_with_border.show()
            width, height = img_with_border.size
            images_with_border.append(img_with_border)
            # print(image)
            img_with_border = DrawHorizontalMark(m_total,m_total*0.85,'left',img_with_border)
            img_with_border = DrawHorizontalMark(m_total,m_total*0.85,'right',img_with_border)
            img_with_border = DrawHorizontalMark(height-m_total,m_total*0.85,'left',img_with_border)
            img_with_border = DrawHorizontalMark(height-m_total,m_total*0.85,'right',img_with_border)

            img_with_border = DrawVerticalMark(m_total,m_total*0.85,'top',img_with_border)
            img_with_border = DrawVerticalMark(m_total,m_total*0.85,'bottom',img_with_border)
            img_with_border = DrawVerticalMark(width-m_total,m_total*0.85,'top',img_with_border)
            img_with_border = DrawVerticalMark(width-m_total,m_total*0.85,'bottom',img_with_border)
            img_with_border.show()

            break

    im1 = images_with_border.pop(0)
    im1.save(os.path.join(path_parent,"EXP1_BLANCAS")+".pdf", "PDF", resolution=300.0, save_all=True, append_images=images_with_border)