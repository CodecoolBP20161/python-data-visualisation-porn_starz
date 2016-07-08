from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from sqlhandling import Sql
from text import Text

Sql.openDataBase('TothBalint', 'postgres', 'localhost', 'pw')
Sql.writeQuery(''' SELECT company_name as "Companies", count(company_name) as "Projects" FROM project
GROUP BY company_name ORDER BY count(company_name) DESC''')
first_tuple_list = Sql.getData()
first_list = [list(tuple) for tuple in first_tuple_list]

for i in range(len(first_list)):
    Sql.writeQuery(''' SELECT main_color FROM project WHERE company_name='%s' and main_color IS NOT NUll;''' % str(first_list[i][0]))
    new_list = Sql.getData()
    first_list[i].append(new_list)
for color_list in first_list: # [company_name, projects,  [(hex1,), (hex2)...]]
    for i in range(len(color_list[2])):
        color_list[2][i] = list(color_list[2][i][0][1:])
        for y in range(len(color_list[2][i])):
            color_list[2][i][y] = (int(color_list[2][i][y], 16))*17
        r, g, b = 0, 0, 0
        r += color_list[2][i][0]
        g += color_list[2][i][1]
        b += color_list[2][i][2]
    if color_list[2] != []:
        r = int(r/len(color_list[2]))
        g = int(g / len(color_list[2]))
        b = int(b / len(color_list[2]))
        color_list[2] = [r, g, b]
    else:
        continue

picture = Image.new("RGB", (400, 1000), "white")

for text_info in first_list:
    text = Text(text_info[0], text_info[1]*5, tuple(text_info[2]), "Fonts/Capture_it.ttf", 255)

for text in Text.text_object_list:
    text.calculate_length(picture)

Text.order_list()
for text in Text.ordered_list:
    text.findPlace_halfPyramid()

how_high = Text.ordered_list[-1].y + Text.ordered_list[-1].size
how_wide = Text.ordered_list[0].length

picture = Image.new("RGB", (how_wide, how_high), "white")

for text in Text.ordered_list:
    picture = text.place(picture)

title = Text("Porn_Stars", 40, (255, 0, 0), "Fonts/Capture_it.ttf", 255)
title.calculate_length(picture)
title.x = how_high - title.length
title.y = 0
picture = title.place(picture, 90)
picture.save("FirstPicture.png")