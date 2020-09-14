from bs4 import BeautifulSoup
import os
import html.parser
import sys
import requests
import re

folder = 'C:\\Users\\demom\\Desktop\\Parse_site\\Новая папка\\'
site_for_parse = 'https://ca.kontur.ru/about/certificates'

################### Блок с функциями ######################

def create_folder(folder):
    if os.path.exists(folder):
        return 1 
    else:
        try:
            os.makedirs(folder)
            print("Каталог создан")
            return 1
        except OSError:
            print("Невозможно создать директорию")
            return 0

def log_file (text, file_name):
    if os.path.isfile(file_name):
        with open(file_name, 'a', encoding='UTF-8') as file_name:
            file_name.write(text+'\n')
    else:
        with open(file_name, 'w', encoding='UTF-8') as file_name:    
            file_name.write(text+'\n')

def download_file(url, name):
    req = requests.get(url)
    file_data = req.content
    with open(name, 'wb') as f:
        f.write(file_data)

 #############################################

main_folder  = create_folder(folder)
os.chdir(folder)

if main_folder==0:
    print("Выход из программы")
    sys.exit()
else:
    print ("Продолжаем работу")
    os.chdir(folder)

resp = requests.get(site_for_parse).text
soup = BeautifulSoup(resp, "html.parser")
result = soup.findAll('div', id=re.compile('^caCertifcicatesGroupId'))



for i in result:
    result2 = i.findAll('td')
    for k in result2:
        if not re.search('Скачать', k.text):
            print(k.text)
            log_file(k.text, 'link.txt')
            # new_folder = k.text # использовать переменную для формирования записи файлов
            new_folder = create_folder(k.text)
        else:
            if  k.a.get('href').startswith('/Files') or k.a.get('href').startswith('/cdp/'):
                print('https://ca.kontur.ru'+k.a.get('href'))
                # cert_name = 'https://ca.kontur.ru'+k.a.get('href')
                log_file('https://ca.kontur.ru'+k.a.get('href'), 'link.txt')
                # url = r'https://ca.kontur.ru'+k.a.get('href') # использовать переменную для формирования записи файлов
                # download_file(url, cert_name)
                # name_file = re.search('\.(crt|crl|zip)$', k.a.get('href'))
                # print (name_file)
                # todo включить функцию по записи сертификатов в каталог
            else:
                print(k.a.get('href'))
                # cert_name = k.a.get('href')
                log_file(k.a.get('href'), 'link.txt')
                # url = k.a.get('href') 
                # # использовать переменную для формирования записи файлов
                # download_file(url, cert_name)