import urllib
import random

url = "https://raw.githubusercontent.com/Samuraianonweb/password/main/1_200.txt"
id = random.randint(1,2)
file_name = 'targets.txt'
urllib.urlretrieve(url, filename)
