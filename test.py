from urllib.request import urlopen
passid = urlopen("https://raw.githubusercontent.com/Samuraianonweb/password/main/all.txt").read()
print(passid)
