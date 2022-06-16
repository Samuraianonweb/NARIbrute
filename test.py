import urllib, urllib2
import​ ​urlopen
id = "https://raw.githubusercontent.com/Samuraianonweb/password/main/all.txt"

idpash = urlopen(id)
passbit = idpash.read()
passid = pashbit.decode("utf-8")
print (passid)
