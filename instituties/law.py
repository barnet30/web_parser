from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
from instituties.ivmiit import get_link_from_button

url_law = 'https://kpfu.ru/law'

def get_cathedras(url):
    site = urlopen(url)
    soup = bs(site, 'html.parser')

    cathedras = list()
    uls = soup.find_all('ul',class_='menu_list')[:2]
    for ul in uls:
        list_items = ul.find_all('li',class_='li_spec')
        for item in list_items:
            tag_a = item.find('a')
            if tag_a:
                if tag_a.text.startswith('Кафедра'):
                    cathedras.append((tag_a.text, tag_a.get('href')))
    return cathedras

def get_stuff(url):
    site = urlopen(url)
    soup = bs(site,'html.parser')

    stuff = list()
    div = soup.find('div',class_='visit_link')
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

def parse_law(url):
    cathedras = get_cathedras(url)

    res = {}
    for name, url_cath in cathedras:
        url1 = get_link_from_button(url_cath,'Сотрудники')
        url2 = get_link_from_button(url_cath,'Сотрудники кафедры')
        if url1:
            stuff_url = url1
        elif url2:
            stuff_url = url2
        stuff = get_stuff(stuff_url)
        res[name] = len(stuff)
    return res

# print(parse_law(url_law))
