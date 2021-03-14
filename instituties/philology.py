from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
from instituties.ivmiit import get_link_from_button

url_phyl = 'https://kpfu.ru/philology-culture'

def get_schools(url):
    site = urlopen(url)
    soup = bs(site, 'html.parser')

    ul = soup.find('ul',class_='menu_list_left')
    list_items = ul.find_all('li')

    schools = list()
    for item in list_items:
        tag_a = item.find('a')
        if tag_a:
            if tag_a.text.startswith('Высшая школа'):
                schools.append((tag_a.text,tag_a.get('href')))
    return schools

def get_cathedras(url):
    site = urlopen(url)
    soup = bs(site,'html.parser')

    ul = soup.find('ul',class_='menu_list_left')
    list_items = ul.find_all('li')
    cathedras = list()
    for item in list_items:
        tag_a = item.find('a')
        if tag_a:
            if tag_a.text.startswith('Кафедра'):
                cathedras.append((tag_a.text, tag_a.get('href')))
    return cathedras

def get_stuff(url):
    stuff = list()
    site = urlopen(url)
    soup = bs(site, 'html.parser')

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
    else:
        select_list = soup.select('p a[href]')
        for i in select_list:
            if i.text != 'КФУ' and not i.text.startswith('Институт'):
                stuff.append((i.text, i.get('href')))

    return stuff

def parse_philology(url):
    struct_button_url = get_link_from_button(url,'Структура')
    cathedras = list()
    schools = get_schools(struct_button_url)
    res = {}
    for name,url in schools:
        tmp = get_cathedras(url)
        cathedras+=tmp

    for name, url in cathedras:
        stuff_button_url = get_link_from_button(url,'Сотрудники')
        res[name] = len(get_stuff(stuff_button_url))
    return res


# print(parse_philology(url_phyl))

