import requests
import urllib

link = "https://raw.githubusercontent.com/Samuraianonweb/password/main/1_500.txt"

page = urllib.request.urlopen(link)
html = page.read()
   for line in html:
        print(line.strip())
