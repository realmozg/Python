from bs4 import BeautifulSoup
import os
import html.parser
import sys
import requests
import re

folder = 'C:\\Users\\demom\\Desktop\\Parse_site\\'
source_file = folder+'site.html'
file_log = folder+'log.txt'
site_for_parse = 'https://ca.kontur.ru/about/certificates'

def create_folder(folder):
    if os.path.exists(folder):
        os.chdir(folder)
        return 1
    else:
        try:
            os.makedirs(folder)
            dirs = os.path.dirname(folder)
        except OSError:
            print("Невозможно создать директорию")
            return 0
        else:
            print("Рабочий каталог %s создан"%dirs)
            return 1

status = create_folder(folder)
if status==0:
    print("Выход из программы")
    sys.exit()
else:
    print ("Продолжаем работу")
    os.chdir(folder)


def log_file (text, file_name):
    if os.path.isfile(file_name):
        with open(file_name, 'a', encoding='UTF-8') as file_name:
            file_name.write(text+'\r\n')
    else:
        with open(file_name, 'w', encoding='UTF-8') as file_name:    
            file_name.write(text+'\r\n')

resp = requests.get(site_for_parse).text
soup = BeautifulSoup(resp, "html.parser")
result = soup.findAll('div', id=re.compile('^caCertifcicatesGroupId'))

for i in result:
    result2 = i.findAll('td')
    for k in result2:
        if k.string!='cкачать':
            print(k.string)
        elif k.a:
            print(k.a.get('href'))
        # else:
        #     continue
