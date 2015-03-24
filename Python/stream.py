# Importent note:
# This uses the program http://docs.livestreamer.io/index.html which provides the livestreamer command
# This python program is used to open twitch streams in vlc media player
import time
import os
service = ''
stream = ''
streaming = ''
service = input('What stream service?: ')
stream = input('What stream?:')
if service == 'twitch':
	streaming = 'livestreamer twitch.tv/' + stream + ' source'
	pass
if service == 'youtube':
	if stream[1:32] == 'https://www.youtube.com/watch?v=':
		streaming = 'livestreamer youtube.com/watch?v=' + stream[32:] + ' best --player-no-close'
	else:
		streaming = 'livestreamer youtube.com/watch?v=' + stream + ' best --player-no-close'
	pass
os.system(streaming)
time.sleep(1)
input("Press Enter to continue...")
