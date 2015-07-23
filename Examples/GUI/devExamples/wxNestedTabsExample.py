

# based on http://wiki.wxpython.org/Notebooks


import wx



class PanelOne(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent, id=wx.ID_ANY)
        
        sizer = wx.BoxSizer(wx.VERTICAL)
        self.txtOne = wx.TextCtrl(self, wx.ID_ANY, "")
        self.txtTwo = wx.TextCtrl(self, wx.ID_ANY, "")
        
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.txtOne, 0, wx.ALL, 5)
        sizer.Add(self.txtTwo, 0, wx.ALL, 5)
        
        self.SetSizer(sizer)



class NestedPanel(wx.Panel):
    def __init__(self, parent):
        
        wx.Panel.__init__(self, parent=parent, id=wx.ID_ANY)
        
        sizer = wx.BoxSizer(wx.VERTICAL)
        
        # Create some nested tabs on the first tab
        nestedNotebook = wx.Notebook(self, wx.ID_ANY)
        nestedTabOne = PanelOne(nestedNotebook)
        nestedTabOne.txtOne.AppendText('NT 1 Text 1')
        nestedTabOne.txtTwo.AppendText('NT 1 Text 2')
        
        nestedTabTwo = PanelOne(nestedNotebook)
        nestedTabTwo.txtOne.AppendText('NT 2 Text 1')
        nestedTabTwo.txtTwo.AppendText('NT 2 Text 2')
        
        nestedNotebook.AddPage(nestedTabOne, "NestedTabOne")
        nestedNotebook.AddPage(nestedTabTwo, "NestedTabTwo")
        
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(nestedNotebook, 1, wx.ALL|wx.EXPAND, 5)
                
        self.SetSizer(sizer)



class NestedNotebookDemo(wx.Notebook):
    def __init__(self, parent):
        wx.Notebook.__init__(self, parent, id=wx.ID_ANY, style=wx.BK_DEFAULT)
        
        # Create the first tab and add it to the notebook
        tabOne = NestedPanel(self)
        self.AddPage(tabOne, "TabOne")
                
        # Create and add the second tab
        tabTwo = PanelOne(self)
        self.AddPage(tabTwo, "TabTwo")
        
        # Create and add the third tab
        self.AddPage(PanelOne(self), "TabThree")
        
        self.Bind(wx.EVT_NOTEBOOK_PAGE_CHANGED, self.OnPageChanged) # prints msg
        self.Bind(wx.EVT_NOTEBOOK_PAGE_CHANGING, self.OnPageChanging) # prints msg


    def OnPageChanged(self, event):
        old = event.GetOldSelection()
        new = event.GetSelection()
        sel = self.GetSelection()
        print 'OnPageChanged,  old:%d, new:%d, sel:%d\n' % (old, new, sel)
        event.Skip()


    def OnPageChanging(self, event):
        old = event.GetOldSelection()
        new = event.GetSelection()
        sel = self.GetSelection()
        print 'OnPageChanging, old:%d, new:%d, sel:%d\n' % (old, new, sel)
        event.Skip()



class DemoFrame(wx.Frame):
    
    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY, 
                          "Notebook Tutorial",
                          size=(600,400)
                          )
        panel = wx.Panel(self)
        
        notebook = NestedNotebookDemo(panel)
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(notebook, 1, wx.ALL|wx.EXPAND, 5)
        panel.SetSizer(sizer)
        self.Layout()
        
        self.Show()



if __name__ == "__main__":
    app = wx.PySimpleApp()
    frame = DemoFrame()
    app.MainLoop()
