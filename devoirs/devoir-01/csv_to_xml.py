#-*-coding:utf-8-*-

xml_data = open('tournages.xml','w')
xml_data.write('<?xml version="1.0" encoding="UTF-8"?>' + '\n' + '<!DOCTYPE cinema SYSTEM "tournages.dtd">' + '\n' + '<cinema>' + '\n')

num = 0
with open("tournagesdefilmsparis2011.csv") as f :
    for line in f:
        line = line.strip()
        data = line.split(";")
        if num == 0:
            info = data
            for i in range(len(info)) :
                info[i] = info[i].replace(' ','_')
        else :
            xml_data.write('\t' + '<tournage num="' + str(num) + '">'+'\n')
            for i in range(len(data)) :
                xml_data.write('\t\t<' + info[i] + '>'+ data[i] + '</' + info[i] + '>' + '\n')
            xml_data.write('\t' + '</tournage>' + '\n')
        num += 1

xml_data.write('</cinema>' + '\n')
xml_data.close()