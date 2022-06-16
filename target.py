import urllib
import random

url = "https://raw.githubusercontent.com/Samuraianonweb/password/main/'+id+'200'"
id = random.randint(1,2)
file_name = 'targets'
urllib.urlretrieve(url, filename)
