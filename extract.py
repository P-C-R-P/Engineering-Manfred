import xml.etree.ElementTree as ET
import os
import re
import urllib.request

# Download and write the full file 
response = urllib.request.urlopen('https://www.gutenberg.org/files/20158/20158-0.txt')
data = response.readlines()

with open('./files/manfred_full.txt', 'w', encoding = 'utf-8-sig') as file:
    for line in data:
        lines = line.decode('utf-8-sig')
        print(lines)
        file.write(lines)

# Initial clean to only extract Manfred
with open('./files/manfred_full.txt', 'r', encoding = 'utf-8') as extract:
    text = extract.read()

manfred_start = re.findall('Manfred:\n', text, re.IGNORECASE)
print('This is the start of Manfred:', manfred_start)
manfred_end = re.findall(r'.*poem."\]', text)
print('This is the end of Manfred:', manfred_end)

in_text_3 = text.index(manfred_start[0])
print(in_text_3)
in_text_4 = text.index(manfred_end[0])
print(in_text_4)

with open('./files/manfred_extracted.txt', 'w', encoding = 'utf-8') as manfred_extract:
        manfred_final = manfred_extract.write(text[in_text_3 : in_text_4 + len(manfred_end[0])])
        print(manfred_final)


# ------------------- #
with open('./files/manfred_extracted.txt', 'r', encoding="utf-8") as file:
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

with open('./files/manfred_extracted.txt', 'w', encoding="utf-8") as file:
    file.write(data)