from PIL import Image, ImageDraw, ImageFont

# Create Image object with the imput image
image = Image.open('background.png')

draw = ImageDraw.Draw(image)

font = ImageFont.truetype('arial.ttf', size=45)

# starting position of the message

(x, y) = (50, 50)
message = "Happy Birthday!"
color = (0, 0, 0, 255)# black color

draw.text((x, y), message, fill=color, font=font)

(x, y) = (150, 150)
name = 'Vinay'
color = (255, 255, 255, 0)# white color
draw.text((x, y), name, fill=color, font=font)

# save the edited image

image.save('greeting_card.png')
