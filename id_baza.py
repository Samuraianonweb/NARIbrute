import urllib

id = input('ID бази: ')
urllib.urlretrieve('https://raw.githubusercontent.com/Samuraianonweb/password/main/'+str(id)+'_500.txt', 'pass.txt')
