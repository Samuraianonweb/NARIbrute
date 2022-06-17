import urllib

a=1
while a < 3:
    print(a)
    a = a + 1

urllib.urlretrieve('https://raw.githubusercontent.com/Samuraianonweb/password/main/'+str(id)+'_500.txt', 'pass.txt')
