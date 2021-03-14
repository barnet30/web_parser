from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
from instituties.ivmiit import get_link_from_button

url_imo = 'https://kpfu.ru/imoiv'

def get_cathedras(url):
    site = urlopen(url)
    soup = bs(site, 'html.parser')

    div = soup.find('div', class_='visit_link')
    tags_a = div.find_all('a')

    cathedras = list()
    for item in tags_a:
        if 'Кафедра' in item.text:
            cathedras.append((item.text, item.get('href')))
    return cathedras

def get_stuff(url):
    site = urlopen(url)
    soup = bs(site, 'html.parser')

    stuff = list()

    iframe = soup.find('iframe')
    if iframe:
        source = iframe.get('src')

        site = urlopen(source)
        soup = bs(site, 'html.parser')

        spans = soup.find_all('span', class_='fio')

        for span in spans:
            tag_a = span.find('a')
            if tag_a:
                stuff.append((tag_a.text, tag_a.get('href')))
    else:
        div = soup.find('div', class_='visit_link')
        p = div.find('p')
        for row in p.text.split('\r\n'):
            stuff.append((row, None))
    return stuff

def parse_imo(url):
    struct_button_url = get_link_from_button(url, 'Структура')
    cathedras = get_cathedras(struct_button_url)

    res = {}

    for name, url in cathedras:
        url1 = get_link_from_button(url, 'Сотрудники')
        url2 = get_link_from_button(url, 'Состав кафедры')
        if url1:
            stuff_url = url1
        if url2:
            stuff_url = url2
        res[name] = len(get_stuff(stuff_url))

    return res
# print(parse_imo(url_imo))