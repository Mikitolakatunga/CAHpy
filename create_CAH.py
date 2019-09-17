from create_white_card import *
from draw_mtext import *


size = (230, 261)
bottom_t = 'cards egueinst iumaniti'
font = ImageFont.truetype('arial.ttf', 25)


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
        card = write_text(img, line, font, color)
        card.save("C:/SPB_Data/github/CAHpy/Example_Cards/" + line.rstrip() + '.png', optimize=True)

if __name__ == '__main__':
    generate_CAH_cards("Random_words.txt", 'black')
