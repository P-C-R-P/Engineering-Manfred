import xml.etree.ElementTree as ET
import lxml.etree as ET
import re


inputFile = 'files/manfred_extracted.txt'
xmlFile = 'files/output.xml'

tree = ET.ElementTree(element= ET.Element('document'))
root=tree.getroot()

# Add header
header = ET.Element('header')
root.append(header)

authors = ET.Element('authors')
authors.text = "compiled by Philipa Payne et Fábio Cabral"
header.append(authors)

drama = ET.Element('drama')
root.append(drama)

countActs = 0
countScenes = 0

with open (inputFile, 'r', encoding="utf-8") as txt_file:
    for line in txt_file:
        #act match
        a = re.match(r'\s*(ACT\s([I]{1,3})\.)', line)
        if a:
            countScenes = 0
            countActs += 1
            #print("Act caught")
            act = ET.SubElement(drama, 'act', attrib = {'n': str(countActs)})
            act.text = a.group()

        b = re.match(r'\s*(SCENE\s([I]{1,3}V?)\.)', line)
        if b:
            countScenes += 1
            #print("Scene caught")
            scene = ET.SubElement(act, 'scene', attrib = {'n': str(countScenes)})
            scene.text = b.group()

        c = re.match(r'\s* ([A-Z]*)\.', line)
        if c:
            #print("Character caught")
            speaker = ET.SubElement(scene, 'speaker', attrib = {'name': c.group(1)})
            speaker.text = c.group()

        d = re.match(r'\s* ([A-Z]* [A-Z]*)\.', line)
        if d:
            #print("Two-part character caught")
            speaker = ET.SubElement(scene, 'speaker', attrib = {'name': d.group(1)})
            speaker.text = d.group()
        e = re.match(r'\s*(\[[A-za-z_\s:;.,-]*\])', line)
        if e:
            #print("Stage direction caught")
            stage = ET.SubElement(scene, 'stage')
            stage.text = e.group()
            
        f = re.match(r'(.+)', line)
        if f and not a and not b and not c and not d and not e:
            print("Speech" + f.group())
            speech = ET.SubElement(scene, 'speech')
            speech.text = line
        else:
            pass

# regex for one part characters:" [A-Z]*\." 
# regex for two part characters:" [A-Z]* [A-Z]*\."

ET.indent(tree)
tree.write(xmlFile, encoding="utf-8", xml_declaration=True)

#HTML rendering

xmlFile = 'files/output.xml'
xsltFile = 'files/stylesheet.xslt'
htmlFile = 'files/manfred.html'

xml = ET.parse(xmlFile)
xslt = ET.parse(xsltFile)

transform = ET.XSLT(xslt)
newdom = transform(xml)

newdom.write(htmlFile, encoding="utf-8")