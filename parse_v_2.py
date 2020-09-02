from bs4 import BeautifulSoup
import os
import html.parser
import sys

folder = 'C:\\Users\\demom\\Desktop\\Parse_site\\'
source_file = folder+'site.html'
file_log = folder+'log.txt'

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
