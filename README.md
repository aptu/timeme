# timeme
Activity time tracker

To run from the command line: $ python3 main.py

Script ui2py.sh converts .ui files into .py files.
Run from command line ./ui2py.sh before running main.py.
Check if ui2py is executable; if not, do chmod +x.

The window containing buttons Work Relax Pause ... appears.

The first run of the program creates a database containing stats for Work and relax time by day.


Project structure:
- Main.py defines the functionality of the application
- Main_windowui.py sets buttons of the ui interface 
- Timeui.py contains window and button settings of the main ui widget
- Statsui.py contains ui settings for '...' button
- Timetracker.py creates a database and contains functions for retrieving information




