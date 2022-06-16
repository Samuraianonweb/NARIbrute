import urllib.request
import random

url = ''https://raw.githubusercontent.com/Samuraianonweb/password/main/{{id}}200"
id = random.randint(1,2)
file_name = 'targets.txt'
urllib.request.urlretrieve(url, filename)
