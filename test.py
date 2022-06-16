import urllib.request

html = urllib.request.urlopen('test')

with open(html) as f:
    mas = f.read().splitlines()
for x in mas:
    print(x)
