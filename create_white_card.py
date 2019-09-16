from PIL import Image, ImageDraw, ImageFont

def create_card(size, bg, txtc):

    img = Image.new('RGB', size, color = bg)

    fnt = ImageFont.truetype('arial.ttf', 15)
    d = ImageDraw.Draw(img)
    d.text((55,275), "cards egueinst iumaniti", font=fnt, fill=txtc)

    return img

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

def add_bottom_logo(img):

    offset = (20, 270)
    logo = Image.open('Logo.png')
    logo.thumbnail((30,30))
    img.paste(logo, offset, mask=logo)

    return img



if __name__ == '__main__':

    size = (230, 302)
    white = (255, 255, 255)
    black = (0, 0, 0)
    rad = 20

    img = create_card(size, black, white)
    img = add_corners(img, rad)
    img = add_bottom_logo(img)

    img.save('black_card.png')
