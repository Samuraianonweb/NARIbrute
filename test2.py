import requests
import urllib

link = "https://raw.githubusercontent.com/Samuraianonweb/password/main/"

f = urllib.request.urlopen(link)
myfile = f.read()

writeFileObj = open('pass.txt', 'wb')
writeFileObj.write(myfile)
writeFileObj.close()
