import shutil
import os
import datetime
import zipfile
import subprocess
import sys
import xml.etree.ElementTree
import logging
import configparser

def config_file():
    if not os.path.exists(os.path.join(os.getcwd(),'settings.ini')):
        path = os.path.join(os.getcwd(),'settings.ini')
        config = configparser.ConfigParser()
        section_dict = {
                        'Настройка каталогов':{'Каталог входящих уведомлений IN':'',
                                               'Каталог исходящих уведомлений OUT':'',
                                               'Каталог для передачи уведомлений Inbound':'',
                                               'Каталог для поиска ответов Outbound':'',
                                               'Каталог лог файлов':'',
                                               'Каталог базы данных':'',
                                               'Временный каталог':'',
                                               'Архивные файлы':''},
                             'Настройка базы':{'Название базы':'',
                                               'Имя пользователя':'',
                                               'Пароль':''},
                        'Настройка архивации':{'Архивировать входящие уведомления':'',
                                               'Максимальный размер архива (МБ)':'',
                                               'Создавать лог файл по каждому архиву':''}
                        }
        config.read_dict(section_dict)
        with open(path, 'w') as file:
            config.write(file)
    else:
        pass

def create_folder(path, name):
    if os.path.exists(os.path.join(path, name)):
        folder = os.path.join(path, name)
        print(f'Каталог {folder} уже существует')
        return folder
    else:
        try:
            folder = os.path.join(path, name)
            os.makedirs(folder)
            return folder
        except OSError:
            folder = os.path.join(path, name)
            # print(f"Невозможно создать каталог {folder}")
            error = sys.exc_info()[1]
            print(type(error))
            log_write(error)
            return 0

def log_write(text):
    log_date = datetime.datetime.now().strftime('%d.%m.%yyyy')
    logging.basicConfig(filename=log_date + '.log', format='%(name)s - %(asctime)s- %(levelname)s - %(message)s', datefmt='%d.%m.%Y %H:%M:%S', level=logging.WARN)
##    logging.warning(text, exc_info = True)
    logging.info(text)
##    logging.error(text, exc_info = True)




##if __name__ == '__main__':
    
