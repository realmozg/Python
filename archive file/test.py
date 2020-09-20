import shutil
import os
import datetime
import zipfile
import subprocess
import sys
import xml.etree.ElementTree
import logging
import configparser

def create_folder(path, name):
    if os.path.exists(os.path.join(path, name)):
        folder = os.path.join(path, name)
        print(f"Каталог {folder} уже существует")
        return folder
    else:
        try:
            folder = os.path.join(path, name)
            os.makedirs(folder)
            return folder
        except OSError:
            folder = os.path.join(path, name)
            print(f"Невозможно создать каталог {folder}")
            log_write(f"Невозможно создать каталог {folder}")
            return 0

def log_write(text):
    logging.basicConfig(filename='2020-09-19.log', level=logging.INFO)
    logging.warning(text, exc_info = True)
    logging.info(text, exc_info = True)
    logging.error(text, exc_info = True)        

##if __name__ == '__main__':
    
