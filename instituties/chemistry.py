from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
from instituties.ivmiit import get_link_from_button

url_chem = 'https://kpfu.ru/chemistry'

def get_cathedras(url):
    site = urlopen(url)
    soup = bs(site, 'html.parser')

    cathedras = list()
    ul = soup.find('ul',class_='menu_list')
    list_items = ul.find_all('li',class_='li_spec')
    for item in list_items:
        tag_a = item.find('a')
        if tag_a:
            if tag_a.text.startswith('Кафедра'):
                cathedras.append((tag_a.text,tag_a.get('href')))
    return cathedras

def get_stuff(url):
    site = urlopen(url)
    soup = bs(site, 'html.parser')

    iframe = soup.find('iframe')
    source = iframe.get('src')

    site = urlopen(source)
    soup = bs(site,'html.parser')

    stuff = list()
    spans = soup.find_all('span', class_='fio')
    for item in spans:
        tag_a = item.find('a')
        if tag_a:
            stuff.append((tag_a.text, tag_a.get('href')))

    return stuff

def parse_chemistry(url):
    info_button_url = get_link_from_button(url,'Структура')
    cathedras = get_cathedras(info_button_url)

    res = {}
    for name,url in cathedras:
        stuff_url = get_link_from_button(url,'Список сотрудников')
        stuff = get_stuff(stuff_url)
        res[name] = len(stuff)

    return res

# print(parse_chemistry(url_chem))

