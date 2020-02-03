import json
import sys

def versionCheck():
    with open('config/app.json') as configFile:
        config = json.load(configFile)
        minVersion = config['MIN_PYTHON']
        minPy = tuple(minVersion)
        if sys.version_info < minPy:
            sys.exit("Python %s.%s or later is required!\n" % minPy)