from requests import get
ip = get('https://api.ipify.org').content.decode('utf8')
print(ip)


import urllib.request
external_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')
print(external_ip)


import os
externalIP  = os.popen('curl -s ifconfig.me').readline()
print(externalIP)