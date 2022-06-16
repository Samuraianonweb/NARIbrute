import urllib

id = input('ID')
urllib.urlretrieve('https://raw.githubusercontent.com/Samuraianonweb/password/main/'+str(id)+'_500.txt', 'baza'+str(id)+'.txt')
