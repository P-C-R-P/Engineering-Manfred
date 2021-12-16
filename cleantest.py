import re
with open('test.txt', 'r', encoding="utf-8") as file:
    data = file.read()
"""
new_data = ""

pattern = re.compile(r'(ACT\s[I]{1}[\w\W\n\s]*)(ACT\s[I]{2}[\w\W\n\s]*)(ACT\s[I]{3}[\w\W\n\s]*)')

matches = re.finditer(r'(ACT\s[I]{1}[\w\W\n\s]*)(ACT\s[I]{2}[\w\W\n\s]*)(ACT\s[I]{3}[\w\W\n\s]*)', data)
matchesall = re.findall(r'(ACT\s[I]{1}[\w\W\n\s]*)(ACT\s[I]{2}[\w\W\n\s]*)(ACT\s[I]{3}[\w\W\n\s]*)', data)
matches2 = pattern.findall(data)
matches3 = re.search(r'(ACT\s[I]{1}[\w\W\n\s]*)(ACT\s[I]{2}[\w\W\n\s]*)(ACT\s[I]{3}[\w\W\n\s]*)', data)
"""




"""
for i in range(1,4):
    new_data += "<div1" + " type=\"act\" n=\"" + str(i) + "\">" + matches3.group(i) + "</div1" + ">"


data = re.sub(r"(ACT\s[I]{1}[\w\W\n\s]*)ACT\s[I]{2}\W", r'<div1 type="act" n="1">\1</div1>ACT II.', data)
data = re.sub(r"(ACT\s[I]{2}[\w\W\n\s]*)ACT\s[I]{3}\W", r'<div2 type="act" n="2">\1</div2>ACT III.', data)
data = re.sub(r"(ACT\s[I]{3}[\w\W\n\s]*).", r'<div3 type="act" n="3">\1</div3>', data)
"""


with open('test2.txt', 'w', encoding="utf-8") as file:
    file.write(data)


## regex for ACTS --- ACT\s[I]+
## (ACT\s[I]{1}[\w\W\n\s]*)ACT\s[I]{2}\W
## (ACT\s[I]{1}\W\n*\s*[\w\W]*)ACT\s[I]{2}\W
## (ACT\s[I]{1}[\w\W\n\s]*)ACT\s[I]{2}\W