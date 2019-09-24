from create_card import *
from draw_mtext import *
import sys
import os

size = (230, 261)
bottom_t = 'Cards Against EUITI'
font = ImageFont.truetype('consola.ttf', 25)
dir = os.getcwd()

def generate_CAH_cards(text, type):

    f = open(text, "r")
    lines = f.readlines()
    for line in lines:
        if type == 'white':
            img = create_white(size, bottom_t)
            color = 'black'
        elif type == 'black':
            img = create_black(size, bottom_t)
            color = 'white'
        card = write_text(10, 20, img, line, font, color)
        name = line.rstrip() + '.png'
        name = name.replace(' ', '_')
        name = name.replace('?', '')
        name = name.replace('¿', '')
        name = name.replace(':', '')
        card.save(f"{dir}/{type}_cards/{name}", optimize=True)

        print(name + ' saved')

if __name__ == '__main__':
    txt = sys.argv[1]
    type = sys.argv[2]
    generate_CAH_cards(txt, type)
    print("FINISHED!!")
