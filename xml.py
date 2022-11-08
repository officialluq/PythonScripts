import xml.dom.minidom
file = xml.dom.minidom.parse("plik.xml")
sheet = file.documentElement
names = sheet.getElementsByTagName("name")
for i in names:
    names = sheet.getElementsByTagName("year")[0]
    i.tagName="newtag"

f = open("plik2.xml", "wb")
f.write(sheet.toxml("utf-8"))
