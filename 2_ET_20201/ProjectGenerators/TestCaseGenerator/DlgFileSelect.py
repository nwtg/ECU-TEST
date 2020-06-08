# -*- coding: utf-8 -*-

import wx

LBL = 'File path to your excel file:'

class DlgFileSelect(wx.Dialog):

    def __init__(self, parent, aParamGenerator, workspacePath=None):
        wx.Dialog.__init__(self, parent, style=wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER,
                           title=aParamGenerator.GetName())

        self.theParamGenerator = aParamGenerator

        button_OK = wx.Button(self, label='OK')
        button_OK.SetToolTip('OK')
        button_OK.SetDefault()
        button_OK.Bind(wx.EVT_BUTTON, self.OnCmdOkButton)

        button_Cancel = wx.Button(self, label='Cancel')
        button_Cancel.SetToolTip('Cancel')
        button_Cancel.Bind(wx.EVT_BUTTON, self.OnCmdCancelButton)

        label = wx.StaticText(self, label=LBL)

        self.txtFileName = wx.TextCtrl(self, value=aParamGenerator.GetFilename())

        button_Browse = wx.Button(self, label='...')
        button_Browse.SetMinSize(wx.Size(23, 23))
        button_Browse.Bind(wx.EVT_BUTTON, self.OnCmdBrowseButton)

        sizerButtons = wx.BoxSizer(wx.HORIZONTAL)
        sizerButtons.Add(button_OK, 0, border=5, flag=wx.ALL)
        sizerButtons.Add(button_Cancel, 0, border=5, flag=wx.ALL)

        boxSizer = wx.BoxSizer(wx.HORIZONTAL)
        boxSizer.Add(self.txtFileName, 1, border=0, flag=0)
        boxSizer.AddSpacer(8)
        boxSizer.Add(button_Browse, 0, border=0, flag=0)

        ctrlSizer = wx.BoxSizer(wx.VERTICAL)
        ctrlSizer.Add(label, flag=wx.EXPAND)
        ctrlSizer.AddSpacer(8)
        ctrlSizer.Add(boxSizer, flag=wx.EXPAND)

        sizerMain = wx.BoxSizer(wx.VERTICAL)
        sizerMain.Add(ctrlSizer, 0, border=15, flag=wx.ALL | wx.EXPAND)
        sizerMain.AddStretchSpacer()
        sizerMain.Add(sizerButtons, 0, border=0, flag=wx.ALIGN_BOTTOM | wx.ALIGN_CENTER)

        self.SetSizer(sizerMain)

        self.SetClientSize(wx.Size(356, 125))

    def OnCmdCancelButton(self, event):
        # #Add your code here
        self.EndModal(wx.ID_CANCEL)

    def OnCmdOkButton(self, event):
        # #Add your code to update self.theParamGenerator here
        self.theParamGenerator.SetFilename(self.txtFileName.GetValue())
        self.EndModal(wx.ID_OK)

    def OnCmdBrowseButton(self, event):
        fileDlg = wx.FileDialog(parent=self,
                                style=wx.FD_OPEN,
                                message='Select an Excel file',
                                wildcard='File|*.*',
                                defaultDir=r'',
                                defaultFile='')

        if fileDlg.ShowModal() == wx.ID_OK:
            self.txtFileName.SetValue(fileDlg.GetPath())

        fileDlg.Destroy()
