# -*- coding: utf-8 -*-
# XIA Emilie M2 IM

from lxml import etree
xmlfile = "Duchn-etiquetage.txt.xml"

tree = etree.parse(xmlfile)
root = tree.getroot()

# Extraire tous les déterminants
det = []
for element in tree.xpath("//element/data[1][contains(text(),'DET')]") :
    i = element.getnext().getnext().xpath("text()")
    det += i
print (det)

# Afficher les patrons DET-NOM
i = 0
det_nom = []
for element in root.iter("article") :
    for child in element:
        if "DET" in element[i][0].text :
            if "NOM" in element[i+1][0].text:
                p = element[i][2].text, element[i+1][2].text 
                det_nom.append(p)
        i += 1
print (det_nom)

# Reconstruire les phrases
i = 0
sentences = []
for element in root.iter("article") :
    sentence = []
    for child in element:
        sentence.append(element[i][2].text)
        sep = " "
        sent = sep.join(sentence)
        if element[i][2].text == "." :
            sentences.append(sent)
        i += 1
print (sentences)

# Transformer l'affichage en : token/lemme/pos
i = 0
tok_lem_pos = []
for element in root.iter("article") :
    ele = ""
    for child in element:
        ele = element[i][0].text + "/" +element[i][1].text + "/" +element[i][2].text
        tok_lem_pos.append(ele)
        i += 1
print (tok_lem_pos)
