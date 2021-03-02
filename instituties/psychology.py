from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
from instituties.ivmiit import get_link_from_button

url_psy = 'https://kpfu.ru/psychology'

def get_cathedras(url):
    site = urlopen(url)
    soup = bs(site, 'html.parser')
    ul = soup.find('ul',class_='menu_list_left')
    cathedras = list()

    list_items = ul.find_all('li')
    for item in list_items:
        tag_a = item.find('a')
        if tag_a:
            if tag_a.text.startswith('Кафедра'):
                cathedras.append((tag_a.text, tag_a.get('href')))
    return cathedras

def get_stuff(url):
    site = urlopen(url)
    soup = bs(site, 'html.parser')

    stuff = list()
    div = soup.find('div', class_='visit_link')
    if div:
        pars = div.find_all('p')
        for p in pars:
            tag_a = p.find('a')
            if tag_a:
                stuff.append((tag_a.text, tag_a.get('href')))
            elif p:
                stuff.append((p.text, None))
    else:
        select_list = soup.select('p a[href]')
        for i in select_list:
            stuff.append((i.text, i.get('href')))
    return stuff

def parse_psychology(url):
    struct_btn_link = get_link_from_button(url, 'Структура')
    cathedras_link = get_link_from_button(struct_btn_link,'Кафедры')

    cathedras = get_cathedras(cathedras_link)
    res = {}
    for name, url_cath in cathedras:
        url1 = get_link_from_button(url_cath, 'Сотрудники')
        url2 = get_link_from_button(url_cath, 'Сотрудники кафедры')
        if url1:
            stuff_url = url1
        elif url2:
            stuff_url = url2
        stuff = get_stuff(stuff_url)
        res[name] = len(stuff)
    return res

print(parse_psychology(url_psy))
