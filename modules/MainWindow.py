"""
Creates the main window of YiQi. This should call helper functions in
other classes and scripts as necessary, and should only be used for
drawing the main text, windows, and managing the on-click events to be
handled by the user.
"""

from . import Config
from . import Dependency
import wx

class MainWindow(wx.Frame):
    """
    Manages the drawing of the main window of MainWindow for YiQi.
    """

    def __init__(self, *args, **kw):
        # Create the Panel
        super(MainWindow, self).__init__(*args, **kw)
        panel = wx.Panel(self)

        # Place text in the panel
        st = wx.StaticText(panel, label="YiQi Home")
        font = st.GetFont()
        font.PointSize += 10
        font = font.Bold()
        st.SetFont(font)

        # Set the size of all the child widgets
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(st, wx.SizerFlags().Border(wx.TOP | wx.LEFT, 25))
        panel.SetSizer(sizer)

        # Create Menu Bar and Status Bar
        self.createMenu()
        self.CreateStatusBar()
        self.SetStatusText("YiQi Home Menu")

    def createMenu(self):
        """
        This method builds a set of the menus for the main window and
        calls them as necessary when buttons are pressed.
        """

        # Create a File menu
        fileMenu = wx.Menu()
        optionsItem = fileMenu.Append(0, "&Options...\tCtrl-S",
                                      "Opens the YiQi settings")
        fileMenu.AppendSeparator()
        exitItem = fileMenu.Append(wx.ID_EXIT)

        # Create a Help menu
        helpMenu = wx.Menu()
        aboutItem = helpMenu.Append(wx.ID_ABOUT)

        # Create the Menu bar
        menuBar = wx.MenuBar()
        menuBar.Append(fileMenu, "&File")
        menuBar.Append(helpMenu, "&Help")
        self.SetMenuBar(menuBar)

        # Bing help functions to menu actions
        self.Bind(wx.EVT_MENU, self.OnOptions, optionsItem)
        self.Bind(wx.EVT_MENU, self.OnExit,    exitItem)
        self.Bind(wx.EVT_MENU, self.OnAbout,   aboutItem)

    def OnExit(self, event):
        """Close the frame, terminating the application."""
        self.Close(True)

    def OnOptions(self, event):
        """
        Give the user options so they can customize the application to
        do tasks that have been assigned to them, like logging in.
        """
        wx.MessageBox("Options Menu")

    def OnAbout(self, event):
        """
        Displays the About dialog for YiQi. Shows information linking
        to the website, as well as docs, support, version information
        and more.
        """
        wx.MessageBox(
            """
            Welcome to YiQi!
            Version: {}
            """.format(Dependency.getVersion()),
            "About YiQi",
            wx.OK | wx.ICON_INFORMATION)


def main():
    app = wx.App()
    frm = MainWindow(None, title='YiQi')
    frm.Show()
    app.MainLoop()
