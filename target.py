import urllib.request

print('Beginning file download with urllib2...')

url = 'https://raw.githubusercontent.com/Samuraianonweb/password/main/1_200.txt'
urllib.request.urlretrieve(url)
