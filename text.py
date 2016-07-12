from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import random

# using the data from sql we create a lot of text object, they all are in the text_object_list
# with a for loop we calculate their length (calculate_length method)
# the order list class method creates a list with the texts, ordered by the lengths of them
# the x coordinates are fixed, the find_place instance method sets up all the y coordinates (in a for loop)
# we use the place method, again in a for loop - all the text is written

class Text():

    text_object_list = []
    ordered_list = []
    not_empty_pixels = []
    check_ratio = [1, 1]

    def __init__(self, content, size, color, font, opacity):

        self.content = content
        self.size = size
        self.color = color
        if self.color == ():
            self.color = (0, 0, 0)
        self.font = font
        self.font_type = None
        self.opacity = opacity
        self.length = 0
        self.y = 0
        self.x = 0
        Text.text_object_list.append(self)

    def place(self, img, rotate_rate=0):

        self.font_type = ImageFont.truetype(self.font, self.size)
        img = img.rotate(rotate_rate, expand=1)
        draw = ImageDraw.Draw(img)
        draw.text((self.x, self.y), self.content, self.color, self.font_type)
        img = img.rotate(rotate_rate*(-1), expand=1)
        return img

    def findPlace_halfPyramid(self):

        number_x = 0

        for text in Text.ordered_list:
            if self.content == text.content:
                break
            else:
               number_x += 1

        y_coordinate = 0
        if number_x == 0:
            y_coordinate = 0
        else:
            for text in Text.ordered_list[:number_x]:
                y_coordinate += text.size
        self.y = y_coordinate

    def calculate_length(self, img):

        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype(self.font, self.size)
        content = self.content
        text_size = draw.textsize(content, font)
        self.length = text_size[0]

    @classmethod
    def order_list(cls):

        list_of_lengths = []
        for text in cls.text_object_list:
            list_of_lengths.append(text.length)
        list_of_lengths = reversed(sorted(list_of_lengths))
        for length in list_of_lengths:
            for text in cls.text_object_list:
                if text.length == length:
                    cls.ordered_list.append(text)
                    cls.text_object_list.remove(text)

    def occupyPlace(self):

        for x in range(self.x, (self.x + self.length+1)):
            for y in range(self.y, (self.y+self.size+1), Text.check_ratio[1]):
                Text.not_empty_pixels.append([x, y])

        for y in range(self.y, (self.y + self.size + 1)):
            for x in range(self.y, (self.x + self.length + 1), Text.check_ratio[0]):
                Text.not_empty_pixels.append([x, y])

        for x in range(self.x, self.x + self.length+1):
            Text.not_empty_pixels.append([x, self.y+self.size])
        for y in range(self.y, self.y + self.size+1):
            Text.not_empty_pixels.append([self.x + self.length, y])

    def checkOverLap(self):

        for x in range(self.x, (self.x + self.length)):
            coordinates = [x, self.y]
            if coordinates in Text.not_empty_pixels:
                return True
            else:
                continue

        for x in range(self.x, (self.x + self.length)):
            coordinates = [x, self.y+self.size]
            if coordinates in Text.not_empty_pixels:
                return True
            else:
                continue

        for y in range(self.y, (self.y + self.size)):
            coordinates = [self.x, y]
            if coordinates in Text.not_empty_pixels:
                return True
            else:
                continue

        for y in range(self.y, (self.y + self.size)):
            coordinates = [self.x + self.length, y]
            if coordinates in Text.not_empty_pixels:
                return True
            else:
                continue

        return False

    def randomPlace(self, img):

        placed = False
        while not placed:
            self.x = random.randint(100, 1100-self.length)
            self.y = random.randint(100, 1100-self.size)
            self.calculate_length(img)
            is_overlap = self.checkOverLap()
            if is_overlap is False:
                placed = True
                self.occupyPlace()
                img = self.place(img)
                return img
            else:
                print("...")
                continue

    @classmethod
    def checkOccupyRatio(cls):

        lengths = []
        for text in cls.text_object_list:
            lengths.append(text.length)
        cls.check_ratio[0] = (min(lengths))-1
        heights = []
        for text in cls.text_object_list:
            heights.append(text.size)
        cls.check_ratio[1] = (min(heights))-1