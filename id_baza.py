import urllib

id = input('Number Id')
urllib.urlretrieve('https://raw.githubusercontent.com/Samuraianonweb/password/main/'+str(id)+'_500.txt', 'baza'+str(id)+'.txt')
