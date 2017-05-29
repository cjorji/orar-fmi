from bs4 import BeautifulSoup

with open("343.html") as fp:
    soup = BeautifulSoup(fp,"html.parser")

[s.extract() for s in soup('img')]

table = soup.find_all('table')[0]  # Grab the first table
rows = table.findAll('tr')

i = 0
for tr in rows:
    cols = tr.findAll('td')

    #print(cols)
    for col in cols:
        if col:
            print(col.string)


#print(table)