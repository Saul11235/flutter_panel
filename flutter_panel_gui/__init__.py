import tkinter as tk
from tkinter import ttk

try:     from  panel_debug import build_debug_panel
except:  from .panel_debug import build_debug_panel

try:     from  panel_config import build_config_panel
except:  from .panel_config import build_config_panel

class window_panel:

    def __init__(self):
        self.window=tk.Tk()
        self.notebook=ttk.Notebook(self.window)
        self.build_aplication()
        self.objectPanel=None
        self.path_panel=""
        self.path_work=""

    def get_obj_Notebook(self):
        return self.notebook
        
    def config_object(self,objectPanel):
        self.objectPanel=objectPanel

    def build_aplication(self):
        self.window.title("flutter panel")
        self.window.resizable(False,False)
        self.window.geometry("600x400")
        build_debug_panel(self)
        build_config_panel(self)
        self.notebook.pack(expand=1,fill="both",padx=4,pady=4)

    def mainloop(self):
        self.window.mainloop()

#----------------------------

if __name__=="__main__":
    print("flutter panel window test")
    a=window_panel()
    a.mainloop()
