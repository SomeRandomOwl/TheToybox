# Importent note:
# This uses the program http://docs.livestreamer.io/index.html which provides the livestreamer command
# This python program is used to open twitch streams in vlc media player

import os
service = ''
stream = ''
streaming = ''
service = input('What stream service?: ')
stream = input('What stream?:')
streaming = 'livestreamer twitch.tv/' + stream + ' source'
os.system(streaming)
input("Press Enter to continue...")