from bs4 import BeautifulSoup
import os
import requests 
import csv

folder = 'C:\\Users\\demom\\OneDrive\\Рабочий стол\\Parse\\'
file_log = 'C:\\Users\\demom\\OneDrive\\Рабочий стол\\Parse\\log.txt'
url = 'https://ca.kontur.ru/about/certificates'

response = requests.get(url)
status = response.status_code
text_for_parse = response.text

print(status)
print(requests.status_codes)

os.chdir(folder)

file_log = open(file_log, "w", encoding="UTF-8")

soup = BeautifulSoup(text_for_parse, 'html.parser')

for name in soup.find_all('td'):
        
        if name.text != 'Скачать':
                file_log.write(name.text + '\n')
        elif name.a:
                if name.a.get('href').startswith('/Files') or name.a.get('href').startswith('/cdp/'):
                      file_log.write('https://ca.kontur.ru'+name.a.get('href')+'\n')
                else:
                        file_log.write(name.a.get('href')+'\n')

        else:
                continue

file_log.close()

