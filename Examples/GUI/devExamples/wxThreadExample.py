

# This example is based on http://wiki.wxpython.org/LongRunningTasks


import time
import threading
import wx

# Button definitions
ID_START = wx.NewId()
ID_STOP = wx.NewId()

# Define notification event for thread status
EVT_RESULT_ID = wx.NewId()


def EVT_RESULT(win, func):
    """Define Result Event."""
    win.Connect(-1, -1, EVT_RESULT_ID, func)



# this class exists for the sole purpose of passing data
class ResultEvent(wx.PyEvent):
    def __init__(self, data):
        """Init Result Event."""
        wx.PyEvent.__init__(self)
        self.SetEventType(EVT_RESULT_ID)
        self.data = data



# Thread class that executes processing
class WorkerThread(threading.Thread):
    """Worker Thread Class."""
    def __init__(self, notify_window):
        """Init Worker Thread Class."""
        threading.Thread.__init__(self)
        self._notify_window = notify_window
        self._want_abort = 0
        # This starts the thread running on creation, but you could
        # also make the GUI thread responsible for calling this
        self.start()


    def run(self):
        """Run Worker Thread."""
        # This is the code executing in the new thread. Simulation of
        # a long process as a simple loop with time.sleep()
        for i in range(10):
            
            # this example decodes the event data *type*, here a string
            wx.PostEvent(self._notify_window, ResultEvent(str(i) + " of 10"))
            
            time.sleep(1.0)
            if self._want_abort:
                
                # this example decodes the event data *type*, here None
                wx.PostEvent(self._notify_window, ResultEvent(None))
                return
        # # this example decodes the event data *type*, here an integer
        wx.PostEvent(self._notify_window, ResultEvent(10))


    def abort(self):
        """abort worker thread."""
        # Method for use by main thread to signal an abort
        self._want_abort = 1



# GUI Frame class that spins off the worker thread
class MainFrame(wx.Frame):
    """Class MainFrame."""
    def __init__(self, parent, id):
        """Create the MainFrame."""
        wx.Frame.__init__(self, parent, id, 'Thread Test')

        # Dumb sample frame with two buttons
        wx.Button(self, ID_START, 'Start Separate Thread', pos=(0,0))
        wx.Button(self, ID_STOP, 'Stop Separate Thread', pos=(0,50))
        self.status = wx.StaticText(self, -1, '', pos=(0,100))

        self.Bind(wx.EVT_BUTTON, self.OnStart, id=ID_START)
        self.Bind(wx.EVT_BUTTON, self.OnStop, id=ID_STOP)

        # Set up event handler for any worker thread results
        EVT_RESULT(self, self.OnResult)

        # And indicate we don't have a worker thread yet
        self.worker = None


    def OnStart(self, event):
        """Start Computation."""
        # Trigger the worker thread unless it's already busy
        if not self.worker:
            self.status.SetLabel('Starting computation')
            self.worker = WorkerThread(self)


    def OnStop(self, event):
        """Stop Computation."""
        # Flag the worker thread to stop if running
        if self.worker:
            self.status.SetLabel('Trying to abort computation')
            self.worker.abort()


    def OnResult(self, event):
        """Show Result status."""
        if type(event.data) == type(''): # I use string data for status updates
            self.status.SetLabel('Intermediate Result: ' + event.data)
        elif event.data is None:
            # Thread aborted (using our convention of None as event data)
            self.status.SetLabel('Computation aborted')
            self.worker = None # the worker thread was aborted, so it is done
        else:
            # Process final results here
            self.status.SetLabel('Computation Completed, Result: %s' % event.data)
            self.worker = None # the worker thread completed



class MainApp(wx.App):
    """Class Main App."""
    def OnInit(self):
        """Init Main App."""
        self.frame = MainFrame(None, -1)
        self.frame.Show(True)
        self.SetTopWindow(self.frame)
        return True

if __name__ == '__main__':
    app = MainApp(0)
    app.MainLoop()
