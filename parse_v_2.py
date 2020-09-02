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
            file_name.write(text+'\n')
    else:
        with open(file_name, 'w', encoding='UTF-8') as file_name:    
            file_name.write(text+'\n')

resp = requests.get(site_for_parse).text
soup = BeautifulSoup(resp, "html.parser")
result = soup.findAll(id=re.compile('^caCertifcicatesGroupId'))

for i in result:
    print(str(i.td.text)+"\n\n")
    print(str(i.td.a.get('href'))+"\n\n")


# openfile = open(file, "r", encoding="UTF-8")
# file_log = open(file_log, "w", encoding="UTF-8")

# contents = openfile.read()

# soup = BeautifulSoup(contents, 'html.parser')



# print(soup.td.text)
# print(soup.a['href'])

# list_td = soup.find_all('td')

# for href in list_td:
	
# 	print (href.children)
# 	print (href.text)


# file_log.close()
# openfile.close()
