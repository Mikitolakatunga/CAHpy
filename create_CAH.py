from create_white_card import *
from draw_mtext import *


f = open("Random_words.txt", "r")

lines = f.readlines()
for line in lines:
    print(line)
