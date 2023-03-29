import configparser
import os

def base_settings(path: str):
    config = configparser.ConfigParser()
    config.add_section('user')

    config['user']['steam'] = '0'
    with open(path, 'w') as configfile:
        config.write(configfile)
    return

def check_setting(path: str, section: str, set: str)->str:
    config = configparser.ConfigParser()
    config_settings = os.path.join(path, "settings.ini")
    config.read(config_settings)
    data = config[section][set]
    return data

def change_setting(path: str, section: str, set: str, change: str):
    config = configparser.ConfigParser()
    config_settings = os.path.join(path, "settings.ini")
    config.read(config_settings)
    config.set(section, set, change)
    with open(config_settings, 'w') as configfile:
        config.write(configfile)
    return

def load_window_settings(path: str)->list:
    output = list()
    config = configparser.ConfigParser()
    config_settings = os.path.join(path, "settings.ini")
    config.read(config_settings)
    if config['user']['steam'] != '0':
        output.append('s')
    
    return output