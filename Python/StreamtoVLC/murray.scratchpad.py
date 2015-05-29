#def writeToData(location,val):
	#def i(loc):
		#if loc==[]:
			#return data
		#return i(loc[:-1])[loc[-1]]
	#i(location)=val
	##print i(location)
	#jsonWrite()

def pull_val_from_tree(key,tree):
	if key==[]:
		return tree
	return pull_val_from_tree(val[1:],tree[val[0]])

def writeToData(location,val,d='data',top=1):
	if location==[]:
		d=val
		return d
	else:
		if type(d)==type(''):
			globals()[d][location[0]]=writeToData(location[1:],val,globals()[d][location[0]],0)
		else:
			d[location[0]]=writeToData(location[1:],val,d[location[0]],0)
			return d
		if top:
			jsonWrite()

def jsonWrite():
	with open('list.json', "w") as write_file:
		write_file.write(json.dumps(data, sort_keys=True, indent=4, separators=(',', ': ')))




from tkinter import *
from tkinter import ttk

from tkinter import ttk.style

import platform

def main():

	class Example(Frame):

		def centerWindow(self,windowWidth,windoHeight):
			screenwidth = self.parent.winfo_screenwidth()
			screenheight = self.parent.winfo_screenheight()
			
			xpos = (screenwidth - windowWidth)/2
			ypos = (screenheight - windoHeight)/2
			self.parent.geometry('%dx%d+%d+%d' % (windowWidth, windoHeight, xpos, ypos))
		
		def populateUI(self):
			quitButton = Button(self, text="Quit",command=self.quit)
			quitButton.place(x=50, y=50)

		def initUI(self):
			self.centerWindow(290,150)
			self.parent.title("Simple")
			self.style = Style()
			self.style.theme_use("default")
			self.pack(fill=BOTH, expand=1)
			self.populateUI()

		def __init__(self, parent):
			Frame.__init__(self, parent, background="white")
			self.parent = parent
			self.initUI()

	root = Tk()
	app = Example(root)
	root.mainloop()

if __name__ == '__main__':
	main()
