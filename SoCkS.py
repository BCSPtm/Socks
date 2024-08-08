""" 
@BCSP
"""
import random,requests
import re,time,json,os
item = []

def __BCSP__():
        if os.path.isfile('.proxi.txt') is True:
           return(open('.proxi.txt','r').read().splitlines())
        else:
           try:
               link = 'https://api.proxyscrape.com/v2/?request=displayproxies&protocol={}&timeout=100000&country=all&ssl=all&anonymity=all'
               resp = requests.get(link.format('socks5'))
               for i in resp.text.splitlines():
                   if i.isdigit:
                      if i not in item:
                         item.append(i)
                         open('.proxi.txt','a').write(f'{i}\n')
               return item
           except requests.exceptions.ConnectionError: time.sleep(5); self.socks()


prox = __BCSP__()
prok = {'http': 'socks5://' + random.choice(prox)}
print(prok)
