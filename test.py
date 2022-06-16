from urllib.request import urlopen
passid = urlopen("https://raw.githubusercontent.com/Samuraianonweb/password/main/1_500.txt").read()
parsid = passid.decode("utf-8")
print(parsid)
