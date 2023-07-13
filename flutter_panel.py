# Flutter panel an simple app for flutter development
# writed by: Edwin Saul PM 
# my site: www.edwinsaul.com 

try:   from  gui_flutter_panel import window_panel 
except:from .gui_flutter_panel import window_panel 

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
