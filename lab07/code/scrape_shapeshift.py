
import requests
import pickle

# get data from remote source
url = 'https://shapeshift.io/recenttx/50'
r = requests.get(url)

# parse it as json
entries = r.json()

# save it intact to a file 
pickle.dump(entries,open('shapeshift.p','wb'))
