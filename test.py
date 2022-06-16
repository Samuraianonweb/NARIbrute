import urllib.request

html = urllib.request.urlopen('https://raw.githubusercontent.com/Samuraianonweb/password/main/1_500.txt')

with open(html) as f:
    mas = f.read().splitlines()
for x in mas:
    print(x)
