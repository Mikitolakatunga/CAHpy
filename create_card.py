from PIL import Image, ImageDraw, ImageFont

def create_card(size, bg, txtc):

    img = Image.new('RGB', size, color = bg)

    return img

def add_black_corners(im, rad):
    circle = Image.new('L', (rad * 2, rad * 2), 0)
    draw = ImageDraw.Draw(circle)
    draw.ellipse((0, 0, rad * 2, rad * 2), fill=255)
    alpha = Image.new('L', im.size, "white")
    w, h = im.size
    im.paste(circle.crop((0, 0, rad, rad)), (0, 0))
    im.paste(circle.crop((0, rad, rad, rad * 2)), (0, h - rad))
    im.paste(circle.crop((rad, 0, rad * 2, rad)), (w - rad, 0))
    im.paste(circle.crop((rad, rad, rad * 2, rad * 2)), (w - rad, h - rad))

    return im

def add_corners(im, rad):
    circle = Image.new('L', (rad * 2, rad * 2), 0)
    draw = ImageDraw.Draw(circle)
    draw.ellipse((0, 0, rad * 2, rad * 2), fill=255)
    alpha = Image.new('L', im.size, "white")
    w, h = im.size
    alpha.paste(circle.crop((0, 0, rad, rad)), (0, 0))
    alpha.paste(circle.crop((0, rad, rad, rad * 2)), (0, h - rad))
    alpha.paste(circle.crop((rad, 0, rad * 2, rad)), (w - rad, 0))
    alpha.paste(circle.crop((rad, rad, rad * 2, rad * 2)), (w - rad, h - rad))
    im.putalpha(alpha)

    return im

def add_bottom_logo(img, txtc, bottom_t):

    fnt = ImageFont.truetype('consola.ttf', 15)
    d = ImageDraw.Draw(img)
    d.text((40,234), bottom_t, font=fnt, fill=txtc)

    offset = (5, 229)
    logo = Image.open('Logo.png')
    logo.thumbnail((30,30))
    img.paste(logo, offset, mask=logo)

    return img

def create_white(size, bottom_t):

    img = create_card(size, 'white', 'black')
    img = add_black_corners(img, 20)
    img = add_bottom_logo(img, 'black', bottom_t)

    # img.save('white_card.png')
    return img

def create_black(size, bottom_t):

    img = create_card(size, 'black', 'white')
    img = add_corners(img, 20)
    img = add_bottom_logo(img, 'white', bottom_t)

    # img.save('black_card.png')
    return img


if __name__ == '__main__':

    size = (230, 261)
    bottom_t = 'Cards Against Humanity'
    # white = 255
    # black = 0
    # rad = 20

    black_c = create_black(size, bottom_t)
    white_c = create_white(size, bottom_t)

    black_c.save('black_card.png')
    white_c.save('white_card.png')
