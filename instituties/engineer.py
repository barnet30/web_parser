from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
from instituties.ivmiit import get_link_from_button

url_engineer = 'https://kpfu.ru/engineer'

def get_cathedras(url):
    site = urlopen(url)
    soup = bs(site, 'html.parser')

    div = soup.find('div', class_='area_width')
    tags_a = div.find_all('a')

    cathedras = list()
    for item in tags_a:
        if item.text.startswith('Кафедра'):
            cathedras.append((item.text, item.get('href')))
    return cathedras

def get_stuff(url):
    site = urlopen(url)
    if site is None:
        return
    soup = bs(site, 'html.parser')
    stuff = list()

    div = soup.find('table', class_='cke_show_border')
    if div:
        tags_a = div.find_all('a')
        for item in tags_a:
            if item:
                stuff.append((item.text, item.get('href')))
    else:
        iframe = soup.find('iframe')
        if iframe:
            source = iframe.get('src')

            site = urlopen(source)
            soup = bs(site, 'html.parser')

            spans = soup.find_all('span', class_='fio')
            for item in spans:
                tag_a = item.find('a')
                if tag_a:
                    stuff.append((tag_a.text, tag_a.get('href')))

    return stuff

def parse_engineer(url):
    struct_button_url = get_link_from_button(url, 'Структура')
    cathedras = get_cathedras(struct_button_url)

    res = {}

    for name, url in cathedras:
        url1 = get_link_from_button(url, 'Состав кафедры')
        url2 = get_link_from_button(url, 'Сотрудники кафедры')
        if url1:
            stuff_url = url1
        elif url2:
            stuff_url = url2
        res[name] = len(get_stuff(stuff_url))

    return res

# print(parse_engineer(url_engineer))
