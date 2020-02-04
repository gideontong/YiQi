"""
Creates the main window of YiQi. This should call helper functions in
other classes and scripts as necessary, and should only be used for
drawing the main text, windows, and managing the on-click events to be
handled by the user.
"""

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
        sizer.Add(st, wx.SizerFlags().Border(wx.TOP|wx.LEFT, 25))
        panel.SetSizer(sizer)

        # Create Menu Bar and Status Bar
        self.createMenu()
        self.CreateStatusBar()
        self.SetStatusText("YiQi Home Menu")


    def createMenu(self):
        """
        A menu bar is composed of menus, which are composed of menu items.
        This method builds a set of menus and binds handlers to be called
        when the menu item is selected.
        """

        # Create a File menu
        fileMenu = wx.Menu()
        helloItem = fileMenu.Append(-1, "&Hello...\tCtrl-H",
                "Help string shown in status bar for this menu item")
        fileMenu.AppendSeparator()
        exitItem = fileMenu.Append(wx.ID_EXIT)

        # Create a Help menu
        helpMenu = wx.Menu()
        aboutItem = helpMenu.Append(wx.ID_ABOUT)

        # Make the menu bar and add the two menus to it. The '&' defines
        # that the next letter is the "mnemonic" for the menu item. On the
        # platforms that support it those letters are underlined and can be
        # triggered from the keyboard.
        menuBar = wx.MenuBar()
        menuBar.Append(fileMenu, "&File")
        menuBar.Append(helpMenu, "&Help")

        # Give the menu bar to the frame
        self.SetMenuBar(menuBar)

        # Finally, associate a handler function with the EVT_MENU event for
        # each of the menu items. That means that when that menu item is
        # activated then the associated handler function will be called.
        self.Bind(wx.EVT_MENU, self.OnHello, helloItem)
        self.Bind(wx.EVT_MENU, self.OnExit,  exitItem)
        self.Bind(wx.EVT_MENU, self.OnAbout, aboutItem)


    def OnExit(self, event):
        """Close the frame, terminating the application."""
        self.Close(True)


    def OnHello(self, event):
        """Say hello to the user."""
        wx.MessageBox("Hello again from wxPython")


    def OnAbout(self, event):
        """Display an About Dialog"""
        wx.MessageBox("This is a wxPython Hello World sample",
                      "About Hello World 2",
                      wx.OK|wx.ICON_INFORMATION)

def main():
    app = wx.App()
    frm = MainWindow(None, title='YiQi')
    frm.Show()
    app.MainLoop()
    print("test")