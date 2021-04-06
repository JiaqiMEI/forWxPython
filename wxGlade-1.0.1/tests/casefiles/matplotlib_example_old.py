#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# generated by wxGlade 0.8.0a7 on Mon Nov  6 20:03:46 2017
#

# extra code at start

import wx

# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
import matplotlib
from matplotlib.figure import Figure
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
# end wxGlade


class MyFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyFrame.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.panel_1 = wx.Panel(self, wx.ID_ANY)
        figure = self.matplotlib_figure = Figure()
        # 1x1 grid, first subplot
        self.matplotlib_axes = figure.add_subplot(111)
        self.matplotlib_canvas = FigureCanvas(self.panel_1, wx.ID_ANY, figure)
        self.text_function = wx.TextCtrl(self.panel_1, wx.ID_ANY, "sin(x)")
        self.text_xmin = wx.TextCtrl(self.panel_1, wx.ID_ANY, "0")
        self.text_max = wx.TextCtrl(self.panel_1, wx.ID_ANY, "10")
        self.text_xstep = wx.TextCtrl(self.panel_1, wx.ID_ANY, "0.1")
        self.button_plot = wx.Button(self.panel_1, wx.ID_ANY, "Plot")
        self.button_clear = wx.Button(self.panel_1, wx.ID_ANY, "Clear")

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_BUTTON, self.on_button_plot, self.button_plot)
        # end wxGlade
        # some extra code at end of MyFrame

    def __set_properties(self):
        # begin wxGlade: MyFrame.__set_properties
        self.SetTitle("matplotlib canvas example")
        self.text_xmin.SetMinSize((40, -1))
        self.text_max.SetMinSize((40, -1))
        self.text_xstep.SetMinSize((40, -1))
        self.button_plot.SetDefault()
        # end wxGlade
    def __do_layout(self):
        # begin wxGlade: MyFrame.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_2 = wx.BoxSizer(wx.VERTICAL)
        sizer_3 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_4 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_2.Add(self.matplotlib_canvas, 1, wx.ALL | wx.EXPAND, 3)
        label_4 = wx.StaticText(self.panel_1, wx.ID_ANY, "f(x) = ")
        sizer_4.Add(label_4, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)
        sizer_4.Add(self.text_function, 1, 0, 0)
        sizer_2.Add(sizer_4, 0, wx.ALL | wx.EXPAND, 5)
        label_1 = wx.StaticText(self.panel_1, wx.ID_ANY, "xmin")
        sizer_3.Add(label_1, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_3.Add(self.text_xmin, 0, 0, 0)
        label_2 = wx.StaticText(self.panel_1, wx.ID_ANY, "xmax")
        sizer_3.Add(label_2, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_3.Add(self.text_max, 0, 0, 0)
        label_3 = wx.StaticText(self.panel_1, wx.ID_ANY, "step")
        sizer_3.Add(label_3, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_3.Add(self.text_xstep, 0, 0, 0)
        sizer_3.Add((20, 20), 1, 0, 0)
        sizer_3.Add(self.button_plot, 0, 0, 0)
        sizer_3.Add(self.button_clear, 0, wx.LEFT, 8)
        sizer_2.Add(sizer_3, 0, wx.ALL | wx.EXPAND, 5)
        self.panel_1.SetSizer(sizer_2)
        sizer_1.Add(self.panel_1, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        self.Layout()
        self.SetSize((400, 300))
        # end wxGlade

    def on_button_plot(self, event):  # wxGlade: MyFrame.<event_handler>
        import numpy
        xmin = xmax = step = None
        try:
            xmin = float( self.text_xmin.GetValue() )
            self.text_xmin.SetBackgroundColour(wx.WHITE)
        except:
            self.text_xmin.SetBackgroundColour(wx.RED)
        try:
            xmax = float( self.text_max.GetValue() )
            self.text_max.SetBackgroundColour(wx.WHITE)
        except:
            self.text_max.SetBackgroundColour(wx.RED)
        try:
            step = float( self.text_xstep.GetValue() )
            self.text_xstep.SetBackgroundColour(wx.WHITE)
        except:
            self.text_xstep.SetBackgroundColour(wx.RED)
            
        x = numpy.arange(xmin, xmax, step)
        # build globals with some functions
        g = {}
        for name in ["sin","cos","tan","ufunc","square"]:
            g[name] = getattr(numpy, name)
        y = eval(self.text_function.GetValue(), g, {"numpy":numpy, "x":x})
        self.matplotlib_axes.plot(x,y)
        self.matplotlib_canvas.draw()
        event.Skip()

# end of class MyFrame

class MyApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame(None, wx.ID_ANY, "")
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True

# end of class MyApp

# extra code after MyApp

if __name__ == "__main__":
    app = MyApp(0)
    app.MainLoop()
