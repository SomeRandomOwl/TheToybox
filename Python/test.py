from tkinter import *
from tkinter import ttk


root = Tk()
root.title("Feet to feet")
def calculate():
	pass
mainframe = ttk.Frame(root, padding="12 12 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

feet = StringVar()
meters = StringVar()


ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))
ttk.Button(mainframe, text="button", command=calculate).grid(column=4, row=3, sticky=W)
ttk.Button(mainframe, text="button", command=calculate).grid(column=3, row=3, sticky=W)
ttk.Button(mainframe, text="button", command=calculate).grid(column=2, row=3, sticky=W)

ttk.Label(mainframe, text="""
	
Avalible options:
	
----------
	
Check (checks status of a specific user
List (Checks the status of a list of predefined users
Open (opens a stream)
Add (Adds a user to to the tracked user list)
Stats (Views the list of tracked stats)
	
----------
	
""").grid(column=1, row=1, sticky=W)
#ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="Things!").grid(column=1, row=1, sticky=E)
ttk.Label(mainframe, text="Yey Tests!").grid(column=1, row=2, sticky=W)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

#feet_entry.focus()
root.bind('<Return>', calculate)

root.mainloop()