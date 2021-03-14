from instituties.ivmiit import get_link_from_button, get_stuff

url_buisness = 'https://kpfu.ru/mba'

def parse_buisness(url):
    stuff_url = get_link_from_button(url, 'Список сотрудников')
    return {'Высшая школа бизнеса':len(get_stuff(stuff_url))}

# print(parse_buisness(url_buisness))