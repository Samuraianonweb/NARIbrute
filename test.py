import requests
import urllib

link = "http://www.somesite.com/details.pl?urn=2344"

f = urllib.request.urlopen(link)
myfile = f.read()

writeFileObj = open('output.xml', 'wb')
writeFileObj.write(myfile)
writeFileObj.close()
