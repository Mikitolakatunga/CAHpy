from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

def text_wrap(text, font, max_width):
    lines = []
    # If the width of the text is smaller than image width
    # we don't need to split it, just add it to the lines array
    # and return
    if font.getsize(text)[0] <= max_width:
        lines.append(text)
    else:
        # split the line by spaces to get words
        words = text.split(' ')
        i = 0
        # append every word to a line while its width is shorter than image width
        while i < len(words):
            line = ''
            while i < len(words) and font.getsize(line + words[i])[0] <= max_width:
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
        print(line)
        draw.text((x, y), line, fill=color, font=font)
        y = y + line_height

    return img



def get_line_height(ft):

    line_height = ft.getsize('hg')[1]

    return line_height

if __name__ == '__main__':

    # font = ImageFont.truetype('arial.ttf', 25)
    text = "This could be a single line text but its too long to fit in one."
    # color = "black"
    #
    # img = Image.open("white_card.png")
    # image_size = img.size
    #
    # lines = text_wrap(text, font, image_size[0])
    # line_height = get_line_height(font)
    # draw = ImageDraw.Draw(img)
    #
    # x = 10
    # y = 20
    #
    # for line in lines:
    #     print(line)
    #     draw.text((x, y), line, fill=color, font=font)
    #     y = y + line_height
    img = Image.open("white_card.png")
    font = ImageFont.truetype('arial.ttf', 25)
    card = write_text(10, 20, img, text, font, "black")
    card.save('white_card_mline.png', optimize=True)
