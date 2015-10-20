##########Notes Regarding what this code does##########
#This functions mainly to run a few console commands  #
#that helps increase the 'portability' of the atom    #
#text editor from http://atom.io It needs to run in   #
#instalation directory of atom and will help you keep #
#a local copy of your configuration files and         #
#installed packages, it uses xcopy to copy files      #
#from %HOMEPATH% to the instalation directory of atom #
#it is really ment for use with a flash drive         #
#######################################################

# Import Required Modules #
import os
from tkinter import *
from tkinter import ttk
# UI #
root = Tk()
root.title("Atom Portrable")
root.wm_iconbitmap(bitmap = "atom.ico")
# UI Mainframe #
mainframe = ttk.Frame(root, padding="5 5 5 5")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)
# Defining functions
def oscmd(cmd):
    os.system(cmd)
# Button Function to draw button #
def button(text, command, column, row):
    ttk.Button(mainframe, text=text, command=command).grid(column=column, row=row, sticky=W)
# label Function to draw label #
def label(text, column, row):
    ttk.Label(mainframe, text=text).grid(column=column, row=row)
# Adds configs from current dir #
def add():
    oscmd("rd /s /q C:%HOMEPATH%\.atom\* ")
    oscmd("xcopy .atom C:%HOMEPATH%\.atom\*  /E /Y")
# Removes configs from user dir #
def remove():
    oscmd("rd /s /q C:%HOMEPATH%\.atom ")
    print('Done removing configs from local machine')
# Starts Atom #
def start():
    oscmd("atom")
# Copies configs from user dir to local #
def copy():
    oscmd("xcopy C:%HOMEPATH%\.atom\config.cson .atom\config.cson  /E /Y")
    oscmd("xcopy C:%HOMEPATH%\.atom\storage .atom\storage  /E /Y")
# Copies packages directory from user dir to local #
def update():
    oscmd("xcopy C:%HOMEPATH%\.atom\packages .atom\packages  /E /Y")
# Copies configs from user dir to local #
def updateall():
    oscmd("xcopy C:%HOMEPATH%\.atom\* .atom\*  /E /Y")
# Starts Atom then removes configs when it closes #
def sar():
    oscmd("atom")
    oscmd("rd /s /q C:%HOMEPATH%\.atom ")
# Copy the configs to current directory then remove them from the local machine #
def car():
    oscmd("xcopy C:%HOMEPATH%\.atom\* .atom\*  /E /Y")
    oscmd("rd /s /q C:%HOMEPATH%\.atom ")
# Ui Buttons #
def ui():
    label("Avaliable options: ", 1, 1)
    button("Start Atom", start, 1, 3)
    button("Copy Configs", copy, 1, 4)
    button("Update Packages", update, 1, 5)
    button("Update Everything", updateall, 1, 6)
    button("Add copied Configs", add, 1, 7)
    button("Remove local configs from machine", remove, 1, 8)
    button("Start Atom, Then remove configs", sar, 1, 9)
    button("Copy Configs, then remove local copys", car, 1, 10)
ui()
for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)
root.mainloop()
