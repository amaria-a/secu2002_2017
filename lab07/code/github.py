
import requests

url = 'https://api.github.com/repos/smeiklej/secu2002_2017/commits'

# get data from url and parse it as json
r = requests.get(url)
text = r.json()

# commit message is stored at x['commit']['message']
messages = map(lambda x : x['commit']['message'], text)

# print out all messages
for m in messages:
    print m
