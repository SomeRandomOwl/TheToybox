##------------------------------------------------------------------------------------------------------##
## Importent note:                                                                                      ##
## This uses the program http://docs.livestreamer.io/index.html which provides the livestreamer command ##
## This python program is used to open streams in vlc media player                                      ##
##------------------------------------------------------------------------------------------------------##

##Start##

#Loading modules the script relies on
import time
import os
import platform
from urllib.request import urlopen
from urllib.error import URLError
import json
import sys
import traceback

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
statAdd = 'no'
statwho = ''
debglog = []
streamError = False
jsonTemplate =  {"data": {"errorLogs": {"timesInterrupted": 0, "unRecgonizedCmds": 0, "unknownError": 0, "unsupportedServices": 0}, "logs": {"streamNum": 0, "timesRestarted": 0, "timesStarted": 0, "totalPlay": 0}, "streamData": {"streamTemplate": {"days": 0, "hours": 0, "mins": 0, "musicStream": "true", "playCount": 0, "secs": 0, "totalTime": "0 Days 0:0:0"}}}, "streams": []}

def jsonCheck():
	test = os.path.isfile('list.json')
	if test == False:
		print('List.json Not Found, Creating...')
		fname = "list.json"
		with open(fname, 'w') as fout:
			fout.write(json.dumps(jsonTemplate, sort_keys=True, indent=4, separators=(',', ': ')))
			fout.close()
		
	elif test:
		print('List.json Found, Continueing...')
	

def clearscreen():
	if platform.system()=='Linux':
		os.system('clear')
	else:
		os.system('cls')
clearscreen()

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

def debug(info,error=0):
	global debglog
	if data['data']['errorLogs']['debug'] == 'True':
		if type(info)==type([]):
			for a in info:
				debug(a)
		else:
			import datetime
			if error:
				dbg="ERROR: "
			else:
				dbg="DEBUG: "
			print(datetime.datetime.now().strftime("[%Y-%m-%dT%T%z] ")+dbg +str(info))
			debglog.append(datetime.datetime.now().strftime("[%Y-%m-%dT%T%z] ")+dbg+str(info))
debug('--Start--')
streamDataTemp = data['data']['streamData']['streamTemplate']
startCount = data['data']['logs']['timesStarted']
startCount = startCount + 1
data['data']['logs']['timesStarted'] = startCount
debug('Start Count Added Onto')

#Menu Prompts
global options
options = ""																		+"\n"+\
			"Avalible options:"														+"\n"+\
			""																		+"\n"+\
			"----------"															+"\n"+\
			""																		+"\n"+\
			"Check (checks status of a specific user"								+"\n"+\
			"List (Checks the status of a list of predefined users"					+"\n"+\
			"Open (opens a stream)"													+"\n"+\
			"Add (Adds a user to to the tracked user list)"							+"\n"+\
			"Stats (Views the list of tracked stats)"								+"\n"+\
			""																		+"\n"+\
			"----------"															+"\n"+\
			""

global optionsstreaming
optionsstreaming = ""																+"\n"+\
			"Avalible options:"														+"\n"+\
			""																		+"\n"+\
			"----------"															+"\n"+\
			""																		+"\n"+\
			"The stream you chose is opening"										+"\n"+\
			"So sit back and watch/listen to you stream"							+"\n"+\
			"Enjoy!"																+"\n"+\
			""																		+"\n"+\
			"----------"															+"\n"+\
			""

global optionsopen
optionsopen = ""																	+"\n"+\
			"Avalible options:"														+"\n"+\
			""																		+"\n"+\
			"----------"															+"\n"+\
			""																		+"\n"+\
			"This is to open stream service The only two options avaliable are:"	+"\n"+\
			"Youtube -- Allows you to open a stream with a youtube url ir video id"	+"\n"+\
			"Twitch -- Opens a twitch stream when you input user"					+"\n"+\
			""																		+"\n"+\
			"----------"															+"\n"+\
			""	

global optionsstream
optionsstream = ""																	+"\n"+\
			"Avalible options:"														+"\n"+\
			""																		+"\n"+\
			"----------"															+"\n"+\
			""																		+"\n"+\
			"This is to specify a stream"											+"\n"+\
			"Input a username if for Twitch"										+"\n"+\
			"Input a video id if for Youtube"										+"\n"+\
			""																		+"\n"+\
			"----------"															+"\n"+\
			""

global optionsopenaudio
optionsopenaudio = ""																+"\n"+\
			"Avalible options:"														+"\n"+\
			""																		+"\n"+\
			"----------"															+"\n"+\
			""																		+"\n"+\
			"This is if you want to listen to the audio only for the stream"		+"\n"+\
			"Input yes to only get the audio and no video"							+"\n"+\
			"Input no to have video as well as audio"								+"\n"+\
			""																		+"\n"+\
			"----------"															+"\n"+\
			""

global optionslist
optionslist = ""																	+"\n"+\
			"Avalible options:"														+"\n"+\
			""																		+"\n"+\
			"----------"															+"\n"+\
			""																		+"\n"+\
			"This is used to list users present in the list.json"					+"\n"+\
			"This only works for twitch streamers at the moment"					+"\n"+\
			"Will maybe extend to youtube in the future"							+"\n"+\
			""																		+"\n"+\
			"----------"															+"\n"+\
			""

global optionscheck
optionscheck = ""																	+"\n"+\
			"Avalible options:"														+"\n"+\
			""																		+"\n"+\
			"----------"															+"\n"+\
			""																		+"\n"+\
			"This is used to check the status of a individual twitch streamer"		+"\n"+\
			"This is unavaliable for youtube unless it is otherwisse possible"		+"\n"+\
			"Might have youtube support in the future"								+"\n"+\
			""																		+"\n"+\
			"----------"															+"\n"+\
			""

global optionsstatscheck
optionsstatscheck = ""																+"\n"+\
			"Avalible options:"														+"\n"+\
			""																		+"\n"+\
			"----------"															+"\n"+\
			""																		+"\n"+\
			"This is used to view the stats being tracked"							+"\n"+\
			"You can view the stats of a individual user"							+"\n"+\
			"You can also view the total global stats"								+"\n"+\
			"You can also Clear the stats"											+"\n"+\
			"You can also check the errorLogs"										+"\n"+\
			""																		+"\n"+\
			"---------"																+"\n"+\
			""

global optionsstatsclear
optionsstatsclear = ""																+"\n"+\
			"Avalible options:"														+"\n"+\
			""																		+"\n"+\
			"----------"															+"\n"+\
			""																		+"\n"+\
			"This is the danger zone!"												+"\n"+\
			"This is where you can clear a users stats or the global stats"			+"\n"+\
			"Continue if you sure of what you are doing!"							+"\n"+\
			""																		+"\n"+\
			"----------"															+"\n"+\
			""	

global optionsadd
optionsadd = ""																		+"\n"+\
			"Avalible options:"														+"\n"+\
			""																		+"\n"+\
			"----------"															+"\n"+\
			""																		+"\n"+\
			"This is used to add a user to the tracked list"						+"\n"+\
			"This make ther status to be checked with the list command"				+"\n"+\
			"It also allows statistic tracking for the user"						+"\n"+\
			""																		+"\n"+\
			"----------"															+"\n"+\
			""	

global listing
listing = ""																		+"\n"+\
			"-------------"															+"\n"+\
			""

#Defines the program to check a users status
def check_user(user):
	debug('Retriveing User Status')
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
	debug('User Status Retrived')
	return status

#Defines the program to display the output from the check user as text
def list(urc):
	debug('Processing User Status')
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
	except KeyboardInterrupt:
		pass
	debug('User Status Processed')
	return 

#Function to add new tracked users
def userAdd():
	global streamDataTemp
	global data
	global statAdd
	global statwho

	allRecords = 0
	debug('User Add Started')
	if statAdd.lower() == 'yes':
		array = data['streams']
		array.append(statwho.lower())
		data['data']['streamData'][statwho.lower()] = streamDataTemp
		debug('Short User Add Done')
	debug('Counting Usernames')
	if statAdd.lower() != 'yes':
		for i in range(len(data["streams"])):
			allRecords = allRecords + 1
	debug('Usernames Counted')
	clearscreen()
	print(optionsadd)
	if allRecords == 1:
		print('\nThere is currently: ' + str(allRecords) + ' tracked user.' + '\n')
	elif allRecords == 0:
		print('\nThere is currently: ' + str(allRecords) + ' tracked users.' + '\n')
	elif allRecords >> 1:
		print('\nThere is currently: ' + str(allRecords) + ' tracked users.' + '\n')
	debug('Username Count Printed')
	userAdd = input('Name of the user to add?: ')
	if not userAdd:
		print('\nPlease type in a username and not leave the line blank.')
	else:
		array = data['streams']
		array.append(userAdd.lower())
		data['data']['streamData'][userAdd.lower()] = streamDataTemp
		debug('User added')
		isMusicStream = input('Is this stream a music stream? (Yes or No): ')
	
		if isMusicStream.lower() == 'yes':
			data['data']['streamData'][userAdd]['musicStream'] = 'true'
		for i in range(len(data["streams"])):
			datanum = i
		debug('User Music Status added')
		datanum = datanum + 1
		data['data']['logs']['streamNum'] = datanum
		debug('StreamNum Updated')
	
def statCheck():
	global data
	global statAdd
	global statwho

	debug('Stat Check Started')
	statAdd = 'no'
	clearscreen()
	print(optionsstatscheck)
	statWhat = input('Which stat do you want to see? (User, Global, Error or Clear): ')
	if statWhat.lower() == 'user':
		clearscreen()
		print(optionsstatscheck)
		statwho = input('Who do you want to check the stats of?: ')
		debug('Retriveing User Stats')
		try:
			print("\nThis stream has been played: " + str(data['data']['streamData'][statwho.lower()]['playCount']))
			print("\nThis stream has been played for a total of: " + data['data']['streamData'][statwho.lower()]['totalTime'])
			if data['data']['streamData'][statwho.lower()]['musicStream'] == 'true':
				print('\nThis stream is also marked as a music stream')
			debug('Done')
		except:
			clearscreen()
			print(optionsstatscheck)
			print('\nThere are no stats for this user!\n')
			debug('Done')
			statAdd = input('Whould you like to add this user to the tracked list?: ')
			if statAdd.lower() == 'yes':
				userAdd()
				
	elif statWhat.lower() == 'global':
		clearscreen()
		print(optionsstatscheck)
		debug('Checking Global Stats')
		print('\nThe total ammount of streams played is: ' + str(data['data']['logs']['totalPlay']))
		print('\nTheres a total of: ' + str(data['data']['logs']['streamNum']) + ' streams being tracked.')
		print('\nThe total ammount of time the streams have been played for is: ' + data['data']['timeCounters']['totalTime'])
		print('\nThe script has been started: ' + str(data['data']['logs']['timesStarted']) + ' times.')
		print('\nThe script has been restarted: ' + str(data['data']['logs']['timesRestarted']) + ' times.')
		debug('Done')

	elif statWhat.lower() == 'error':
		clearscreen()
		print(optionsstatscheck)
		debug('Checking Error Stats')
		print('\nThe total ammount of times the script has been interuppted is: ' + str(data['data']['errorLogs']['timesInterrupted']))
		print('\nThe total of unsupported services entered is:  ' + str(data['data']['errorLogs']['unsupportedServices']))
		print('\nThe total ammount of unrecgonized commands entered is: ' + str(data['data']['errorLogs']['unRecgonizedCmds']))
		print('\nThe total number of Unknown Errors encountered: ' + str(data['data']['errorLogs']['unknownError']))
		if data['data']['errorLogs']['debug'] == 'True' :
			print('\nCurrently in Debug Mode!')
			pass

	elif statWhat.lower() == 'clear':
		clearscreen()
		print(optionsstatsclear)
		debug('Clear Stats Started')
		print('Do you want to clear global stats or the stats of a specific user?')
		statClear = input('Or do you want to erase all tracked stats and users? (Global, User, Erase): ')
		if statClear.lower() == 'global':
			clearscreen()
			print(optionsstatsclear)
			debug('Global Stat Clear')
			data['data']['logs']['totalPlay'] = 0
			data['data']['timeCounters']['totalTime'] = "0 Days 0:0:0"
			data['data']['timeCounters']['secs'] = 0
			data['data']['timeCounters']['mins'] = 0
			data['data']['timeCounters']['hours'] = 0
			data['data']['timeCounters']['days'] = 0
			print('\nStat Clear Done!\n')
			debug('Done')
		elif statClear.lower() == 'user':
			clearscreen()
			print(optionsstatsclear)
			debug('User Stat Clear')
			statClearUser = input('Whos stats do you want to clear?: ')
			data['data']['streamData'][statClearUser] = streamDataTemp
			print('\nStat clear done!')
			debug('Done')
		elif statClear.lower() == 'erase':
			debug('File Deleation')
			os.system('del list.json')
			print('\nJson file deleted, regenerating json to default template...')
			data = jsonTemplate
			jsonCheck()
			print('\nJson file recreated, all tracked stats and users erased.')
			debug('Done')
		else:
			print('\nStat clear aborted!')
	elif not statWhat:
		print('No command Entered!')
	else:
		unrecgonizedCmd = data['data']['errorLogs']['unRecgonizedCmds']
		unrecgonizedCmd = unrecgonizedCmd + 1
		data['data']['errorLogs']['unRecgonizedCmds'] = unrecgonizedCmd
		print("\n\n----------\nOption Not Recgonized\n-----------\n\n")
	debug('Stat Check Done')
		
	

#Individual user status check
def check():
	clearscreen()
	debug('Individual User Status Check Started')
	print(optionscheck)
	user = input('User to check status of: ')	
	if not user:
		print('No Username entered!')
	else:
		print('')
		list(user)
		print('')
	debug('Individual Check done')
	
#Loops through the json to check the status of users and prints using print()
def lvstList():
	global data
	global datanum
	global data_file

	clearscreen()
	print(optionslist)
	debug('User List started')
	for i in range(len(data["streams"])):
		if data['streams'][i] != "null":
			datanum = i
	debug('StreamNum Updateing')
	datanum = datanum + 1
	datanum = str(datanum)
	data['data']['logs']['streamNum'] = int(datanum)
	debug('StreamNum Updated')
	print('There are ' + datanum + ' streams on being tracked.\n\nDisplaying Online Users')
	for i in range(len(data["streams"])):
		if data["streams"][i] != "null":
			if check_user(data["streams"][i]) != 1:
				list(data["streams"][i])
	debug('List Done')

#Command to open a stream
def openstream():
	global service
	global lvst
	global lsTwitch
	global lvsting
	global lsYoutube
	global audio
	global options
	global streamError

	clearscreen()
	print(optionsopen)
	debug('Opening Stream Started')
	service = input('What stream service? (Youtube or Twitch): ')

	if service.lower() == 'youtube' or service.lower() == 'twitch':
		clearscreen()
		print(optionsstream)
		debug('Service Recived ' + service)
		lvst = input('What stream?: ')
		debug('Streamer Recived ' + lvst)
		#Process to use for twitch streams
		if not lvst:
			print('\nNo Stream Entered')
			streamError = True
		elif service.lower() == 'twitch':
			try:
				audioOnly = data['data']['streamData'][lvst.lower()]['musicStream']
				if audioOnly == 'true':
					clearscreen()
					print(optionsopenaudio)
					debug('Music stream')
					audio = input('Do you want to do audio only?: ')
					debug('Recived' + audio)
					if audio.lower() == 'yes':
						lvsting = lsTwitch + lvst + ' audio'
					else:
						lvsting = lsTwitch + lvst + ' source'
						
				else:
					lvsting = lsTwitch + lvst + ' source'
				
			except:
				lvsting = lsTwitch + lvst + ' source'
				return
			debug('Twitch Stream commands set')
		#Process for youtube streams
		elif service.lower() == 'youtube':
			clearscreen()
			print(optionsopenaudio)
			if lvst[1:32] == 'https://www.youtube.com/watch?v=':
				audio = input('Do you want to do audio only?: ')
				if audio.lower() == 'yes':
					lvsting = lsYoutube + lvst[32:] + ' audio_mp4'
				else:
					lvsting = lsYoutube + lvst[32:] + ' best'
					
			else:
				audio = input('Do you want to do audio only?: ')
				if audio.lower() == 'yes':
					lvsting = lsYoutube + lvst + ' audio_mp4'
				else:
					lvsting = lsYoutube + lvst + ' best'
			debug('Youtube commands set')
			
	elif not service:
		print('\nNo Stream Service Entered!')
		streamError = True
	else:
		print('\nStream service not supported!\n')
		streamError = True
		serviceErrorCnt = data['data']['errorLogs']['unsupportedServices']
		serviceErrorCnt = serviceErrorCnt + 1
		data['data']['errorLogs']['unsupportedServices'] = serviceErrorCnt
	debug('Open stream done')
	
#Starts timer and opens stream

def cmdwin():
	global times
	global lvsting
	global options
	global streamError

	debug('Opening Stream')
	if streamError == False:
		clearscreen()
		print(optionsstreaming)
		print('Opening ' + lvst + "'s stream on " + service + ".\n")
		try:
			print('Total times ' + lvst + " has been played: " + str(data['data']['streamData'][lvst]['playCount']) + ".\n")
			print('Total ammount of time ' + lvst + " Has been played for: " + data['data']['streamData'][lvst]['totalTime'] + " \n")	
		except:
			pass
		start = time.time()
		os.system(lvsting)
		end = time.time()
		times = end - start
		times = int(times)
		debug('Stream Finished')
	else:
		print('\nThere was a error opening the stream!')
 
 #Timer calculation
def timeCalc():
	global times
	global timem
	global timeh

	debug('Time Calculation Started')
	while times > 59:
		debug('Calculating Minutes')
		times = times - 60
		timem = timem + 1
	while timem > 59:
		debug('Calculating Hours')
		timem = timem - 60
		timeh = timeh + 1
	#converts timer values to strings to display with print
	times = str(times)
	timem = str(timem)
	timeh = str(timeh)
	#Prints the elapsed time
	debug('Setting ElapsedTime String')
	elapsedTime = timeh + ':' + timem + ':' + times
	print('')
	print ('Time elapsed: ' + elapsedTime)
	print('')
	debug('Time Calculation done')

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
		debug('Updateing User play count') 
		playnum = data['data']['streamData'][lvst]['playCount']
		playnum = playnum + 1
		data['data']['streamData'][lvst]['playCount'] = playnum
		debug('Play count added')
	except:
		pass

	#Updates the total play count for all streams
	debug('Getting total play counters')
	totalplay = data['data']['logs']['totalPlay']
	totalplay = totalplay + 1
	data['data']['logs']['totalPlay'] = totalplay
	debug('Getting total time counters')
	#Updates overall time totals
	totalsec = data['data']['timeCounters']['secs']
	totalmin = data['data']['timeCounters']['mins']
	totalhrs = data['data']['timeCounters']['hours']
	totaldays = data['data']['timeCounters']['days']
	debug('Converting calculated timer unto int')
	times = int(times)
	timem = int(timem)
	timeh = int(timeh)

	debug('Adding total timers')
	totalsec = totalsec + times
	totalmin = totalmin + timem
	totalhrs = totalhrs + timeh
	debug(['TotalSeconds: ' + str(totalsec),
		   'TotalMinutes: ' + str(totalmin),
		   'TotalHours: ' + str(totalhrs),
		   'TotalDays: ' + str(totaldays)])
	debug('Subtracting extras')
	while totalsec > 59:
		debug('One minute over')
		totalsec = totalsec - 60
		totalmin = totalmin + 1
		debug('Added one minute')
		
	while totalmin > 59:
		debug('One hour over')
		totalmin = totalmin - 60
		totalhrs = totalhrs + 1
		debug('Added One hour')
		
	while totalhrs > 23:
		debug('one day over')
		totalhrs = totalhrs - 24
		totaldays = totaldays + 1
		debug('one day added')
		
	debug(['TotalSeconds: ' + str(totalsec),
		   'TotalMinutes: ' + str(totalmin),
		   'TotalHours: ' + str(totalhrs),
		   'TotalDays: ' + str(totaldays)])

	debug('Adding times into json')
	data['data']['timeCounters']['secs'] = totalsec
	debug('Seconds done')
	data['data']['timeCounters']['mins'] = totalmin
	debug('Minutes done')
	data['data']['timeCounters']['hours'] = totalhrs
	debug('Hours done')
	data['data']['timeCounters']['days'] = totaldays
	debug('Days done')
	debug('Converting times to strings')
	totalsec = str(totalsec)
	totalmin = str(totalmin)
	totalhrs = str(totalhrs)
	totaldays = str(totaldays)
	debug('Combining strings')
	totalelapsed = totaldays + " Days " + totalhrs + ":" + totalmin + ":" + totalsec
	debug('Setting time string into json')
	data['data']['timeCounters']['totalTime'] = totalelapsed

	#Updates user time totals
	if service.lower() == 'twitch':
		try:
			debug('Pulling user totals')
			totalusersec = data['data']['streamData'][lvst]['secs']
			totalusermin = data['data']['streamData'][lvst]['mins']
			totaluserhrs = data['data']['streamData'][lvst]['hours']
			totaluserdays = data['data']['streamData'][lvst]['days']
			debug('Adding totals')
			totalusersec = totalusersec + times
			totalusermin = totalusermin + timem
			totaluserhrs = totaluserhrs + timeh
			debug(['TotalUserSeconds: ' + str(totalusersec),
				   'TotalUserMinutes: ' + str(totalusermin),
				   'TotalUserHours: ' + str(totaluserhrs),
				   'TotalUserDays: ' + str(totaluserdays)])
			debug('Removing excess')
			while totalusersec > 59:
				debug('One minute over')
				totalusersec = totalusersec - 60
				totalusermin = totalusermin + 1
				debug('One minute added')
	
			while totalusermin > 59:
				debug('One hour over')
				totalusermin = totalusermin - 60
				totaluserhrs = totaluserhrs + 1
				debug('One hour added')

			while totaluserhrs > 23:
				debug('One day over')
				totaluserhrs = totaluserhrs - 24
				totaluserdays = totaluserdays + 1
				debug('One day added')
				
			debug(['TotalUserSeconds: ' + str(totalusersec),
				   'TotalUserMinutes: ' + str(totalusermin),
				   'TotalUserHours: ' + str(totaluserhrs),
				   'TotalUserDays: ' + str(totaluserdays)])
			debug('Setting times into json')
			data['data']['streamData'][lvst]['secs'] = totalusersec
			debug('seconds done')
			data['data']['streamData'][lvst]['mins'] = totalusermin
			debug('Minutes done')
			data['data']['streamData'][lvst]['hours'] = totaluserhrs
			debug('Hours done')
			data['data']['streamData'][lvst]['days'] = totaluserdays
			debug('Days done')
			debug('Converting times to strings')

			debug(['TotalUserSeconds: ' + str(totalusersec),
				   'TotalUserMinutes: ' + str(totalusermin),
				   'TotalUserHours: ' + str(totaluserhrs),
				   'TotalUserDays: ' + str(totaluserdays)])

			debug('Adding string togther')
			totaluserelapsed = totaluserdays + " Days " + totaluserhrs + ":" + totalusermin + ":" + totalusersec
			debug('Setting string in json')
			data['data']['streamData'][lvst]['totalTime'] = totaluserelapsed
		except:
			pass
	debug('Stat Tracking Done')

#Main Starter
def start():
	global option
	global times
	global timem
	global restart
	global options
	global lvst
	global streamError

	debug('Starting Main starter')
	#Option input
	print(options)
	option = input('What do you want to do?: ')
	clearscreen()
	print(options)

	#checks what option was chosen
	if option.lower() == "check":
		check()
	elif option.lower() == "list":
		lvstList()
	elif option.lower() == "open":
		openstream()
		cmdwin()
		if streamError != True:
			timeCalc()
			stattracker()
	elif option.lower() == "add":
		userAdd()
	elif option.lower() == "stats":
		statCheck()
	elif option.lower() == "debug":
		if data['data']['errorLogs']['debug'] == 'True':
			data['data']['errorLogs']['debug'] = "False"
			print('Debug Set to False')
		elif data['data']['errorLogs']['debug'] == 'False':
			data['data']['errorLogs']['debug'] = "True"
			print('Debug set to True')
	elif not option:
		print('No command Entered!')
	else:
		unrecgonizedCmd = data['data']['errorLogs']['unRecgonizedCmds']
		unrecgonizedCmd = unrecgonizedCmd + 1
		data['data']['errorLogs']['unRecgonizedCmds'] = unrecgonizedCmd
		print("\n\n----------\nOption Not Recgonized\n-----------\n\n")
		
	print('')
	restart = input('Restart the Script?: ')
	debug('Starter Function Done')

#Restarts the script
while restart.lower() in ["yes","y"]:
	try:
		debug('Restarting Script')
		start()
		if restart.lower() in ["yes","y"]:
			clearscreen()
			
	except KeyboardInterrupt:
		print('\n\nEnding Script')
		timesInterrupted = data['data']['errorLogs']['timesInterrupted']
		timesInterrupted = timesInterrupted + 1
		data['data']['errorLogs']['timesInterrupted'] = timesInterrupted
		restart = 'no'
		
	except:
		print('\n\nUnknown Error! You shouldent be seeing this!')
		unknownError = data['data']['errorLogs']['unknownError']
		unknownError = unknownError + 1
		data['data']['errorLogs']['unknownError'] = unknownError
		restart = 'no'
		debug([str(sys.exc_info()), str(traceback.extract_stack())])
		
	if restart.lower() in ["yes","y"]:
		debug('Restart Count Updateing')
		timesRestarted = data['data']['logs']['timesRestarted']
		timesRestarted = timesRestarted + 1
		data['data']['logs']['timesRestarted'] = timesRestarted
		debug('Restart Count updated')

#Script end confirmation
print('')
input("Press Enter to continue...")

debug('--End--')
with open('list.json', "w") as write_file:
	write_file.write(json.dumps(data, sort_keys=True, indent=4, separators=(',', ': ')))
if data['data']['errorLogs']['debug'] == 'True':
	with open('debug.txt', 'w') as debug_file:
		debug_file.write(json.dumps(debglog, sort_keys=True, indent=4, separators=(',', ': ')))
	pass
 
##End##