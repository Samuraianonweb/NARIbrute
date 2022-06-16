import urllib
import random

id = random.randint(1,58)
urllib.urlretrieve('https://raw.githubusercontent.com/Samuraianonweb/password/main/'+str(id)+'_500.txt', 'pass.txt')
