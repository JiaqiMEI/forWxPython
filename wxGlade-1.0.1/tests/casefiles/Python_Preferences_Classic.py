# -*- coding: ISO-8859-15 -*-
#
# generated by wxGlade 0.9.9pre on Sun Feb 23 19:04:05 2020
#

import wx

# begin wxGlade: dependencies
import gettext
# end wxGlade

# begin wxGlade: extracode
# Python specific extra code, non-python code will fail!
import config
import os

_icon_path = os.path.join(config.icons_path, 'icon.png')
# end wxGlade


class wxGladePreferencesUI(wx.Dialog):
    def __init__(self, *args, **kwds):
        # begin wxGlade: wxGladePreferencesUI.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_DIALOG_STYLE
        wx.Dialog.__init__(self, *args, **kwds)
        self.SetTitle(_("wxGlade: preferences"))
        _icon = wx.NullIcon
        _icon.CopyFromBitmap(wx.Bitmap(_icon_path, wx.BITMAP_TYPE_ANY))
        self.SetIcon(_icon)

        sizer_1 = wx.BoxSizer(wx.VERTICAL)

        self.notebook_1 = wx.Notebook(self, wx.ID_ANY, style=0)
        sizer_1.Add(self.notebook_1, 1, wx.ALL | wx.EXPAND, 5)

        self.notebook_1_pane_1 = wx.Panel(self.notebook_1, wx.ID_ANY)
        self.notebook_1.AddPage(self.notebook_1_pane_1, _("Interface"))

        sizer_3 = wx.BoxSizer(wx.VERTICAL)

        self.use_menu_icons = wx.CheckBox(self.notebook_1_pane_1, wx.ID_ANY, _("Use icons in menu items"))
        self.use_menu_icons.SetValue(1)
        sizer_3.Add(self.use_menu_icons, 0, wx.ALL | wx.EXPAND, 5)

        self.frame_tool_win = wx.CheckBox(self.notebook_1_pane_1, wx.ID_ANY, _("Show properties and tree windows as small frames"))
        self.frame_tool_win.SetValue(1)
        sizer_3.Add(self.frame_tool_win, 0, wx.ALL | wx.EXPAND, 5)

        self.show_progress = wx.CheckBox(self.notebook_1_pane_1, wx.ID_ANY, _("Show progress dialog when loading wxg files"))
        self.show_progress.SetValue(1)
        sizer_3.Add(self.show_progress, 0, wx.ALL | wx.EXPAND, 5)

        self.remember_geometry = wx.CheckBox(self.notebook_1_pane_1, wx.ID_ANY, _("Remember position and size of wxGlade windows"))
        self.remember_geometry.SetValue(1)
        sizer_3.Add(self.remember_geometry, 0, wx.ALL | wx.EXPAND, 5)

        self.show_sizer_handle = wx.CheckBox(self.notebook_1_pane_1, wx.ID_ANY, _("Show \"handles\" of sizers"))
        self.show_sizer_handle.SetValue(1)
        sizer_3.Add(self.show_sizer_handle, 0, wx.ALL | wx.EXPAND, 5)

        self.use_kde_dialogs = wx.CheckBox(self.notebook_1_pane_1, wx.ID_ANY, _("Use native file dialogs on KDE"))
        self.use_kde_dialogs.SetValue(1)
        sizer_3.Add(self.use_kde_dialogs, 0, wx.ALL | wx.EXPAND, 5)

        sizer_4 = wx.FlexGridSizer(4, 2, 0, 0)
        sizer_3.Add(sizer_4, 0, wx.EXPAND, 3)

        label_1 = wx.StaticText(self.notebook_1_pane_1, wx.ID_ANY, _("Initial path for \nfile opening/saving dialogs:"))
        sizer_4.Add(label_1, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.open_save_path = wx.TextCtrl(self.notebook_1_pane_1, wx.ID_ANY, "")
        self.open_save_path.SetMinSize((196, -1))
        sizer_4.Add(self.open_save_path, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        label_2_copy = wx.StaticText(self.notebook_1_pane_1, wx.ID_ANY, _("Initial path for \ncode generation file dialogs:"))
        sizer_4.Add(label_2_copy, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.codegen_path = wx.TextCtrl(self.notebook_1_pane_1, wx.ID_ANY, "")
        self.codegen_path.SetMinSize((196, -1))
        sizer_4.Add(self.codegen_path, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        label_2 = wx.StaticText(self.notebook_1_pane_1, wx.ID_ANY, _("Number of items in file history"))
        sizer_4.Add(label_2, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.number_history = wx.SpinCtrl(self.notebook_1_pane_1, wx.ID_ANY, "4", min=0, max=100, style=0)
        self.number_history.SetMinSize((196, -1))
        sizer_4.Add(self.number_history, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        label_2_copy_1 = wx.StaticText(self.notebook_1_pane_1, wx.ID_ANY, _("Number of buttons per row\nin the main palette"))
        sizer_4.Add(label_2_copy_1, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.buttons_per_row = wx.SpinCtrl(self.notebook_1_pane_1, wx.ID_ANY, "5", min=1, max=100, style=0)
        self.buttons_per_row.SetMinSize((196, -1))
        sizer_4.Add(self.buttons_per_row, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.notebook_1_pane_2 = wx.Panel(self.notebook_1, wx.ID_ANY)
        self.notebook_1.AddPage(self.notebook_1_pane_2, _("Other"))

        sizer_5 = wx.BoxSizer(wx.VERTICAL)

        self.use_dialog_units = wx.CheckBox(self.notebook_1_pane_2, wx.ID_ANY, _("Use dialog units by default for size properties"))
        sizer_5.Add(self.use_dialog_units, 0, wx.ALL | wx.EXPAND, 5)

        self.wxg_backup = wx.CheckBox(self.notebook_1_pane_2, wx.ID_ANY, _("Create backup wxg files"))
        self.wxg_backup.SetValue(1)
        sizer_5.Add(self.wxg_backup, 0, wx.ALL | wx.EXPAND, 5)

        self.codegen_backup = wx.CheckBox(self.notebook_1_pane_2, wx.ID_ANY, _("Create backup files for generated source"))
        self.codegen_backup.SetValue(1)
        sizer_5.Add(self.codegen_backup, 0, wx.ALL | wx.EXPAND, 5)

        self.allow_duplicate_names = wx.CheckBox(self.notebook_1_pane_2, wx.ID_ANY, _("Allow duplicate widget names"))
        self.allow_duplicate_names.Hide()
        sizer_5.Add(self.allow_duplicate_names, 0, wx.ALL | wx.EXPAND, 5)

        sizer_7 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_5.Add(sizer_7, 0, wx.EXPAND, 0)

        self.default_border = wx.CheckBox(self.notebook_1_pane_2, wx.ID_ANY, _("Default border width for widgets"))
        sizer_7.Add(self.default_border, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.default_border_size = wx.SpinCtrl(self.notebook_1_pane_2, wx.ID_ANY, "", min=0, max=20, style=0)
        self.default_border_size.SetMinSize((45, 22))
        sizer_7.Add(self.default_border_size, 0, wx.ALL, 5)

        sizer_7_copy = wx.BoxSizer(wx.HORIZONTAL)
        sizer_5.Add(sizer_7_copy, 0, wx.EXPAND, 0)

        self.autosave = wx.CheckBox(self.notebook_1_pane_2, wx.ID_ANY, _("Auto save wxg files every "))
        sizer_7_copy.Add(self.autosave, 0, wx.ALIGN_CENTER_VERTICAL | wx.BOTTOM | wx.LEFT | wx.TOP, 5)

        self.autosave_delay = wx.SpinCtrl(self.notebook_1_pane_2, wx.ID_ANY, "120", min=30, max=300, style=0)
        self.autosave_delay.SetMinSize((45, 22))
        sizer_7_copy.Add(self.autosave_delay, 0, wx.BOTTOM | wx.TOP, 5)

        label_3 = wx.StaticText(self.notebook_1_pane_2, wx.ID_ANY, _(" seconds"))
        sizer_7_copy.Add(label_3, 0, wx.ALIGN_CENTER_VERTICAL | wx.BOTTOM | wx.FIXED_MINSIZE | wx.TOP, 5)

        self.write_timestamp = wx.CheckBox(self.notebook_1_pane_2, wx.ID_ANY, _("Insert timestamp on generated source files"))
        self.write_timestamp.SetValue(1)
        sizer_5.Add(self.write_timestamp, 0, wx.ALL | wx.EXPAND, 5)

        self.write_generated_from = wx.CheckBox(self.notebook_1_pane_2, wx.ID_ANY, _("Insert .wxg file name on generated source files"))
        sizer_5.Add(self.write_generated_from, 0, wx.ALL | wx.EXPAND, 5)

        self.backup_suffix = wx.RadioBox(self.notebook_1_pane_2, wx.ID_ANY, _("Backup options"), choices=[_("append ~ to filename"), _("append .bak to filename")], majorDimension=2, style=wx.RA_SPECIFY_COLS)
        self.backup_suffix.SetSelection(0)
        sizer_5.Add(self.backup_suffix, 0, wx.ALL | wx.EXPAND, 5)

        sizer_6 = wx.StaticBoxSizer(wx.StaticBox(self.notebook_1_pane_2, wx.ID_ANY, _("Local widget path")), wx.HORIZONTAL)
        sizer_5.Add(sizer_6, 0, wx.ALL | wx.EXPAND, 5)

        self.local_widget_path = wx.TextCtrl(self.notebook_1_pane_2, wx.ID_ANY, "")
        sizer_6.Add(self.local_widget_path, 1, wx.ALL, 3)

        self.choose_widget_path = wx.Button(self.notebook_1_pane_2, wx.ID_ANY, _("..."), style=wx.BU_EXACTFIT)
        sizer_6.Add(self.choose_widget_path, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 3)

        sizer_2 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_1.Add(sizer_2, 0, wx.ALIGN_RIGHT | wx.ALL, 10)

        self.ok = wx.Button(self, wx.ID_OK, "")
        self.ok.SetDefault()
        sizer_2.Add(self.ok, 0, 0, 0)

        self.cancel = wx.Button(self, wx.ID_CANCEL, "")
        sizer_2.Add(self.cancel, 0, wx.LEFT, 10)

        self.notebook_1_pane_2.SetSizer(sizer_5)

        sizer_4.AddGrowableCol(1)

        self.notebook_1_pane_1.SetSizer(sizer_3)

        self.SetSizer(sizer_1)
        sizer_1.Fit(self)

        self.SetAffirmativeId(self.ok.GetId())
        self.SetEscapeId(self.cancel.GetId())

        self.Layout()
        self.Centre()
        # end wxGlade

# end of class wxGladePreferencesUI
