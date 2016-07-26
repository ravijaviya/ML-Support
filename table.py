import urllib.request as req

from bs4 import BeautifulSoup as bs

soup = bs(req.urlopen("https://en.wikipedia.org/wiki/2015_in_film").read(), "html.parser")
table = soup.find_all("table", {"class": "wikitable"})
title = []

for tr in table[4].find_all("tr"):
    for i, td in enumerate(tr):
        a = td.string
        if a is None:
            a = ""
            for name in td.find_all("a"):
                a += name.string + ','
        print(i, a)
        if i == 3:
            title.append(a)

print(len(title))
