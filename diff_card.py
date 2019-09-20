from create_card import *
from draw_mtext import *
import sys

type = sys.argv[1]
text = sys.argv[2]
draw = sys.argv[3]
pick = sys.argv[4]

size = (230, 261)
bottom_t = 'Cards Against Humanity'
dir = "D:/PyProjects/CAHpy/Example_Cards/"
font = ImageFont.truetype('consolab.ttf', 25)
font2 = ImageFont.truetype('consolab.ttf', 20)
line_height = font2.getsize('hg')[1]

if type == 'white':
    card = create_white(size, bottom_t)
    card = write_text(10, 20, card, text, font, 'black')
    if draw != "0":
        card = write_text(40, 180, card, "Draw " + draw, font2, 'black')
    if pick != "0":
        card = write_text(40, 180 + line_height, card, "Pick " + pick, font2, 'black')
elif type == 'black':
    card = create_black(size, bottom_t)
    card = write_text(10, 20, card, text, font, 'white')
    if draw != "0":
        card = write_text(40, 180, card, "Draw " + draw, font2, 'white')
    if pick != "0":
        card = write_text(40, 180 + line_height, card, "Pick " + pick, font2, 'white')

name = text.rstrip() + '.png'
name = name.replace(' ', '_')
card.save(dir + name, optimize=True)
print(name + ' saved')
