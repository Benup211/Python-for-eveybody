import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')
mysock.close()

import urllib.request,urllib.parse,urllib.error
fhand=urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    print(line.decode().strip())

from bs4 import BeautifulSoup
url=input('enter url:')
html_value=urllib.request.urlopen(url).read()
soup_value=BeautifulSoup(html_value,'html.parser')
tags=soup_value('a')
for tag in tags:
    print(tag.get('href',None))