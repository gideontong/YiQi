"""
Checks and manages for dependencies of YiQi in terms of the Python
program to include packages and package repositories that are
needed for YiQi to successfully run.
"""

import json
import sys

config = {}

def getVersion():
    return config['version']

def versionCheck():
    minVersion = config['MIN_PYTHON']
    minPy = tuple(minVersion) # Set the minimum Python version
    if sys.version_info < minPy:
        sys.exit("Python %s.%s or later is required!\n" % minPy)

def main():
    global config
    with open('config/app.json') as configFile:
        config = json.load(configFile)

main()