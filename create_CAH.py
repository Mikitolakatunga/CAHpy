from create_card import *
from draw_mtext import *


size = (230, 261)
bottom_t = 'Cards Against Humanity'
font = ImageFont.truetype('consolab.ttf', 25)
dir = "D:/PyProjects/CAHpy/Example_Cards/"


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
        card.save(dir + name, optimize=True)

        print(name + ' saved')

if __name__ == '__main__':
    generate_CAH_cards("Random_words.txt", 'white')
