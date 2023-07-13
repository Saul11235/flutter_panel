# setup debug panel
import tkinter as tk
from tkinter import ttk

def build_config_panel(self):
    notebook=self.get_obj_Notebook()

    #-- New Panel ----
    panel=ttk.Frame(notebook)
    notebook.add(panel, text=" Config  ")
    







