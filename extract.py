import xml.etree.ElementTree as ET
import re
import urllib.request

# This initial block downloads the text, writes an initial file with the whole text and a second one containing only Manfred
# Download and write the full file 
response = urllib.request.urlopen('https://www.gutenberg.org/files/20158/20158-0.txt')
data = response.readlines()

with open('./files/manfred_full.txt', 'w', encoding = 'utf-8-sig') as file:
    for line in data:
        lines = line.decode('utf-8-sig')
        #print(lines)
        file.write(lines)

# Initial clean to only extract Manfred
with open('./files/manfred_full.txt', 'r', encoding = 'utf-8') as extract:
    text = extract.read()

manfred_start = re.findall('Manfred:\n', text, re.IGNORECASE)
#print('This is the start of Manfred:', manfred_start)
manfred_end = re.findall(r'.*poem."\]', text)
#print('This is the end of Manfred:', manfred_end)

in_text_3 = text.index(manfred_start[0])
#print(in_text_3)
in_text_4 = text.index(manfred_end[0])
#print(in_text_4)

with open('./files/manfred_extracted.txt', 'w', encoding = 'utf-8') as manfred_extract:
        manfred_final = manfred_extract.write(text[in_text_3 : in_text_4 + len(manfred_end[0])])
        #print(manfred_final)


#---------------------------------------------------------#
#This block takes the Manfred text and prepares it for further processing

with open('./files/manfred_extracted.txt', 'r', encoding="utf-8") as file:
    data = file.read()

#removes underscores
data = data.replace('_', '')

#splits the text at the initial castlist and removes footnotes
new = re.split(' *ACT 1.\s', data)
# for i in new:
#     print(i)

data = "ACT 1." + new[1]

new2 = re.split('FOOTNOTES', data)
# for i in new2:
#     print(i)

data = new2[0]


# removes footnotes in text
data = re.sub("\[[a-z]{2}\]",'', data)
data = re.sub("\[\d{3}\]", '', data)
# converts ACT 1 to roman numerals (inconsistent Gutenberg number schemes)
data = re.sub("ACT\s\d", 'ACT I', data)
# converts SCENE 1 to roman numerals
data = re.sub("SCENE\s\d", 'SCENE I', data)
# Normalize character indications. Adds invisible unicode character U+200A at the beginning to make regex capturing easier at a later stage
data = re.sub("Abbot\.", ' ABBOT.\n', data)
data = re.sub("Manuel\. ", ' MANUEL.\n', data)
data = re.sub("Man\.", ' MANFRED.\n', data)
data = re.sub("Nem\.", ' NEMESIS.\n', data)
data = re.sub("First Spirit\.", ' FIRST SPIRIT.\n', data)
data = re.sub("Voice of the Third Spirit\.", ' THIRD SPIRIT.\n', data)
data = re.sub("Voice of the Second Spirit\.", ' SECOND SPIRIT.\n', data)
data = re.sub("Second Spirit\.", ' SECOND SPIRIT.\n', data)
data = re.sub("Third Spirit\.", ' THIRD SPIRIT.\n', data)
data = re.sub("Fourth Spirit\.", ' FOURTH SPIRIT.\n', data)
data = re.sub("FOURTH SPIRIT\.", ' FOURTH SPIRIT.\n', data)
data = re.sub("Fifth Spirit\.", ' FIFTH SPIRIT.\n', data)
data = re.sub("FIFTH SPIRIT\.", ' FOURTH SPIRIT.\n', data)
data = re.sub("SIXTH SPIRIT\.", ' FOURTH SPIRIT.\n', data)
data = re.sub("SEVENTH SPIRIT\.", ' FOURTH SPIRIT.\n', data)
data = re.sub("The SEVEN SPIRITS\.", ' FOURTH SPIRIT.\n', data)
data = re.sub("Spirit\.", ' SPIRIT.\n', data)
data = re.sub("C\. Hun\.", ' CHAMOIS HUNTER.\n', data)
data = re.sub("Chamois Hunter\. ", ' CHAMOIS HUNTER.\n', data)
data = re.sub("Her\.", ' HERMAN.\n', data)
data = re.sub("Witch\.", ' WITCH.\n', data)
data = re.sub("Ari\.", ' ARIMANES.\n', data)
data = re.sub("First Des\.", ' FIRST DESTINY.\n', data)
data = re.sub("Second Des\.", ' SECOND DESTINY.\n', data)
data = re.sub("Third Des\.", ' THIRD DESTINY.\n', data)
data = re.sub("Phantom of Astarte\.", ' PHANTOM OF ASTARTE.\n', data)
data = re.sub("Phan\.", ' PHANTOM OF ASTARTE.\n', data)
#normalize stage directions
data = re.sub("(\[[a-zA-Z '\s,]*\.)", '\\1]', data)
data = re.sub("\s*(The[A-Za-z\s,-]*ins\.)\s", '[\\1]', data)
data = re.sub("(Enter[a-zA-Z '.]*\.)", '[\\1]', data)
data = re.sub("(Re-[a-zA-Z '.]*\.)", '[\\1]', data)
data = re.sub("(After[a-zA-Z\s,.]*torrent\.)", '[\\1]', data)
data = re.sub("(--Manfred[A-Za-z,\-\s.]*Midnight.)", '', data)



with open('./files/manfred_extracted.txt', 'w', encoding="utf-8") as file:
    file.write(data)