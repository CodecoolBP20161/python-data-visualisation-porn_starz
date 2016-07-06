from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from sqlhandling import Sql
import text


picture = Image.new("RGB", (1024, 1024), "gold")

Sql.openDataBase('csibi', 'csibi', 'localhost', 'csibi')
Sql.writeQuery(''' SELECT company_name as "Companies", count(company_name) as "Projects" FROM project
GROUP BY company_name ORDER BY count(company_name) DESC''')
first_tuple_list = Sql.getData()
first_list = [list(tuple) for tuple in first_tuple_list]

for i in range(len(first_list)):
    Sql.writeQuery(''' SELECT main_color FROM project WHERE company_name=%s and main_color IS NOT NUll;''' % str(first_list[i][0]))
    new_list = Sql.getData()
    first_list[i].append(new_list)
for list in first_list: # [company_name, projects,  [(hex1), (hex2)...]]
    for tuple in list[2]:
        tuple = str(tuple)
print(first_list)

