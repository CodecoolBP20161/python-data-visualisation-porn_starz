from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

class text():

    text_object_list = []

    def __init__(self, content, size, color, font, opacity):

        self.content = content
        self.size = size
        self.color = color
        self.font = font
        self.opacity = opacity
        text.text_object_list.append(self)

    def place(self, img, coordinates, rotate_rate=0):

        img.rotate(rotate_rate, expand=1)
        draw = ImageDraw.Draw(img)
        draw.text((coordinates[0], coordinates[1]), self.content, self.color, self.font)
        img.rotate(rotate_rate*(-1), expand=1)
        return img

    def findPlace(self):

        y_coordinate = 0
        for text in text.text_object_list:
            y_coordinate += text.textsize[1]
        return [0, y_coordinate]












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
