from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

# using the data from sql we create a lot of text object, they all are in the text_object_list
# with a for loop we calculate their length (calculate_length method)
# the order list class method creates a list with the texts, ordered by the lengths of them
# the x coordinates are fixed, the find_place instance method sets up all the y coordinates (in a for loop)
# we use the place method, again in a for loop - all the text is written

class Text():

    text_object_list = []
    ordered_list = []

    def __init__(self, content, size, color, font, opacity):

        self.content = content
        self.size = size
        self.color = color
        self.font = font
        self.opacity = opacity
        self.length = 0
        self.y = 0
        self.x = 0
        Text.text_object_list.append(self)

    def place(self, img, rotate_rate=0):

        img.rotate(rotate_rate, expand=1)
        draw = ImageDraw.Draw(img)
        draw.text((self.x, self.y), self.content, self.color, self.font)
        img.rotate(rotate_rate*(-1), expand=1)
        return img

    def findPlace(self):

        number_x = 0

        for text in text.ordered_list:
            if self.content == text.content:
                break
            else:
               number_x += 1

        y_coordinate = 0
        if number_x == 0:
            y_coordinate = 0
        else:
            for text in text.ordered_list[:number_x]:
                y_coordinate += text.size[1]
        self.y = y_coordinate

    def calculate_length(self):

        font = ImageFont.truetype(self.font, self.size)
        content = self.content
        text_size = draw.textsize(content, font)
        self.length = text_size[1]

    @classmethod
    def order_list(cls):

        list_of_lengths = []
        for text in cls.text_object_list:
            list_of_lengths.append(text.length)
        list_of_lengths = reverse(sort(list_of_lengths))
        for length in list_of_lengths:
            for text in cls.text_object_list:
                if text.length == length:
                    cls.ordered_list.append(text)
                    cls.text_object_list.remove(text)

