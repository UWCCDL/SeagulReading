"""
GUI for Seagul Reading Project
"""


import wx

class SeagulFrame(wx.Frame):

  def __init__(self):
    wx.Frame.__init__(self, None, wx.ID_ANY, "Seagul Reading") 
    self.panel = wx.Panel(self)
    self.Bind(wx.EVT_CLOSE, self.on_close)
    self.button = wx.Button(self.panel, label="Start")
    # listener
    self.button.Bind(wx.EVT_BUTTON, self.on_start)


  def on_start(self, event):
    """
    Start information recording window
    """
    info_window = StartWindow()
    info_window.Show()
    
  def on_close(self, event):
    self.Destroy()


class StartWindow(wx.Frame):

  def __init__(self):
    wx.Frame.__init__(self, None, wx.ID_ANY, "Please enter your information:") 
    self.panel = wx.Panel(self)
    self.Bind(wx.EVT_CLOSE, self.on_close)
    # Subject recording
    self.name_txt = wx.TextCtrl(self.panel, -1, style=wx.TE_CENTRE, size=(250, -1))
    self.name_txt.SetValue("Your name (Last, First): ") 
    self.exp_txt = wx.TextCtrl(self.panel, -1, style=wx.TE_CENTRE, size=(250, -1)) 
    self.exp_txt.SetValue("Your experiment number: ")   
    # boxer
    sizer = wx.BoxSizer(wx.VERTICAL)
    sizer.Add(self.name_txt, 1, wx.ALL|wx.ALIGN_CENTER, 5)
    sizer.Add(self.exp_txt, 1, wx.ALL|wx.ALIGN_CENTER, 5)
    self.panel.SetSizer(sizer)
    # button
    hbox = wx.BoxSizer(wx.HORIZONTAL)
    self.submit_btn = wx.Button(self.panel, label="Submit")
    self.cancel_btn = wx.Button(self.panel, label="Cancel")
    hbox.Add(self.submit_btn)
    hbox.Add(self.cancel_btn)
    sizer.Add(hbox, 1, wx.ALL|wx.ALIGN_CENTER, 5)
    # bind buttons
    self.cancel_btn.Bind(wx.EVT_BUTTON, self.on_cancel)


  def on_close(self, event):
    self.Destroy()
 
  def on_cancel(self, event):
    self.on_close(event) 

if __name__ == "__main__":
  app = wx.App(False)
  frame = SeagulFrame()
  frame.Show()

  app.MainLoop()