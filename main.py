# -*- coding: utf-8 -*-
# !/usr/bin/env python
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
import config
from instituties import ivmiit, buisness, chemistry, ecology, engineer, imo, law, mehmat, philology, physics, psychology


def get_instituties(url):
    site = urlopen(url)
    soup = bs(site, 'html.parser')

    ul = soup.find_all('ul', class_='menu_list')[:1]
    lis = ul[0].find_all('li', class_='li_spec')

    institutes = [(li.find('a').text, li.find('a').get('href')) for li in lis[:-10]]

    return institutes


def main():
    instituties = get_instituties(config.basic_url)

    parsing_funcs = {
        'Институт экологии и природопользования': ecology.parse_ecology,
        'Институт геологии и нефтегазовых технологий': None,
        'Институт математики и механики им. Н.И. Лобачевского': mehmat.parse_mehmat,
        'Институт физики': physics.parse_physics,
        'Химический институт им. А.М. Бутлерова': chemistry.parse_chemistry,
        'Юридический факультет': law.parse_law,
        'Институт вычислительной математики и информационных технологий': ivmiit.parse_ivmiit,
        'Институт филологии и межкультурной коммуникации': philology.parse_philology,
        'Институт психологии и образования': psychology.parse_psychology,
        'Общеуниверситетская кафедра физического воспитания и спорта': None,
        'Институт информационных технологий и интеллектуальных систем': None,
        'Институт фундаментальной медицины и биологии': None,
        'Инженерный институт': engineer.parse_engineer,
        'Институт международных отношений': imo.parse_imo,
        'Высшая школа бизнеса': buisness.parse_buisness,
        'Институт социально-философских наук и массовых коммуникаций': None,
        'Институт управления, экономики и финансов': None,
    }

    data = {}
    for name, url in instituties:
        parse = parsing_funcs.get(name)
        if parse:
            data[name] = parse(url)

    f = open('data.txt', 'w')
    f.write(str(data))
    f.close()
    print(data)

if __name__ == '__main__':
    main()