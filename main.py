from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
import config
from instituties import *



def get_name_link_of_institutes(url):
    site = urlopen(url)
    soup = bs(site, 'html.parser')

    ul = soup.find_all('ul', class_='menu_list')[:2]
    lis = ul[0].find_all('li', class_='li_spec')
    lis += ul[1].find_all('li', class_='li_spec')

    institutes = [(li.find('a').text, li.find('a').get('href')) for li in lis]

    return institutes

#
# def main():
#     parsing_dictionary = {
#         'Институт экологии и природопользования': parse_ecology,
#         'Институт геологии и нефтегазовых технологий': None,
#         'Институт математики и механики им. Н.И. Лобачевского': parse_mehmat,
#         'Институт физики': parse_physics,
#         'Химический институт им. А.М. Бутлерова': parse_chemistry,
#         'Юридический факультет': parse_law,
#         'Институт вычислительной математики и информационных технологий': parse_ivmiit,
#         'Институт филологии и межкультурной коммуникации': None,
#         'Институт психологии и образования': parse_psychology,
#         'Общеуниверситетская кафедра физического воспитания и спорта': None,
#         'Институт информационных технологий и интеллектуальных систем': None,
#         'Институт фундаментальной медицины и биологии': None,
#         'Инженерный институт': parse_engineer,
#         'Институт международных отношений': parse_imo,
#         'Высшая школа бизнеса': parse_higher_school_buisness,
#         'Институт социально-философских наук и массовых коммуникаций': None,
#         'Институт управления, экономики и финансов': None,
#         'Высшая школа государственного и муниципального управления': None,
#         'Центр корпоративного обучения': None,
#         'IT-лицей-интернат КФУ': parse_IT_licey,
#         'Лицей имени Н.И.Лобачевского': parse_lobach_licey,
#         'Подготовительный факультет для иностранных учащихся': None,
#         'Приволжский центр повышения квалификации и профессиональной переподготовки работников образования': None,
#         'Центр непрерывного повышения профессионального мастерства педагогических работников': None,
#         'Медико-санитарная часть ФГАОУ ВО КФУ': None,
#         'Центр цифровых трансформаций': None,
#         'Институт передовых образовательных технологий': parse_ipot,
#         'Набережночелнинский институт КФУ': parse_chill,
#         'Елабужский институт КФУ': None}
#

if __name__ == '__main__':
    print('hi')
