import requests
import urllib.request

from bs4 import BeautifulSoup

url = "https://minecraft.net/en/"
qDeVizitat = [url]
qVizitate = [url]


while len(qDeVizitat) > 0:


    htmltext = requests.get(qDeVizitat[0]).text
    #html=urllib.request.urlopen(qDeVizitat[0]).read()



    ciorba = BeautifulSoup(htmltext, "html.parser")

    qDeVizitat.pop(0)

    print(len(qDeVizitat))

    for tag in ciorba.findAll('a', href=True):
        tag['href'] = urllib.request.urljoin(url, tag['href'])

        if url in tag['href'] and tag['href'] not in qVizitate:
            qDeVizitat.append(tag['href'])
            qVizitate.append(tag['href'])

with open("a.txt", 'w') as f:
    for s in qVizitate:
        f.write(s + '\n')
