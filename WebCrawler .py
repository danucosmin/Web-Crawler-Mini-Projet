import urllib
import urlparse2

from bs4 import BeautifulSoup



url="http://ing.pub.ro/en/"

qDeVizitat=[url]
qVizitate=[url]


while len(qDeVizitat)!=0:

    htmltext=urllib.urlopen(qDeVizitat[0]).read()




    ciorba=BeautifulSoup(htmltext)

    qDeVizitat.pop(0)

    for tag in ciorba.findAll('a'  ,href=True):
        tag['href'] =urlparse2.urljoin(url,tag['href'])
        if url in tag['href'] and tag['href'] not in qVizitate:
            qDeVizitat.append(tag['href'])
            qVizitate.append(tag['href'])

print (qVizitate)