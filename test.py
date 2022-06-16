from urllib.request import urlopen
passid = urlopen("test").read()
print(passid)
