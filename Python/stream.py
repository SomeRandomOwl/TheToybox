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
lsTwitch = 'livestreamer twitch.tv/'
lsYoutube = 'livestreamer youtube.com/watch?v='
times = 0
timem = 0
timeh =0

with open('list.json') as data_file:    
    data = json.load(data_file)

options = """

Avalible options:

----------

check (checks status of a specific user
list (Checks the status of a list of predefined users
open (opens a stream)

----------

"""

listing = """

-------------

"""

print(options)

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
	   		print(listing)
	   		print(urc + ' Is ONLINE')
	   		print(listing)
	   	elif check_user(urc) == 1:
	   		print(listing)
	   		print(urc + ' Is offline')
	   		print(listing)
	   	elif check_user(urc) == 2:
	   		print(listing)
	   		print(urc + ' Is not found')
	   		print(listing)
	   	elif check_user(urc) == 3:
	   		print(listing)
	   		print('Error in checking status')
	   		print(listing)
	   		pass
	except KeyboardInterrupt:
	   	pass
	return 

if option == 'check':

	print('')
	user = input('User to check status of: ')	
	print('')
	list(user)
	print('')
	whatDo = input('End script?: ')

	if whatDo == 'no':
		option = 'open'
	else:
		exit()
		pass
	pass

if option == 'list':
	
	print('')
	for i in range(len(data["streams"])):
		datanum = i
		pass

	datanum = datanum + 1
	datanum = str(datanum)

	print('There are ' + datanum + ' on record')

	for i in range(len(data["streams"])):
		list(data["streams"][i])
		pass

	whatDo = input('End script?: ')

	if whatDo == 'no':
		option = 'open'
	else:
		exit()
		pass
	pass

if option == 'open':
	service = input('What stream service? (Youtube or Twitch): ')
	stream = input('What stream?:')
	pass

if service == 'twitch':
	if stream == 'monstercat':
		audio = input('Do you want to do audio only?: ')
		if audio == 'yes':
			streaming = lsTwitch + stream + ' audio'
		else:
			streaming = lsTwitch + stream + ' source'
			pass
	else:
		streaming = lsTwitch + stream + ' source'
		pass
	pass

if service == 'youtube':
	if stream[1:32] == 'https://www.youtube.com/watch?v=':
		audio = input('Do you want to do audio only?: ')
		if audio == 'yes':
			streaming = lsYoutube + stream[32:] + ' audio_mp4'
		else:
			streaming = lsYoutube + stream[32:] + ' best'
			pass
	else:
		audio = input('Do you want to do audio only?: ')
		if audio == 'yes':
			streaming = lsYoutube + stream + ' audio_mp4'
		else:
			streaming = lsYoutube + stream + ' best'
			pass
	pass

print('')

start = time.time()
os.system(streaming)
end = time.time()
times = end - start
times = int(times)

while times > 59:
	times = times - 60
	timem = timem + 1
	pass

while timem > 59:
	timem = timem - 60
	timeh = timeh + 1
	pass

times = str(times)
timem = str(timem)
timeh = str(timeh)
print('')
print ('Time elapsed: ' + timeh + ":" + timem + ":" + times)
print('')

time.sleep(1)
input("Press Enter to continue...")
