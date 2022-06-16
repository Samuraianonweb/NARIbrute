import urllib.request

url = "http://olympus.realpython.org/profiles/aphrodite"
    page = urlopen(url)
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")
with open(html) as f:
    mas = f.read().splitlines()
for x in mas:
    print(x)
