from PIL import Image, ImageDraw, ImageFont, ImageOps
import sys
import os

from pathlib import Path


class Card(object):
    """docstring for Card."""

    def __init__(self, size, bg):
        super(Card, self).__init__()
        self.size = size
        self.img = Image.new('RGB', size, color = bg)

    def setTxtcolor(self, color):
        self.txtcolor = color

    def setTxtsize(self, size):
        self.txtsize = size

    def seticon(self, icon):
        self.icon = Image.open(icon).convert("RGBA")

    def drawicon(self):
        self.icon.thumbnail((100,100))
        self.img.paste(self.icon, [15,900], mask=self.icon)

    def setbottomtext(self, text):
        self.bottomtxt = text

    def settext(self, text):
        self.txt = text

    def setfont(self,font):
        self.font = font

    def setfont2(self,font):
        self.font2 = font

    def write_text(self):
        lines = text_wrap(self.txt, self.font, self.img.size[0])
        line_height = get_line_height(self.font)
        self.img = write_text(40, 40, self.img, self.txt, self.font, self.txtcolor)

    def write_btext(self):
        d = ImageDraw.Draw(self.img)
        d.text((140,930), self.bottomtxt, font=self.font2, fill=self.txtcolor)

    def add_border(self, border):

        if isinstance(border, int) or isinstance(border, tuple):
            self.img = ImageOps.expand(self.img, border=border)
        else:
            raise RuntimeError('Border is not an integer or tuple!')

def generate_CAH_cards(doc, type):
    f = open(doc, "r")
    lines = f.readlines()
    for line in lines:
        if type == 'white':
            color = 'black'
        elif type == 'black':
            color = 'white'

        carta = Card(size, type)

        carta.setfont(ImageFont.truetype(RobotoMono_Medium, 60))
        carta.setfont2(ImageFont.truetype(RobotoMono_Medium, 40))

        carta.settext(line)
        carta.setbottomtext(btext)
        carta.setTxtcolor(color)
        carta.seticon(logo)

        carta.drawicon()
        carta.write_text()
        carta.write_btext()

        carta.add_border(borde)

        # carta.img.show()
        name = line.rstrip() + '.png'
        name = name.replace(' ', '_')
        name = name.replace('?', '')
        name = name.replace('¿', '')
        name = name.replace(':', '')
        carta.img.save(f"{dir}/{type}_cards/{name}")

        print(name + ' saved')
    print("FINISHED!!")

def add_corners(im, rad):
    circle = Image.new('L', (rad * 2, rad * 2), 255)
    draw = ImageDraw.Draw(circle)
    draw.ellipse((0, 0, rad * 2, rad * 2), fill=0)
    alpha = Image.new('L', im.size, "black")
    w, h = im.size
    im.paste(circle.crop((0, 0, rad, rad)), (0, 0))
    im.paste(circle.crop((0, rad, rad, rad * 2)), (0, h - rad))
    im.paste(circle.crop((rad, 0, rad * 2, rad)), (w - rad, 0))
    im.paste(circle.crop((rad, rad, rad * 2, rad * 2)), (w - rad, h - rad))
    # im.putalpha(alpha)

    return im
def text_wrap(text, font, max_width):
    lines = []
    # If the width of the text is smaller than image width
    # we don't need to split it, just add it to the lines array
    # and return
    if font.getsize(text)[0] <= max_width - 60:
        lines.append(text)
    else:
        # split the line by spaces to get words
        words = text.split(' ')
        i = 0
        # append every word to a line while its width is shorter than image width
        while i < len(words):
            line = ''
            while i < len(words) and font.getsize(line + words[i])[0] <= max_width - 60:
                line = line + words[i] + " "
                i += 1
            if not line:
                line = words[i]
                i += 1
            # when the line gets longer than the max width do not append the word,
            # add the line to the lines array
            lines.append(line)
    return lines

def draw_text(text, size, bg):
    # open the background file
    img = Image.open(bg)

    # size() returns a tuple of (width, height)
    image_size = img.size

    # create the ImageFont instance
    font_file_path = 'arial.ttf'
    font = ImageFont.truetype(font_file_path, size=size)

    # get shorter lines
    lines = text_wrap(text, font, image_size[0])
    print(lines) # ['This could be a single line text ', 'but its too long to fit in one. ']

def write_text(x, y, img, text, font, color):

    lines = text_wrap(text, font, img.size[0])
    line_height = get_line_height(font)
    draw = ImageDraw.Draw(img)

    # x = 10
    # y = 20

    for line in lines:
        # print(line)
        draw.text((x, y), line, fill=color, font=font)
        y = y + line_height

    return img

def get_line_height(ft):

    line_height = ft.getsize('hg')[1]

    return line_height

if __name__ == '__main__':
    dir = os.getcwd()

    # doc = 'CARTAS_BLANCAS.txt'
    doc = 'CARTAS_NEGRAS.txt'
    # doc = 'EUITI_blancas.txt'
    # doc = 'EUITI_negras.txt'

    type = 'black'
    Path(f"{dir}/{type}_cards").mkdir(parents=True, exist_ok=True)

    RobotoMono_Light = 'C:/Users/mikit/AppData/Local/Microsoft/Windows/Fonts/RobotoMono-Light.ttf'
    RobotoMono_Medium = 'C:/Users/mikit/AppData/Local/Microsoft/Windows/Fonts/RobotoMono-Medium.ttf'

    btext = 'Cards Against Humanity'
    size = (737, 1020)
    borde = 2
    logo = 'Logo3.png'
    # logo = 'Logo4.png'

    generate_CAH_cards(doc, type)
