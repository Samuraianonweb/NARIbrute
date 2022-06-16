import urllib
import random

id = random.randint(1,2)
urllib.urlretrieve('https://raw.githubusercontent.com/Samuraianonweb/password/main/'str(id)'_200.txt', 'test.txt')
