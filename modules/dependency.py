"""
Checks and manages for dependencies of YiQi in terms of the Python
program to include packages and package repositories that are
needed for YiQi to successfully run.
"""

import json
import sys

config = {}

def getVersion():
    """
    getVersion returns the current version of the YiQi application.
    """
    return config['version']

def versionCheck():
    """
    verisonCheck checks whether or not the current running version of
    Python is new enough to run by checking the dependency defined in
    app.json.
    """
    minVersion = config['MIN_PYTHON']
    minPy = tuple(minVersion) # Set the minimum Python version
    if sys.version_info < minPy:
        sys.exit("Python %s.%s or later is required!\n" % minPy)

def getHostUrl(host: str) -> str:
    """
    getHostUrl returns the corresponding HOST URL defined in app.json.
    There is intentionally no serialization or type-checking because
    this function should only be called by the programming without
    passing any input so in theory this is not an attackable vector.
    """
    return config['sites'][host]

def main():
    """
    The main function is called when the app first starts by calling
    the dependency from main.py. It reads the current vesrion of the
    config and loads it into memory.
    """
    global config
    with open('config/app.json') as configFile:
        config = json.load(configFile)

main()