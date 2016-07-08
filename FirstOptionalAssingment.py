from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from sqlhandling import Sql
from text import Text

Sql.openDataBase('TothBalint', 'postgres', 'localhost', 'pw')
Sql.writeQuery('''select manager, max(budget_value) from project
group by manager order by max(budget_value) desc
limit 5''')
first_tuple_list = Sql.getData()
first_list = [list(tuple) for tuple in first_tuple_list]

picture = Image.new("RGB", (400, 1000), "white")

for text_info in first_list:
    text = Text(text_info[0], 10*(first_list.index(text_info)+1), (255, 255, 255), "Fonts/Capture_it.ttf", 255)

for text in Text.text_object_list:
    text.calculate_length(picture)

Text.order_list()
for text in Text.ordered_list:
    text.findPlace_halfPyramid()

how_high = int((Text.ordered_list[-1].y + Text.ordered_list[-1].size)*3.5)
how_wide = int(Text.ordered_list[0].length*1.5)

picture = Image.new("RGB", (how_wide, how_high), "black")

rotate_rates = [0, 90, 180, 270]
for rotate_rate in rotate_rates:
    for text in Text.ordered_list:
        picture = text.place(picture, rotate_rate)

porn = Text("Porn", 55, (255, 0, 0), "Fonts/Y2k Subterran Express KG.ttf", 255)
porn.calculate_length(picture)

star = Text("StarZ", 55, (255, 0, 0), "Fonts/Y2k Subterran Express KG.ttf", 255)
star.calculate_length(picture)

porn.x = int(how_wide/2)-150
porn.y = int(how_high/2)-40
picture = porn.place(picture)
star.x = int(how_wide/2)-35
star.y = int(how_high/2)+30
picture = star.place(picture)

picture.save("ThirdPicture.png")