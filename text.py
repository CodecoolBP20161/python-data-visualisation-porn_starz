from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

class text():

    def __init__(self, content, size, color, font, opacity):

        self.content = content
        self.size = size
        self.color = color
        self.font = font
        self.opacity = opacity

    def place(self, img, x_coordinate, y_coordinate, rotate_rate=0):

        img.rotate(rotate_rate, expand=1)
        draw = ImageDraw.Draw(img)
        draw.text((x_coordinate, y_coordinate), self.content, self.color, self.font)
        img.rotate(rotate_rate*(-1), expand=1)
        return img

  









img = Image.new("RGB", (512, 512), "red")
draw = ImageDraw.Draw(img)
# font = ImageFont.truetype(<font-file>, <font-size>)
# font = ImageFont.truetype("sans-serif.ttf", 16)
text_options = {
    'fill': (255, 255, 255,255)
}
text_content = "Sample Text"
text_size = draw.textsize(text_content)
# draw.text((x, y),text_content,(r,g,b))
draw.text((0, 0), text_content, **text_options)
draw.text((0, text_size[1]), text_content, **text_options)
draw.text((text_size[0], 0), text_content, **text_options)
draw.text(text_size, text_content, **text_options)
img.save('sample-out.png')
