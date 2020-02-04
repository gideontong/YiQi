"""
Checks and manages for dependencies of YiQi in terms of the Python
program to include packages and package repositories that are
needed for YiQi to successfully run.
"""

import json
import sys

minPy = (0, 0)
ver = ""

def getVersion():
    return ver

def versionCheck():
    if sys.version_info < minPy:
        sys.exit("Python %s.%s or later is required!\n" % minPy)

def main():
    global minPy, ver
    with open('config/app.json') as configFile:
        config = json.load(configFile)
        minVersion = config['MIN_PYTHON']
        minPy = tuple(minVersion) # Set the minimum Python version
        ver = config['version']

main()