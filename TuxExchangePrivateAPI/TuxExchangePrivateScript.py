import json
import requests
import hmac
import hashlib
import urllib


#Tuxexchange opening Public Key file and Private Key file, then converting to string

with open('PublKey.txt', 'r') as file:
   data=file.read().replace('\n','')

with open('PrivKey.txt', 'r') as privfile:
   privdata=privfile.read().replace('\n','')

tuxURL = "https://tuxexchange.com/api"

query = {"method":"getmybalances"}

newquery = {"method":"getmytradehistory"}

encoded = urllib.urlencode(query)

signature = hmac.new(privdata,encoded,hashlib.sha512).hexdigest()

TuxexchangeHeader = {'Sign':signature, 'Key': data}

tuxgetbalance = requests.post(tuxURL, data=query, headers=TuxexchangeHeader,timeout=15).json()

encodeurl = urllib.urlencode(newquery)

signature1 = hmac.new(privdata,encodeurl,hashlib.sha512).hexdigest()

TuxexchangeHeader1 = {'Sign':signature1, 'Key': data}

tuxgetaddresses = requests.post(tuxURL, data=newquery, headers=TuxexchangeHeader1, timeout=15).json()


