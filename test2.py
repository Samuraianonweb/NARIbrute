import requests
import urllib

link = "https://raw.githubusercontent.com/Samuraianonweb/password/main/1_500.txt"

page = urllib.request.urlopen(link)
html = page.read()

with open(html) as f:
    mas = f.read().splitlines()
for x in mas:
    print(x)
