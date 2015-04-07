##------------------------------------------------------------------------------------------------------##
## Importent note: ##
## This uses the program http://docs.livestreamer.io/index.html which provides the livestreamer command ##
## This python program is used to open streams in vlc media player ##
##------------------------------------------------------------------------------------------------------##

#Loading modules the script relies on
import time
import os
from urllib.request import urlopen
from urllib.error import URLError
import json

#Sets up the input variables that is used later in the script
option = ''
service = ''
stream = ''
streaming = ''
	
#Variables used to condense code down slightly
lsTwitch = 'livestreamer twitch.tv/'
lsYoutube = 'livestreamer youtube.com/watch?v='
	
#Sets the inital value for the timer variable so calculatins are correct
times = 0
timem = 0
timeh =0
	
#Opens the json file for the list of tracked streamers
with open('list.json') as data_file:    
    data = json.load(data_file)
	
#Displays avaliable options
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
	
#Option input
option = input('What do you want to do?: ')
	
#Defines the program to check a users status
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

#Defines the program to display the output from the check user as text
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
	
#Individual user status check
if option == 'check':
	print('')
	user = input('User to check status of: ')	
	print('')
	list(user)
	print('')
	pass
	
#User status list from the list.json file
if option == 'list':
	print('')
	for i in range(len(data["streams"])):
		datanum = i
		pass

	datanum = datanum + 1
	datanum = str(datanum)

	print('There are ' + datanum + ' streams on being tracked.')

	for i in range(len(data["streams"])):
		list(data["streams"][i])
		pass
	pass

#Command to open a stream
if option == 'open':
	service = input('What stream service? (Youtube or Twitch): ')
	stream = input('What stream?:')
	pass

#Process to use for twitch streams
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

#Process for youtube streams
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
	
#Starts timer and opens stream
start = time.time()
os.system(streaming)
end = time.time()
times = end - start
times = int(times)
	
#Timer calculation
while times > 59:
	times = times - 60
	timem = timem + 1
	pass

while timem > 59:
	timem = timem - 60
	timeh = timeh + 1
	pass
	
#converts timer values to strings to display with print
times = str(times)
timem = str(timem)
timeh = str(timeh)
	
#Displays timer
print('')
print ('Time elapsed: ' + timeh + ":" + timem + ":" + times)
print('')
pass


#Script end confirmation
input("Press Enter to continue...")
	
##End##
	