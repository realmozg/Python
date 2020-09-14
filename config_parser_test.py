import configparser
import os


def create_config (name, section, option, value):
    config = configparser.ConfigParser()
    config.add_section(section)
    config.set(section, option, value)
    if os.path.exists(os.path.abspath(os.getcwd())+name):
        with open ('settings.ini', 'w') as config_file:
            config.write(config_file)
    else:
        with open ('settings.ini', 'a') as config_file:
            config.write(config_file)
