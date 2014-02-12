#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# generated by wxGlade 0.6.8 (standalone edition) on Tue Jan 14 12:09:36 2014
#

import wx
import wx.grid

# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class MyFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyFrame.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.statusbar = self.CreateStatusBar(5, wx.ST_SIZEGRIP)
        self.SplitterWindow = wx.SplitterWindow(self, wx.ID_ANY, style=wx.SP_3D | wx.SP_BORDER)
        self.window_1_pane_1 = wx.ScrolledWindow(self.SplitterWindow, wx.ID_ANY, style=wx.SIMPLE_BORDER | wx.TAB_TRAVERSAL)
        self.pnlSettingBar = wx.Panel(self.window_1_pane_1, wx.ID_ANY)
        self.btnHideBar = wx.Button(self.pnlSettingBar, wx.ID_ANY, "Hide")
        self.btnEnumPorts = wx.Button(self.pnlSettingBar, wx.ID_ANY, "EnumPorts")
        self.label_1 = wx.StaticText(self.pnlSettingBar, wx.ID_ANY, "Port")
        self.cmbPort = wx.ComboBox(self.pnlSettingBar, wx.ID_ANY, choices=[], style=wx.CB_DROPDOWN)
        self.label_2 = wx.StaticText(self.pnlSettingBar, wx.ID_ANY, "Baud Rate")
        self.cmbBaudRate = wx.ComboBox(self.pnlSettingBar, wx.ID_ANY, choices=["300", "600", "1200", "1800", "2400", "4800", "9600", "19200", "38400", "57600", "115200", "230400", "460800", "500000", "576000", "921600", "1000000", "1152000", "1500000", "2000000", "2500000", "3000000", "3500000", "4000000"], style=wx.CB_DROPDOWN)
        self.label_3 = wx.StaticText(self.pnlSettingBar, wx.ID_ANY, "Data Bits")
        self.choiceDataBits = wx.Choice(self.pnlSettingBar, wx.ID_ANY, choices=["5", "6", "7", "8"])
        self.label_4 = wx.StaticText(self.pnlSettingBar, wx.ID_ANY, "Parity")
        self.choiceParity = wx.Choice(self.pnlSettingBar, wx.ID_ANY, choices=["None", "Even", "Odd", "Mark", "Space"])
        self.label_5 = wx.StaticText(self.pnlSettingBar, wx.ID_ANY, "Stop Bits")
        self.choiceStopBits = wx.Choice(self.pnlSettingBar, wx.ID_ANY, choices=["1", "1.5", "2"])
        self.chkboxrtscts = wx.CheckBox(self.pnlSettingBar, wx.ID_ANY, "RTS/CTS")
        self.chkboxxonxoff = wx.CheckBox(self.pnlSettingBar, wx.ID_ANY, "Xon/Xoff")
        self.sizer_6_staticbox = wx.StaticBox(self.pnlSettingBar, wx.ID_ANY, "HandShake")
        self.btnOpen = wx.Button(self.pnlSettingBar, wx.ID_ANY, "Open")
        self.btnClear = wx.Button(self.pnlSettingBar, wx.ID_ANY, "Clear Screen")
        self.window_1_pane_2 = wx.Panel(self.SplitterWindow, wx.ID_ANY, style=wx.SIMPLE_BORDER | wx.TAB_TRAVERSAL)
        self.SplitterWindow2 = wx.SplitterWindow(self.window_1_pane_2, wx.ID_ANY, style=wx.SP_3D | wx.SP_BORDER)
        self.window_2_pane_1 = wx.ScrolledWindow(self.SplitterWindow2, wx.ID_ANY, style=wx.SIMPLE_BORDER | wx.TAB_TRAVERSAL)
        self.txtctlMain = wx.TextCtrl(self.window_2_pane_1, wx.ID_ANY, "", style=wx.TE_MULTILINE | wx.TE_RICH | wx.TE_RICH2 | wx.TE_AUTO_URL | wx.TE_LINEWRAP | wx.TE_WORDWRAP | wx.NO_BORDER)
        self.window_2_pane_2 = wx.Panel(self.SplitterWindow2, wx.ID_ANY, style=wx.SIMPLE_BORDER | wx.TAB_TRAVERSAL)
        self.pnlGrid = wx.ScrolledWindow(self.window_2_pane_2, wx.ID_ANY, style=wx.DOUBLE_BORDER | wx.TAB_TRAVERSAL)
        self.button_1 = wx.Button(self.pnlGrid, wx.ID_ANY, "Send1")
        self.button_2 = wx.Button(self.pnlGrid, wx.ID_ANY, "Send2")
        self.button_3 = wx.Button(self.pnlGrid, wx.ID_ANY, "Send3")
        self.button_4 = wx.Button(self.pnlGrid, wx.ID_ANY, "Send4")
        self.button_5 = wx.Button(self.pnlGrid, wx.ID_ANY, "Send5")
        self.button_6 = wx.Button(self.pnlGrid, wx.ID_ANY, "Send6")
        self.button_7 = wx.Button(self.pnlGrid, wx.ID_ANY, "Send7")
        self.button_8 = wx.Button(self.pnlGrid, wx.ID_ANY, "Send8")
        self.button_9 = wx.Button(self.pnlGrid, wx.ID_ANY, "Send9")
        self.button_10 = wx.Button(self.pnlGrid, wx.ID_ANY, "Send10")
        self.button_11 = wx.Button(self.pnlGrid, wx.ID_ANY, "Send 11")
        self.button_12 = wx.Button(self.pnlGrid, wx.ID_ANY, "Send 12")
        self.button_13 = wx.Button(self.pnlGrid, wx.ID_ANY, "Send 13")
        self.button_14 = wx.Button(self.pnlGrid, wx.ID_ANY, "Send 14")
        self.button_15 = wx.Button(self.pnlGrid, wx.ID_ANY, "Send 15")
        self.button_16 = wx.Button(self.pnlGrid, wx.ID_ANY, "Send 16")
        self.button_17 = wx.Button(self.pnlGrid, wx.ID_ANY, "Send 17")
        self.button_18 = wx.Button(self.pnlGrid, wx.ID_ANY, "Send 18")
        self.button_19 = wx.Button(self.pnlGrid, wx.ID_ANY, "Send 19")
        self.button_20 = wx.Button(self.pnlGrid, wx.ID_ANY, "Send 20")
        self.button_21 = wx.Button(self.pnlGrid, wx.ID_ANY, "Send 21")
        self.button_22 = wx.Button(self.pnlGrid, wx.ID_ANY, "Send 22")
        self.button_23 = wx.Button(self.pnlGrid, wx.ID_ANY, "Send 23")
        self.button_24 = wx.Button(self.pnlGrid, wx.ID_ANY, "Send 24")
        self.button_25 = wx.Button(self.pnlGrid, wx.ID_ANY, "Send 25")
        self.button_26 = wx.Button(self.pnlGrid, wx.ID_ANY, "Send 26")
        self.button_27 = wx.Button(self.pnlGrid, wx.ID_ANY, "Send 27")
        self.button_28 = wx.Button(self.pnlGrid, wx.ID_ANY, "Send 28")
        self.button_29 = wx.Button(self.pnlGrid, wx.ID_ANY, "Send 29")
        self.button_30 = wx.Button(self.pnlGrid, wx.ID_ANY, "Send 30")
        self.button_31 = wx.Button(self.pnlGrid, wx.ID_ANY, "Send 31")
        self.button_32 = wx.Button(self.pnlGrid, wx.ID_ANY, "Send 32")
        self.button_33 = wx.Button(self.pnlGrid, wx.ID_ANY, "Send 33")
        self.button_34 = wx.Button(self.pnlGrid, wx.ID_ANY, "Send 34")
        self.button_35 = wx.Button(self.pnlGrid, wx.ID_ANY, "Send 35")
        self.button_36 = wx.Button(self.pnlGrid, wx.ID_ANY, "Send 36")
        self.button_37 = wx.Button(self.pnlGrid, wx.ID_ANY, "Send 37")
        self.button_38 = wx.Button(self.pnlGrid, wx.ID_ANY, "Send 38")
        self.button_39 = wx.Button(self.pnlGrid, wx.ID_ANY, "Send 39")
        self.button_40 = wx.Button(self.pnlGrid, wx.ID_ANY, "Send 40")
        self.button_41 = wx.Button(self.pnlGrid, wx.ID_ANY, "Send 41")
        self.button_42 = wx.Button(self.pnlGrid, wx.ID_ANY, "Send 42")
        self.button_43 = wx.Button(self.pnlGrid, wx.ID_ANY, "Send 43")
        self.button_44 = wx.Button(self.pnlGrid, wx.ID_ANY, "Send 44")
        self.button_45 = wx.Button(self.pnlGrid, wx.ID_ANY, "Send 45")
        self.button_46 = wx.Button(self.pnlGrid, wx.ID_ANY, "Send 46")
        self.button_47 = wx.Button(self.pnlGrid, wx.ID_ANY, "Send 47")
        self.button_48 = wx.Button(self.pnlGrid, wx.ID_ANY, "Send 48")
        self.button_49 = wx.Button(self.pnlGrid, wx.ID_ANY, "Send 49")
        self.button_50 = wx.Button(self.pnlGrid, wx.ID_ANY, "Send 50")
        self.grid_csv = wx.grid.Grid(self.pnlGrid, wx.ID_ANY, size=(1, 1))
        self.pnlTransmitHex = wx.Panel(self.window_2_pane_2, wx.ID_ANY)
        self.label_6 = wx.StaticText(self.pnlTransmitHex, wx.ID_ANY, "Transmit Hex")
        self.btnTransmitHex = wx.Button(self.pnlTransmitHex, wx.ID_ANY, "Transmit")
        self.txtTransmitHex = wx.TextCtrl(self.pnlTransmitHex, wx.ID_ANY, "", style=wx.TE_MULTILINE | wx.TE_LINEWRAP | wx.TE_WORDWRAP)

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MyFrame.__set_properties
        self.SetTitle("MyTerm")
        self.SetSize((1300, 700))
        self.statusbar.SetStatusWidths([-28, -10, -10, 55, 105])
        # statusbar fields
        statusbar_fields = ["", "Rx:0", "Tx:0", "Rx:Ascii", "Local echo:Off"]
        for i in range(len(statusbar_fields)):
            self.statusbar.SetStatusText(statusbar_fields[i], i)
        self.cmbBaudRate.SetSelection(7)
        self.choiceDataBits.SetSelection(3)
        self.choiceParity.SetSelection(0)
        self.choiceStopBits.SetSelection(0)
        self.btnOpen.SetMinSize((-1, 30))
        self.btnClear.SetMinSize((-1, 30))
        self.pnlSettingBar.SetMinSize((158, -1))
        self.window_1_pane_1.SetScrollRate(1, 1)
        self.txtctlMain.SetFont(wx.Font(10, wx.MODERN, wx.NORMAL, wx.NORMAL, 0, "Consolas"))
        self.window_2_pane_1.SetScrollRate(10, 10)
        self.button_1.SetMinSize((-1, 20))
        self.button_2.SetMinSize((-1, 20))
        self.button_3.SetMinSize((-1, 20))
        self.button_4.SetMinSize((-1, 20))
        self.button_5.SetMinSize((-1, 20))
        self.button_6.SetMinSize((-1, 20))
        self.button_7.SetMinSize((-1, 20))
        self.button_8.SetMinSize((-1, 20))
        self.button_9.SetMinSize((-1, 20))
        self.button_10.SetMinSize((-1, 20))
        self.button_11.SetMinSize((-1, 20))
        self.button_12.SetMinSize((-1, 20))
        self.button_13.SetMinSize((-1, 20))
        self.button_14.SetMinSize((-1, 20))
        self.button_15.SetMinSize((-1, 20))
        self.button_16.SetMinSize((-1, 20))
        self.button_17.SetMinSize((-1, 20))
        self.button_18.SetMinSize((-1, 20))
        self.button_19.SetMinSize((-1, 20))
        self.button_20.SetMinSize((-1, 20))
        self.button_21.SetMinSize((-1, 20))
        self.button_22.SetMinSize((-1, 20))
        self.button_23.SetMinSize((-1, 20))
        self.button_24.SetMinSize((-1, 20))
        self.button_25.SetMinSize((-1, 20))
        self.button_26.SetMinSize((-1, 20))
        self.button_27.SetMinSize((-1, 20))
        self.button_28.SetMinSize((-1, 20))
        self.button_29.SetMinSize((-1, 20))
        self.button_30.SetMinSize((-1, 20))
        self.button_31.SetMinSize((-1, 20))
        self.button_32.SetMinSize((-1, 20))
        self.button_33.SetMinSize((-1, 20))
        self.button_34.SetMinSize((-1, 20))
        self.button_35.SetMinSize((-1, 20))
        self.button_36.SetMinSize((-1, 20))
        self.button_37.SetMinSize((-1, 20))
        self.button_38.SetMinSize((-1, 20))
        self.button_39.SetMinSize((-1, 20))
        self.button_40.SetMinSize((-1, 20))
        self.button_41.SetMinSize((-1, 20))
        self.button_42.SetMinSize((-1, 20))
        self.button_43.SetMinSize((-1, 20))
        self.button_44.SetMinSize((-1, 20))
        self.button_45.SetMinSize((-1, 20))
        self.button_46.SetMinSize((-1, 20))
        self.button_47.SetMinSize((-1, 20))
        self.button_48.SetMinSize((-1, 20))
        self.button_49.SetMinSize((-1, 20))
        self.button_50.SetMinSize((-1, 20))
        self.grid_csv.CreateGrid(50, 9)
        self.grid_csv.SetRowLabelSize(25)
        self.grid_csv.SetColLabelSize(21)
        self.pnlGrid.SetMinSize((-1, 1055))
        self.pnlGrid.SetScrollRate(10, 20)
        self.btnTransmitHex.SetMinSize((100, -1))
        self.pnlTransmitHex.SetMinSize((-1, 69))
        self.window_1_pane_2.SetMinSize((1006, 640))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MyFrame.__do_layout
        sizer_1 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_7 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_9 = wx.BoxSizer(wx.VERTICAL)
        sizer_14 = wx.BoxSizer(wx.VERTICAL)
        sizer_15 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_11 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_12 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_13 = wx.BoxSizer(wx.VERTICAL)
        sizer_8 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_2 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_3 = wx.BoxSizer(wx.VERTICAL)
        self.sizer_6_staticbox.Lower()
        sizer_6 = wx.StaticBoxSizer(self.sizer_6_staticbox, wx.HORIZONTAL)
        grid_sizer_1 = wx.GridSizer(6, 2, 0, 0)
        sizer_4 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_4.Add(self.btnHideBar, 1, wx.ALL | wx.EXPAND, 1)
        sizer_4.Add(self.btnEnumPorts, 1, wx.ALL | wx.EXPAND, 1)
        sizer_3.Add(sizer_4, 0, wx.EXPAND, 0)
        grid_sizer_1.Add(self.label_1, 0, wx.ALL, 1)
        grid_sizer_1.Add(self.cmbPort, 0, wx.ALL | wx.EXPAND, 1)
        grid_sizer_1.Add(self.label_2, 0, wx.ALL, 1)
        grid_sizer_1.Add(self.cmbBaudRate, 0, wx.ALL | wx.EXPAND, 1)
        grid_sizer_1.Add(self.label_3, 0, wx.ALL, 1)
        grid_sizer_1.Add(self.choiceDataBits, 0, wx.ALL | wx.EXPAND, 1)
        grid_sizer_1.Add(self.label_4, 0, wx.ALL, 1)
        grid_sizer_1.Add(self.choiceParity, 0, wx.ALL | wx.EXPAND, 1)
        grid_sizer_1.Add(self.label_5, 0, wx.ALL, 1)
        grid_sizer_1.Add(self.choiceStopBits, 0, wx.ALL | wx.EXPAND, 1)
        sizer_3.Add(grid_sizer_1, 0, wx.ALL | wx.EXPAND, 1)
        sizer_6.Add(self.chkboxrtscts, 1, wx.ALL | wx.EXPAND, 1)
        sizer_6.Add(self.chkboxxonxoff, 1, wx.ALL | wx.EXPAND, 1)
        sizer_3.Add(sizer_6, 0, wx.LEFT | wx.RIGHT | wx.EXPAND, 2)
        sizer_3.Add(self.btnOpen, 0, wx.ALL | wx.EXPAND, 5)
        sizer_3.Add(self.btnClear, 0, wx.ALL | wx.EXPAND, 5)
        self.pnlSettingBar.SetSizer(sizer_3)
        sizer_2.Add(self.pnlSettingBar, 1, wx.EXPAND, 0)
        self.window_1_pane_1.SetSizer(sizer_2)
        sizer_8.Add(self.txtctlMain, 1, wx.EXPAND, 0)
        self.window_2_pane_1.SetSizer(sizer_8)
        sizer_13.Add((20, 20), 0, 0, 0)
        sizer_13.Add(self.button_1, 0, 0, 0)
        sizer_13.Add(self.button_2, 0, 0, 0)
        sizer_13.Add(self.button_3, 0, 0, 0)
        sizer_13.Add(self.button_4, 0, 0, 0)
        sizer_13.Add(self.button_5, 0, 0, 0)
        sizer_13.Add(self.button_6, 0, 0, 0)
        sizer_13.Add(self.button_7, 0, 0, 0)
        sizer_13.Add(self.button_8, 0, 0, 0)
        sizer_13.Add(self.button_9, 0, 0, 0)
        sizer_13.Add(self.button_10, 0, 0, 0)
        sizer_13.Add(self.button_11, 0, 0, 0)
        sizer_13.Add(self.button_12, 0, 0, 0)
        sizer_13.Add(self.button_13, 0, 0, 0)
        sizer_13.Add(self.button_14, 0, 0, 0)
        sizer_13.Add(self.button_15, 0, 0, 0)
        sizer_13.Add(self.button_16, 0, 0, 0)
        sizer_13.Add(self.button_17, 0, 0, 0)
        sizer_13.Add(self.button_18, 0, 0, 0)
        sizer_13.Add(self.button_19, 0, 0, 0)
        sizer_13.Add(self.button_20, 0, 0, 0)
        sizer_13.Add(self.button_21, 0, 0, 0)
        sizer_13.Add(self.button_22, 0, 0, 0)
        sizer_13.Add(self.button_23, 0, 0, 0)
        sizer_13.Add(self.button_24, 0, 0, 0)
        sizer_13.Add(self.button_25, 0, 0, 0)
        sizer_13.Add(self.button_26, 0, 0, 0)
        sizer_13.Add(self.button_27, 0, 0, 0)
        sizer_13.Add(self.button_28, 0, 0, 0)
        sizer_13.Add(self.button_29, 0, 0, 0)
        sizer_13.Add(self.button_30, 0, 0, 0)
        sizer_13.Add(self.button_31, 0, 0, 0)
        sizer_13.Add(self.button_32, 0, 0, 0)
        sizer_13.Add(self.button_33, 0, 0, 0)
        sizer_13.Add(self.button_34, 0, 0, 0)
        sizer_13.Add(self.button_35, 0, 0, 0)
        sizer_13.Add(self.button_36, 0, 0, 0)
        sizer_13.Add(self.button_37, 0, 0, 0)
        sizer_13.Add(self.button_38, 0, 0, 0)
        sizer_13.Add(self.button_39, 0, 0, 0)
        sizer_13.Add(self.button_40, 0, 0, 0)
        sizer_13.Add(self.button_41, 0, 0, 0)
        sizer_13.Add(self.button_42, 0, 0, 0)
        sizer_13.Add(self.button_43, 0, 0, 0)
        sizer_13.Add(self.button_44, 0, 0, 0)
        sizer_13.Add(self.button_45, 0, 0, 0)
        sizer_13.Add(self.button_46, 0, 0, 0)
        sizer_13.Add(self.button_47, 0, 0, 0)
        sizer_13.Add(self.button_48, 0, 0, 0)
        sizer_13.Add(self.button_49, 0, 0, 0)
        sizer_13.Add(self.button_50, 0, 0, 0)
        sizer_13.Add((20, 30), 0, 0, 0)
        sizer_11.Add(sizer_13, 0, wx.EXPAND, 0)
        sizer_12.Add(self.grid_csv, 1, wx.EXPAND, 0)
        sizer_11.Add(sizer_12, 1, wx.EXPAND, 0)
        self.pnlGrid.SetSizer(sizer_11)
        sizer_9.Add(self.pnlGrid, 1, wx.EXPAND, 0)
        sizer_15.Add(self.label_6, 0, wx.LEFT | wx.ALIGN_CENTER_VERTICAL, 7)
        sizer_15.Add((50, 20), 1, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_15.Add(self.btnTransmitHex, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_15.Add((15, 20), 0, 0, 0)
        sizer_14.Add(sizer_15, 0, wx.EXPAND, 0)
        sizer_14.Add(self.txtTransmitHex, 1, wx.EXPAND, 0)
        self.pnlTransmitHex.SetSizer(sizer_14)
        sizer_9.Add(self.pnlTransmitHex, 0, wx.EXPAND, 0)
        self.window_2_pane_2.SetSizer(sizer_9)
        self.SplitterWindow2.SplitVertically(self.window_2_pane_1, self.window_2_pane_2, 450)
        sizer_7.Add(self.SplitterWindow2, 1, wx.EXPAND, 0)
        self.window_1_pane_2.SetSizer(sizer_7)
        self.SplitterWindow.SplitVertically(self.window_1_pane_1, self.window_1_pane_2, 271)
        sizer_1.Add(self.SplitterWindow, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        self.Layout()
        self.Centre()
        # end wxGlade

# end of class MyFrame
class MyApp(wx.App):
    def OnInit(self):
        wx.InitAllImageHandlers()
        mainFrame = MyFrame(None, wx.ID_ANY, "")
        self.SetTopWindow(mainFrame)
        mainFrame.Show()
        return 1

# end of class MyApp

if __name__ == "__main__":
    app = MyApp(0)
    app.MainLoop()