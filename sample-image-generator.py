from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

img = Image.open('sample-out.png')
im = img.rotate(90, expand=1)
im.save('sample-out.png')
draw = ImageDraw.Draw(im)
# font = ImageFont.truetype(<font-file>, <font-size>)base_data.sql:11
# font = ImageFont.truetype("sans-serif.ttf", 16)
text_options = {
    'fill': (140, 45, 255)
}
text_content = "Mukodik a forgatas!!!!!!!!"
text_size = draw.textsize(text_content)

# draw.text((x, y),text_content,(r,g,b))
draw.text((0, 0), text_content, **text_options)
draw.text((0, text_size[1]), text_content, **text_options)
draw.text((text_size[0], 0), text_content, **text_options)
draw.text(text_size, text_content, **text_options)
im.save('sample-out.png')
