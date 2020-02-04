"""
Config subroutine for YiQi. Manages configuration files in order for
other parts of the program to call back to and get user data.
"""

import json
import os
import shutil

configPath = 'config/keys.json'
emptyConfigPath = 'config/keyBlanks.json'

def init():
    """
    Initializes the config file. If a file exists, loads the config
    file into the configs variable for access later and sets the
    file to global. If it doesn't exist or the file cannot be
    decoded, the file is destroyed and recreated.
    """

    global configs
    try:
        configFile = open(configPath)
    except FileNotFoundError:
        dest = shutil.copyfile(configPath, emptyConfigPath)
        configFile = open(dest)
    finally:
        try:
            configs = json.load(configFile)
        # If there is an issue, reset the config file
        except json.decoder.JSONDecodeError:
            configFile.close()
            os.remove(configPath)
            init()
        configFile.close()

def exit():
    configFile = open(configPath, 'w')
    json.dump(configs, configFile)
    configFile.close()

def main():
    """
    The main function of Config handles the initialization of the
    entire class to ensure that the data is clear and usable.
    """
    init()
    exit()

main()