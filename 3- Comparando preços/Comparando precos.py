import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import math

url = 'https://www.kabum.com.br/hardware/placa-de-video-vga'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'}
site = requests.get(url, headers=headers)
soup = BeautifulSoup(site.content, 'html.parser')

qtd_itens = soup.find('div', id='listingCount').get_text().strip()

index = qtd_itens.find(' ')
qtd = qtd_itens[:index]

ultima_pagina = math.ceil(int(qtd) / 36)

dic_produtos = {'site':[], 'marca':[], 'preco':[], 'link':[]}

for i in range(1, ultima_pagina+1):
    url_pag = f'https://www.kabum.com.br/hardware/placa-de-video-vga?page_number={i}&page_size=20&facet_filters=&sort=most_searched'
    site = requests.get(url_pag, headers=headers)
    soup = BeautifulSoup(site.content, 'html.parser')
    produtos = soup.find_all('div', class_=re.compile('productCard'))
    
    for produto in produtos:
        site = 'Kabum'
        marca = produto.find('span', class_=re.compile('nameCard')).get_text().strip()    
        preco = produto.find('span', class_=re.compile('priceCard')).get_text().strip()
        link = url_pag        
        print(i, site, marca, preco, link)
        
        dic_produtos['site'].append(site)
        dic_produtos['marca'].append(marca)
        dic_produtos['preco'].append(preco)
        dic_produtos['link'].append(link)     
               
        
        
url = 'https://www.pichau.com.br/hardware/placa-de-video'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'}
site = requests.get(url, headers=headers)
soup = BeautifulSoup(site.content, 'html.parser')

qtd_itens = soup.find('div', id='jss406').get_text().strip()


index = qtd_itens.find(' ')
qtd = qtd_itens[:index]

ultima_pagina = math.ceil(int(qtd) / 36)


for i in range(1, ultima_pagina+1):
    url_pag = f'https://www.pichau.com.br/hardware/placa-de-video?page={i}'
    site = requests.get(url_pag, headers=headers)
    soup = BeautifulSoup(site.content, 'html.parser')
    produtos = soup.find_all('div', class_=re.compile('productCard'))







df = pd.DataFrame(dic_produtos)
df.to_csv('C:\\Users\\Luis Felipe\\Documents\\CSV Placa de Vídeos\\preco_cadeira.csv', encoding='utf-8', sep=';')

read_file = pd.read_csv (r'C:\\Users\\Luis Felipe\\Documents\\CSV Placa de Vídeos\\preco_cadeira.csv', encoding='utf-8', sep=';')
read_file.to_excel (r'C:\\Users\\Luis Felipe\\Documents\\CSV Placa de Vídeos\\preco_cadeira.xls', index = None, header=True)