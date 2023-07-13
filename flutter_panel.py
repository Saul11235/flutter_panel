# Flutter panel an simple app for flutter development
# writed by: Edwin Saul PM 
# my site: www.edwinsaul.com 

try:   from  flutter_panel_gui import window_panel 
except:from .flutter_panel_gui import window_panel 

try:   from  flutter_panel_vars import panel_vars
except:from .flutter_panel_vars import panel_vars

try:   from  flutter_panel_actions import panel_actions
except:from .flutter_panel_actions import panel_actions


print("""\n
   +--------------------------------------------+ 
   | Welcome to flutter panel! :)               |
   | writed by Saul11235   www.edwinsaul.com    |
   | https://github.com/Saul11235/flutter_panel |
   | (Use the GUI, this is for monitoring only) |
   +--------------------------------------------+\n\n""") 

from os import getcwd,path

work_path  =  getcwd()
panel_path =  path.dirname(path.abspath(__file__))

print(work_path)
print(panel_path)

window=window_panel()
window.mainloop()
