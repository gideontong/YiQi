from modules import *
import wx

def main():
    Dependency.versionCheck()
    MainWindow.main()
    print("The main function is running!")  

main()