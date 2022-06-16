import requests
import urllib

link = "https://raw.githubusercontent.com/Samuraianonweb/password/main/1_500.txt"

f = urllib.request.urlopen(link)
myfile = f.read()

print(myfile)
