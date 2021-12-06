import requests
from bs4 import BeautifulSoup

url= 'https://www.meteoromania.ro/radarm/radar.index.php'

g = requests.get(url)

sup = BeautifulSoup(g.content, 'lxml')
# print(sup)
div = sup.find_all('img')


print(div)