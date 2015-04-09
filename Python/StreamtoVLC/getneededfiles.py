import  os
def dependGet():
	dependGetOption = input('Do you want to download the dependancies? (Yes or No): ')
	if dependGetOption == 'yes':
		os.system('start https://github.com/chrippa/livestreamer/releases/download/v1.12.1/livestreamer-v1.12.1-win32-setup.exe')
		pass
	pass
dependGet()