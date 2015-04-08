##------------------------------------------------------------------------------------------------------##
## Importent note:                                                                                      ##
## This uses the program http://docs.livestreamer.io/index.html which provides the livestreamer command ##
## This python program is used to open streams in vlc media player                                      ##
##------------------------------------------------------------------------------------------------------##

#Loading modules the script relies on
import time
import os
from urllib.request import urlopen
from urllib.error import URLError
import json

os.system('cls')

#Sets up the input variables that is used later in the script

option = ''
service = ''
lvst = ''
wincmd = ''
audio = ''
restart = 'yes'
lvsting = ''
totalsec = 0
totalmin = 0
totalhrs = 0
totaldays = 0
totalusersec = 0
totalusermin = 0
totaluserhrs = 0
totaluserdays = 0

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
    data_file.close()
    pass

streamDataTemp = data['data']['streamData']['streamTemplate']
#Displays avaliable options
options = """
	
Avalible options:
	
----------
	
check (checks status of a specific user
list (Checks the status of a list of predefined users
open (opens a stream)
Add (Adds a user to to the tracked user list)
	
----------
	
"""
optionsstreaming = """
	
Avalible options:
	
----------
	
The stream you chose is opening
So sit back and watch/listen to you stream
Enjoy!
	
----------
	
"""
optionsopen = """
	
Avalible options:
	
----------

This is to open stream service The only two options avaliable are:	
Youtube -- Allows you to open a stream with a youtube url ir video id
Twitch -- Opens a twitch stream when you input user
	
----------
	
"""
optionsstream = """
	
Avalible options:
	
----------

This is to specify a stream
Input a username if for Twitch
Input a video id if for Youtube
	
----------
	
"""
optionsopenaudio = """
	
Avalible options:
	
----------
	
This is if you want to listen to the audio only for the stream
Input yes to only get the audio and no video
Input no to have video as well as audio
	
----------
	
"""
optionslist = """
	
Avalible options:
	
----------
	
This is used to list users present in the list.json
This only works for twitch streamers at the moment
Will maybe extend to youtube in the future
	
----------
	
"""
optionscheck = """
	
Avalible options:
	
----------
	
This is used to check the status of a individual twitch streamer
This is unavaliable for youtube unless it is otherwisse possible
Might have youtube support in the future
	
----------
	
"""
optionsadd = """
	
Avalible options:
	
----------
	
This is used to add a user to the tracked list
This make ther status to be checked with the list command
It also allows statistic tracking for the user
	
----------
	
"""
listing = """
-------------
"""
	
	
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
def userAdd():
	global streamDataTemp
	global data

	goodRecord = 0
	emptyRecord = 0
	allRecords = 0

	for i in range(len(data["streams"])):
		if data['streams'][i] != "null":
			goodRecord = goodRecord + 1
		elif data['streams'][i] == "null":
			emptyRecord = emptyRecord + 1
			pass
		allRecords = allRecords + 1
		pass

	goodRecord = str(goodRecord)
	emptyRecord = str(emptyRecord)
	allRecords = str(allRecords)

	os.system('cls')
	print(optionsadd)
	print('\nThere are ' + goodRecord + ' used records and  ' + emptyRecord + ' empty records out of ' + allRecords + '\n')
	userAdd = input('Name of the user to add?: ')
	nextRecord = data['data']['nextRecord']
	data['streams'][nextRecord] = userAdd
	data['data']['streamData'][userAdd.lower()] = streamDataTemp
	nextRecord = nextRecord + 1
	data['data']['nextRecord'] = nextRecord
	isMusicStream = input('Is this streama music stream? (Yes or No): ')
	if isMusicStream.lower() == 'yes':
		data['data']['streamData'][userAdd]['musicStream'] = true
		pass

	for i in range(len(data["streams"])):
		if data['streams'][i] != "null":
			datanum = i
		pass

	datanum = datanum + 1
	data['data']['streamNum'] = datanum

	pass
#Individual user status check
def check():
	os.system('cls')
	print(optionscheck)
	user = input('User to check status of: ')	
	print('')
	list(user)
	print('')
	pass
	
#User status list from the list.json file
def lvstList():
	global data
	global datanum
	global data_file

	os.system('cls')
	print(optionslist)
	for i in range(len(data["streams"])):
		if data['streams'][i] != "null":
			datanum = i
		pass

	datanum = datanum + 1
	datanum = str(datanum)
	data['data']['streamNum'] = int(datanum)
	print('There are ' + datanum + ' streams on being tracked.\n\nDisplaying Online Users')

	for i in range(len(data["streams"])):
		if data["streams"][i] != "null":
			if check_user(data["streams"][i]) != 1:
				list(data["streams"][i])
				pass
			pass
		pass
	pass

#Command to open a stream
def openstream():
	global service
	global lvst
	global lsTwitch
	global lvsting
	global lsYoutube
	global audio
	global options

	os.system('cls')
	print(optionsopen)
	service = input('What stream service? (Youtube or Twitch): ')
	os.system('cls')
	print(optionsstream)
	lvst = input('What stream?: ')
	#Process to use for twitch streams
	if service.lower() == 'twitch':
		try:
			audioOnly = data['data']['streamData'][lvst.lower()]['musicStream']
			if audioOnly == 'true':
				os.system('cls')
				print(optionsopenaudio)
				audio = input('Do you want to do audio only?: ')

				if audio.lower() == 'yes':
					lvsting = lsTwitch + lvst + ' audio'
				else:
					lvsting = lsTwitch + lvst + ' source'
					pass
				pass
			else:
				lvsting = lsTwitch + lvst + ' source'
				pass
			pass
		except:
			lvsting = lsTwitch + lvst + ' source'
			return

	
	#Process for youtube streams
	if service.lower() == 'youtube':
		os.system('cls')
		print(optionsopenaudio)
		if lvst[1:32] == 'https://www.youtube.com/watch?v=':
			audio = input('Do you want to do audio only?: ')
			if audio.lower() == 'yes':
				lvsting = lsYoutube + lvst[32:] + ' audio_mp4'
			else:
				lvsting = lsYoutube + lvst[32:] + ' best'
				pass
		else:
			audio = input('Do you want to do audio only?: ')
			if audio.lower() == 'yes':
				lvsting = lsYoutube + lvst + ' audio_mp4'
			else:
				lvsting = lsYoutube + lvst + ' best'
				pass
		pass
	pass
	
 #Starts timer and opens stream

def cmdwin():
	global times
	global lvsting
	global options

	os.system('cls')
	print(optionsstreaming)
	print('Opening ' + lvst + "'s stream on " + service + ".\n")
	print('Total times ' + lvst + " has been played: " + str(data['data']['streamData'][lvst]['playCount']) + ".\n")
	print('Total ammount of time ' + lvst + " Has been played for: " + data['data']['streamData'][lvst]['totalTime'] + " \n")
	start = time.time()
	os.system(lvsting)
	end = time.time()
	times = end - start
	times = int(times)
	pass
 
 #Timer calculation
def timeCalc():
	global times
	global timem
	global timeh

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
	#Prints the elapsed time
	elapsedTime = timeh + ':' + timem + ':' + times
	print('')
	print ('Time elapsed: ' + elapsedTime)
	print('')
	pass

#Updates Stats
def stattracker():
	global times
	global timem
	global timeh
	global lvst
	global elapsedTime
	global totalsec
	global totalmin
	global totalhrs
	global totaldays
	global totalusersec
	global totalusermin
	global totaluserhrs
	global totaluserdays
	global service

	#Updates the play count on the active streamer
	try:
		playnum = data['data']['streamData'][lvst]['playCount']
		playnum = playnum + 1
		data['data']['streamData'][lvst]['playCount'] = playnum
		pass
	except:
		pass

	#Updates the total play count for all streams
	totalplay = data['data']['totalPlay']
	totalplay = totalplay + 1
	data['data']['totalPlay'] = totalplay


	#Updates overall time totals
	totalsec = data['data']['secs']
	totalmin = data['data']['mins']
	totalhrs = data['data']['hours']
	totaldays = data['data']['days']

	times = int(times)
	timem = int(timem)
	timeh = int(timeh)

	totalsec = totalsec + times
	totalmin = totalmin + timem
	totalhrs = totalhrs + timeh

	while totalsec > 59:
		totalsec = totalsec - 60
		totalmin = totalmin + 1
		pass
	while totalmin > 59:
		totalmin = totalmin - 60
		totalhrs = totalhrs + 1
		pass
	while totalhrs > 23:
		totalhrs - 24
		totaldays + 1
		pass

	data['data']['secs'] = totalsec
	data['data']['mins'] = totalmin
	data['data']['hours'] = totalhrs
	data['data']['days'] = totaldays
	totalsec = str(totalsec)
	totalmin = str(totalmin)
	totalhrs = str(totalhrs)
	totaldays = str(totaldays)
	totalelapsed = totaldays + " Days " + totalhrs + ":" + totalmin + ":" + totalsec
	data['data']['totalTime'] = totalelapsed

	#Updates user time totals
	if service.lower() == 'twitch':
		try:
			totalusersec = data['data']['streamData'][lvst]['secs']
			totalusermin = data['data']['streamData'][lvst]['mins']
			totaluserhrs = data['data']['streamData'][lvst]['hours']
			totaluserdays = data['data']['streamData'][lvst]['days']
		
			totalusersec = totalusersec + times
			totalusermin = totalusermin + timem
			totaluserhrs = totaluserhrs + timeh

			while totalusersec > 59:
				totalusersec = totalusersec - 60
				totalusermin = totalusermin + 1
				pass
	
			while totalusermin > 59:
				totalusermin = totalusermin - 60
				totaluserhrs = totaluserhrs + 1
				pass

			while totaluserhrs > 23:
				totaluserhrs - 24
				totaluserdays + 1
				pass
		
			data['data']['streamData'][lvst]['secs'] = totalusersec
			data['data']['streamData'][lvst]['mins'] = totalusermin
			data['data']['streamData'][lvst]['hours'] = totaluserhrs
			data['data']['streamData'][lvst]['days'] = totaluserdays
			totalusersec = str(totalusersec)
			totalusermin = str(totalusermin)
			totaluserhrs = str(totaluserhrs)
			totaluserdays = str(totaluserdays)
			totaluserelapsed = totaluserdays + " Days " + totaluserhrs + ":" + totalusermin + ":" + totalusersec
			data['data']['streamData'][lvst]['totalTime'] = totaluserelapsed
		except:
			pass
	pass

#Main Starter
def start():
	global option
	global times
	global timem
	global restart
	global options
	global lvst

	#Option input
	print(options)
	option = input('What do you want to do?: ')
	os.system('cls')
	print(options)

	#checks what option was chosen
	if option.lower() == "check":
		check()
	elif option.lower() == "list":
		lvstList()
	elif option.lower() == "open":
		openstream()
		cmdwin()
		timeCalc()
		stattracker()
	elif option.lower() == "add":
		userAdd()
	else:
		print("""

-----------
Option Not Recgonized
-----------

""")
		pass
	print('')
	restart = input('Restart the Script?: ')
	pass

#Restarts the script
while restart == "yes":
	start()
	if restart == "yes":
		os.system('cls')
		pass
	pass



#Script end confirmation
print('')
input("Press Enter to continue...")

with open('list.json', "w") as write_file:  
	json.dump(data, write_file)

##End##