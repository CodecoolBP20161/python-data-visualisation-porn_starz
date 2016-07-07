from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from sqlhandling import Sql
from text import Text
import random
picture = Image.new("RGB", (1500, 1500), "Cyan")
Sql.openDataBase('csibi', 'csibi', 'localhost', 'csibi')
Sql.writeQuery(''' SELECT name, budget_value, budget_currency, main_color FROM project
WHERE project IS NOT NULL;''')
first_tuple_list = Sql.getData()
fonttype_list = ["Fonts/Capture_it.ttf", "Fonts/OpenSans-Bold.ttf", "Fonts/AlexBrush-Regular.ttf",
                 "Fonts/Capture_it_2.ttf", "Fonts/FFF_Tusj.ttf", "Fonts/Pacifico.ttf", "Fonts/SEASRN__.ttf"]

# Formatting the SQL data so the text object can be created
first_list = [list(tuple) for tuple in first_tuple_list]

# Changing the currency to EUR
for project in first_list:
    if project[2] == "USD":
        project[1] = int(float(project[1]) * 0.9)
    elif project[2] == "GBP":
        project[1] = int(float(project[1]) * 1.17)
    else:
        project[1] = int(float(project[1]))
    project[2] = "EUR"

# Getting rid of the "#" symbol and making a list from the color string
    project[3] = list(project[3].replace("#", ""))

# Converting the HEX colors to RGB colors to : [r, g, b]
    for i in range(len(project[3])):
        project[3][i] = int(project[3][i], 16)*17

# Creating the text objects(still inside the for cycle :) )
    text = Text(project[0], int((project[1] * 2) / 400), project[3], random.choice(fonttype_list), project[1]/100*2.7)
    text.calculate_length(picture)

# Sort the class list based on the object attribute size, which is based on the desired factor(budget)
Text.order_list()
# Na itt az ordered_list készen, már csak ki kell íratni a randommal. A fonttype_list-re nem fog hibát kiírni, megjavítottam :D
picture.save("SecondAssignment.png")