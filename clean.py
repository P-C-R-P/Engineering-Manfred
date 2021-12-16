import re
with open('manfred2.txt', 'r', encoding="utf-8") as file:
    data = file.read()

data = data.replace('_', '')

new = re.split('DRAMATIS', data)
for i in new:
    print(i)

data = "DRAMATIS" + new[1]

new2 = re.split('FOOTNOTES', data)
for i in new2:
    print(i)

data = new2[0]

# matches footnotes in text
data = re.sub("\[\d{3}\]", '', data)
# converts ACT 1 to roman numerals (inconsistent Gutenberg number schemes)
data = re.sub("ACT\s\d", 'ACT I', data)
# converts SCENE 1 to roman numerals
data = re.sub("SCENE\s\d", 'SCENE I', data)

# add act 1 div
data = re.sub(r"(ACT\s[I]{1}[\w\W\n\s]*)ACT\s[I]{2}\W", r'<div1 type="act" n="1">\1</div1>ACT II.', data)
# add act 2 div
data = re.sub(r"(ACT\s[I]{2}[\w\W\n\s]*)ACT\s[I]{3}\W", r'<div1 type="act" n="2">\1</div1>ACT III.', data)
# add act 3 div
data = re.sub(r"(ACT\s[I]{3}[\w\W\n\s]*).", r'<div1 type="act" n="3">\1</div1>', data)
# add scene1 div
data = re.sub(r"(SCENE\s[I]{1}\.[\w\W\n\s]*?)SCENE\s[I]{2}\.", r'<div2 type="scene" n="1">\1</div2> SCENE II.', data)
#add act1,scene2 div - le parametre count limite le nbr de remplacements
data = re.sub(r"(SCENE\s[I]{2}\.[\w\W\n\s]*?closes.)", r'<div2 type="scene" n="2">\1</div2>', data, count=1)
#add act 2,3 scene 2 div
data = re.sub(r"(SCENE\s[I]{2}\.-{2}A[\w\W\n\s]*?)SCENE\s[I]{3}\.", r'<div2 type="scene" n="2">\1</div2> SCENE III.', data)
#add act 3,4 scene 3
data = re.sub(r"(SCENE\s[I]{3}[\w\W\n\s]*?)SCENE\sIV\.", r'<div2 type="scene" n="3">\1</div2> SCENE IV.', data)
#add act 3, scene 4
data = re.sub(r"(SCENE\sIV[\w\W\n\s]*?\.\))", r'<div2 type="scene" n="4">\1</div2>', data)
#add act 4, scene 4
data = re.sub(r"(SCENE\sIV\.-{2}I{1}[\w\W\n\s]*e.)", r'<div2 type="scene" n="4">\1</div2>', data)
#add cast list
data = re.sub(r"(DR[\w\s\n\W]*\setc\.)", r'<castList>\1</castList>', data)

with open('manfred.txt', 'w', encoding="utf-8") as file:
    file.write(data)
