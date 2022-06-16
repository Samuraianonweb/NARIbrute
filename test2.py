import requests
import urllib

link = "https://raw.githubusercontent.com/Samuraianonweb/password/main/1_500.txt"

page = urllib.request.urlopen(link)
html = page.read()
mystr = html.decode("utf8")
page.close()
print(mystr)

