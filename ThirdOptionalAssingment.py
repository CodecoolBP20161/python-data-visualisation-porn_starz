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

picture = Image.new("RGB", (5000, 5000), "black")

for text_info in first_list:
    text = Text(text_info[0], (text_info[1])*30, (255, 0, 0), "Fonts/Capture_it.ttf", 255)

for text in Text.text_object_list:
    text.calculate_length(picture)

Text.checkOccupyRatio()

Text.order_list()
percent = 0
count = 0
for text in Text.ordered_list:
    picture = text.randomPlace(picture)
    count += 1
    percent = int(count/len(first_list)*100)
    print(str(percent) + " % completed\nWorking...")

picture.save("ThirdOptionalAssingment10.png")