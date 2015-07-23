import wx

# see the included wxThreadExample.py file

# Define notification event for thread status
EVT_THREADSTATUS_ID = wx.ID_ANY

def EVT_THREADSTATUS(win, func):
    """Define Result Event."""
    win.Connect(-1, -1, EVT_THREADSTATUS_ID, func)

# this class exists for the sole purpose of passing data
class ThreadStatusEvent(wx.PyEvent):
    def __init__(self, data):
        """Init Result Event."""
        wx.PyEvent.__init__(self)
        self.SetEventType(EVT_THREADSTATUS_ID)
        self.data = data
