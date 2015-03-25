# Importent note:
# This uses the program http://docs.livestreamer.io/index.html which provides the livestreamer command
# This python program is used to open streams in vlc media player

import time
import os
from urllib.request import urlopen
from urllib.error import URLError
import json

option = ''
service = ''
stream = ''
streaming = ''
lsTwitch = 'E:\Stuff\livestreamer-v1.12.1\livestreamer twitch.tv/'
lsYoutube = 'E:\Stuff\livestreamer-v1.12.1\livestreamer youtube.com/watch?v='
lsConfig =  '-p=E:\PortableApps\VLCPortable'
times = 0
timem = 0
timeh =0

print(' \nAvalible options:\n \n----------\n \ncheck (checks status of a specific user\nlist (Checks the status of a list of predefined users\nopen (opens a stream)\n \n----------\n \n')

def script_end():
	print('')
	whatDo = input('End script?: ')

	if whatDo == 'no':
		option = 'open'
	else:
		exit()
		pass
	return

option = input('What do you want to do?: ')
def check_user(user):
    """ returns 0: online, 1: offline, 2: not found, 3: error """
    url = 'https://api.twitch.tv/kraken/streams/' + user
    try:
        info = json.loads(urlopen(url, timeout = 15).read().decode('utf-8'))
        if info['stream'] == None:
            status = 1
        else:
            status = 0
    except URLError as e:
        if e.reason == 'Not Found' or e.reason == 'Unprocessable Entity':
            status = 2
        else:
            status = 3
    return status

def list(urc):
	try:
	   	if check_user(urc) == 0:
	   		print('')
	   		print('-------------')
	   		print('')
	   		print(urc + ' Is ONLINE')
	   		print('')
	   		print('-------------')
	   	elif check_user(urc) == 1:
	   		print('')
	   		print('-------------')
	   		print('')
	   		print(urc + ' Is offline')
	   		print('')
	   		print('-------------')
	   	elif check_user(urc) == 2:
	   		print('')
	   		print('-------------')
	   		print('')
	   		print(urc + ' Is not found')
	   		print('')
	   		print('-------------')
	   	elif check_user(urc) == 3:
	   		print('')
	   		print('-------------')
	   		print('')
	   		print('Error in checking status')
	   		print('')
	   		print('-------------')
	   		pass
	except KeyboardInterrupt:
	   	pass
	return 

if option == 'check':
	print('')
	user = input('Who?: ')	
	print('')
	list(user)
	script_end()
	pass

if option == 'list':
	list('Totalbiscuit')
	list('Monstercat')
	list('TrionWorlds')
	list('Argodaemon')
	list('Nerdcubed')
	list('Mattophobia')
	list('Muselk')
	list('Scykoh')
	list('NaturalSelection2')
	list('GopherGaming')
	list('Haxmega')
	script_end()	
	pass

if option == 'open':
	service = input('What stream service?: ')
	stream = input('What stream?:')
	pass

if service == 'twitch':
	if stream == 'monstercat':
		audio = input('Do you want to do audio only?: ')
		if audio == 'yes':
			streaming = lsTwitch + stream + ' audio' + lsConfig
		else:
			streaming = lsTwitch + stream + ' source' + lsConfig
			pass
	else:
		streaming = lsTwitch + stream + ' source' + lsConfig
		pass
	pass

if service == 'youtube':
	if stream[1:32] == 'https://www.youtube.com/watch?v=':
		streaming = lsYoutube + stream[32:] + ' best' + lsConfig
	else:
		streaming = lsYoutube + stream + ' best' + lsConfig
	pass

print('')

start = time.time()
os.system(streaming)
end = time.time()
times = end - start
times = int(times)

if times > 60:
	while times > 60:
		times = times - 60
		timem = timem + 1
		pass
	pass

if timem > 60:
	while timem > 60:
		timem = timem - 60
		timhh = timeh + 1
		pass

times = str(times)
timem = str(timem)
timeh = str(timeh)
print('')
print ('Time elapsed: ' + timeh + ":" + timem + ":" + times)
print('')

time.sleep(1)
input("Press Enter to continue...")
