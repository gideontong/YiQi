"""
The main function of YiQi. Run this file in order to run the whole
program without compiling in the Python interpreter. Should 
immediately bring up a window for the user to interact with.
"""

from modules import *
import wx

def main():
    """
    The main routine of YiQi starts the dependencies and initializes
    the configuration files, then starts the main window.
    """

    Dependency.versionCheck()
    Config.main()
    MainWindow.main()

main()