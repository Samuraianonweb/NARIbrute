import urllib.request
from urllib.request import urlopen
url = "https://raw.githubusercontent.com/Samuraianonweb/password/main/1_500.txt"
    page = urllib.urlopen(url)
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")
with open(html) as f:
    mas = f.read().splitlines()
for x in mas:
    print(x)
