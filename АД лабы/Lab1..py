import requests
url = "https://www.dropbox.com/s/lot1946ol8q8u85/test.zip?dl=1"
r = requests.get(url, allow_redirects=True)
open('test.zip', 'wb').write(r.content)

url = "https://www.dropbox.com/s/ivy51wqobna8wbt/train_fix.zip?dl=1"
r = requests.get(url, allow_redirects=True)
open('train_fix.zip', 'wb').write(r.content)