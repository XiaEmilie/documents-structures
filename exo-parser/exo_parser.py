# -*- coding: utf-8 -*-

from lxml import etree
xmlfile = "valery_ame-et-danse_1921.xml"

# Initialiser la lecture du fichier
tree = etree.parse(xmlfile)

# Le contenu en tant que string
#print(etree.tostring(tree))

# La racine
root = tree.getroot()
#print(root.tag)

# Utiliser un espace de nom
TEI_NAMESPACE = "http://www.tei-c.org/ns/1.0"
TEI = "{%s}" % TEI_NAMESPACE
# Obtenir le tag et valeur des enfants de <titleStmt>
#for element in root.iter(TEI + 'titleStmt'):
 #   for child in element:
        #print(child.tag, child.text, child.attrib)

# Afficher le nom de l'éditeur <edition>
for element in root.iter(TEI + 'edition'):
    print(element.text)

# Afficher l'url de la licence <licence>
for element in root.iter(TEI + 'licence'):
    print(element.attrib)

# Afficher le personnage avec le plus de réplique (@speaker) et le nombre de répliques
d = dict()
for element in root.iter(TEI + 'label'):
    d[element.text] = d.get(element.text, 0) +1
    #print (element.text)

max_speaker = max(d, key = d.get)
print (max_speaker)

for element in root.iter(TEI + 'editionStmt'):
    child = etree.SubElement(element,"respStmt")
    sub_child1 = etree.SubElement(child,"name")
    sub_child1.text = "blabla"
    sub_child2 = etree.SubElement(child,"resp")
    sub_child2.text = "blabla"

for element in root.iter(TEI + 'signed'):
    for child in element:
        print (child.text.upper())

# Afficher les attributs (dictionnaire)
#print(root.attrib)
# Afficher un attribut particulier
#print(root.get('{http://www.w3.org/XML/1998/namespace}' + 'lang'))
# Ajouter un attribut
#root.set('nouvel-attribut', 'documentsStructures')
#print(root.attrib)