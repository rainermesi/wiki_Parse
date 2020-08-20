import xml.etree.ElementTree as ET

tree = ET.parse(r'C:\Users\raine\Downloads\etwiki-20200801-pages-meta-current.xml\etwiki-20200801-pages-meta-current.xml')

text_01 = ET.tostring(tree.getroot(),encoding='utf-8',method='text')

text_01.write(open('output.txt', 'wb'))