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
import signal

#Sets up the input variables that is used later in the script
global jsonTemplate

global data

def jsonCheck():
	test = os.path.isfile('list.json')
	if test == False:
		debug('List.json Not Found, Creating...')
		fname = "list.json"
		with open(fname, 'w') as fout:
			fout.write(json.dumps(jsonTemplate, sort_keys=True, indent=4, separators=(',', ': ')))
			fout.close()
		
	elif test:
		debug('List.json Found, Continueing...')

def clearscreen():
	if platform.system()=='Linux':
		os.system('clear')
	else:
		os.system('cls')

#Menu Prompts
global options
global optionsstreaming
global optionsopen
global optionsstream
global optionsopenaudio
global optionslist
global optionscheck
global optionsstatscheck
global optionsstatsclear
global optionsadd
global listing
	
def jsonWrite():
	with open('list.json', "w") as write_file:
		write_file.write(json.dumps(data, sort_keys=True, indent=4, separators=(',', ': ')))

def writeToJson(location,val,d='data',top=1):
	if location==[]:
		d=val
		return d
	else:
		if type(d)==type(''):
			globals()[d][location[0]]=writeToJson(location[1:],val,globals()[d][location[0]],0)
		else:
			d[location[0]]=writeToJson(location[1:],val,d[location[0]],0)
			return d
		if top:
			jsonWrite()

#Debug function to append time stamps and write to files
#i made only outputting text depend on the switch and outputting to log always on
def debug(info,error=0):
	if type(info)==type([]):
		for a in info:
			debug(a,error)
	else:
		import datetime
		if error:
			dbg="ERROR: "
		else:
			dbg="DEBUG: "
		mes=datetime.datetime.now().strftime("[%Y-%m-%dT%H:%M:%S] ")+dbg +str(info)
		if data['data']['errorLogs']['debug'] in [1,'1']:
			print(mes)
			with open("debug.txt", "a") as myfile:
				myfile.write(mes+'\n')
		elif error==1:
			with open("debug.txt", "a") as myfile:
				myfile.write(mes+'\n')

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
		out=''
		if check_user(urc) == 0:
			out=str(urc + ' Is ONLINE')
		elif check_user(urc) == 1:
			out=str(urc + ' Is offline')
		elif check_user(urc) == 2:
			out=str(urc + ' Is not found')
		elif check_user(urc) == 3:
			out=str('Error in checking status')
	except KeyboardInterrupt:
		pass
	debug('User Status Processed')
	return (listing+'\n'+out+'\n'+listing)

#Function to add new tracked users
def userAdd(username,statAdd):
	allRecords = 0
	debug('User Add Started')
	if statAdd:
		array = data['streams']
		array.append(statwho.lower())
		data['data']['streamData'][statwho.lower()] = streamDataTemp
		debug('Short User Add Done')
		debug('Counting Usernames')
	else:
		#for i in range(len(data["streams"])):
			#allRecords = allRecords + 1
		allRecords+=len(data["streams"])
		#why was this done as a for loop?
	debug('Usernames Counted')
	#debug('Username Count Printed')
	array = data['streams']
	array.append(username.lower())
	data['data']['streamData'][username.lower()] = streamDataTemp
	debug('User added')
	#why was this done as a loop?
	datanum=len(data["streams"])
	#for i in range(len(data["streams"])):
		#datanum = i
	debug('User Music Status added')
	datanum = datanum + 1
	data['data']['logs']['streamNum'] = datanum
	debug('StreamNum Updated')
	return allRecords

def setUserMusic(username):
	data['data']['streamData'][username]['musicStream'] = 'true'

def statCheck(statWhat,statOpt,statUser):
	out=''
	debug('Stat Check Started')
	statAdd = 0
	if statWhat.lower() == 'user':
		debug('Retriveing User Stats')
		out+="\nThis stream has been played: " + str(data['data']['streamData'][statUser.lower()]['playCount'])
		out+="\nThis stream has been played for a total of: " + data['data']['streamData'][statUser.lower()]['totalTime']
		if data['data']['streamData'][statUser.lower()]['musicStream'] == 'true':
			out+='\nThis stream is also marked as a music stream'
		debug('Done')
	elif statWhat.lower() == 'global':
		out+=optionsstatscheck
		debug('Checking Global Stats')
		out+='\nThe total ammount of streams played is: ' + str(data['data']['logs']['totalPlay'])
		out+='\nTheres a total of: ' + str(data['data']['logs']['streamNum']) + ' streams being tracked.'
		out+='\nThe total ammount of time the streams have been played for is: ' + data['data']['timeCounters']['totalTime']
		out+='\nThe script has been started: ' + str(data['data']['logs']['timesStarted']) + ' times.'
		out+='\nThe script has been restarted: ' + str(data['data']['logs']['timesRestarted']) + ' times.'
		debug('Done')
	elif statWhat.lower() == 'error':
		out+=optionsstatscheck
		debug('Checking Error Stats')
		out+='\nThe total ammount of times the script has been interuppted is: ' + str(data['data']['errorLogs']['timesInterrupted'])
		out+='\nThe total of unsupported services entered is:  ' + str(data['data']['errorLogs']['unsupportedServices'])
		out+='\nThe total ammount of unrecgonized commands entered is: ' + str(data['data']['errorLogs']['unRecgonizedCmds'])
		out+='\nThe total number of Unknown Errors encountered: ' + str(data['data']['errorLogs']['unknownError'])
		if data['data']['errorLogs']['debug'] == 'True' :
			out+='\nCurrently in Debug Mode!'
	elif statWhat.lower() == 'clear':
		if statOpt.lower() == 'global':
			out+=optionsstatsclear
			debug('Global Stat Clear')
			data['data']['logs']['totalPlay'] = 0
			data['data']['timeCounters']['totalTime'] = "0 Days 0:0:0"
			data['data']['timeCounters']['secs'] = 0
			data['data']['timeCounters']['mins'] = 0
			data['data']['timeCounters']['hours'] = 0
			data['data']['timeCounters']['days'] = 0
			out+='\nStat Clear Done!\n'
			debug('Done')
		elif statOpt.lower() == 'user':
			out+=optionsstatsclear
			debug('User Stat Clear')
			data['data']['streamData'][statUser] = streamDataTemp
			out+='\nStat clear done!'
			debug('Done')
		elif statOpt.lower() == 'erase':
			debug('File Deleation')
			os.system('del list.json')
			out+='\nJson file deleted, regenerating json to default template...'
			data = jsonTemplate
			jsonCheck()
			out+='\nJson file recreated, all tracked stats and users erased.'
			debug('Done')
		else:
			out+='\nStat clear aborted!'
	elif not statWhat:
		print('No command Entered!')
	else:
		unrecgonizedCmd = data['data']['errorLogs']['unRecgonizedCmds']
		unrecgonizedCmd = unrecgonizedCmd + 1
		data['data']['errorLogs']['unRecgonizedCmds'] = unrecgonizedCmd
		print("\n\n----------\nOption Not Recgonized\n-----------\n\n")
	debug('Stat Check Done')
	return out

#Loops through the json to check the status of users and prints using print()
def lvstList():
	global data
	global datanum
	global data_file

	out=optionslist
	debug('User List started')
	for i in range(len(data["streams"])):
		if data['streams'][i] != "null":
			datanum = i
	debug('StreamNum Updateing')
	datanum = datanum + 1
	datanum = str(datanum)
	data['data']['logs']['streamNum'] = int(datanum)
	debug('StreamNum Updated')
	out+='There are ' + datanum + ' streams on being tracked.\n\nDisplaying Online Users'
	for i in range(len(data["streams"])):
		if data["streams"][i] != "null":
			if check_user(data["streams"][i]) != 1:
				out+=list(data["streams"][i])
	return out
	debug('List Done')

#Command to open a stream
def openstream(service,lvst,audio):
	lvsting=''
	lsTwitch = 'livestreamer twitch.tv/'
	lsYoutube = 'livestreamer youtube.com/watch?v='

	debug('Opening Stream Started')
	debug('Service Recived ' + service)
	debug('Streamer Recived ' + lvst)
	#Process to use for twitch streams
	if service.lower() == 'twitch':
		try:
			audioOnly = data['data']['streamData'][lvst.lower()]['musicStream']
			if audioOnly == 'true':
				clearscreen()
				print(optionsopenaudio)
				debug('Music stream')
				debug('Recived ' + audio)
				if audio.lower() == 'yes':
					lvsting = lsTwitch + lvst + ' audio'
				else:
					lvsting = lsTwitch + lvst + ' source'
					
			else:
				lvsting = lsTwitch + lvst + ' source'
		except:
			lvsting = lsTwitch + lvst + ' source'
		debug('Twitch Stream commands set')
	#Process for youtube streams
	elif service.lower() == 'youtube':
		if lvst[1:32] == 'https://www.youtube.com/watch?v=':
			if audio.lower() == 'yes':
				lvsting = lsYoutube + lvst[32:] + ' audio_mp4'
			else:
				lvsting = lsYoutube + lvst[32:] + ' best'
		else:
			if audio.lower() == 'yes':
				lvsting = lsYoutube + lvst + ' audio_mp4'
			else:
				lvsting = lsYoutube + lvst + ' best'
		debug('Youtube commands set')
	return lvsting
	debug('Open stream done')

#Starts timer and opens stream

def cmdwin(lvsting):
	debug('Opening Stream')
	start = time.time()
	os.system(lvsting)
	debug('Stream Finished')
	end = time.time()
	duration = end - start
	duration = int(duration)
	debug('Duration Calculated')
	return duration

#Timer calculation
def timeCalc(times,timem,timeh):
	debug('Time Calculation Started')
	while times > 59:
		debug('Calculating Minutes')
		times = times - 60
		timem = timem + 1
	while timem > 59:
		debug('Calculating Hours')
		timem = timem - 60
		timeh = timeh + 1
	debug('Time Calculation done')
	return [times,timem,timeh]

#Updates Stats
def stattracker(lvst,times,audio):
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
	debug('Converting calculated timer into int')
	times = int(times)

	debug('Adding total timers')
	totalsec = totalsec + times

	debug(['TotalSeconds: ' + str(totalsec),
		   'TotalMinutes: ' + str(totalmin),
		   'TotalHours: ' + str(totalhrs),
		   'TotalDays: ' + str(totaldays)])
	
	debug('Calculating Carries')
	
	[totalsec,totalmin,totalhrs]=timeCalc(totalsec,totalmin,totalhrs)
	while totalhrs > 23:
		debug('one day over')
		totalhrs = totalhrs - 24
		totaldays = totaldays + 1
		debug('one day added')
		
	debug(['TotalSeconds: ' + str(totalsec),
		   'TotalMinutes: ' + str(totalmin),
		   'TotalHours: ' + str(totalhrs),
		   'TotalDays: ' + str(totaldays)])

	debug('Inserting time data into json')
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

			debug(['TotalUserSeconds: ' + str(totalusersec),
				   'TotalUserMinutes: ' + str(totalusermin),
				   'TotalUserHours: ' + str(totaluserhrs),
				   'TotalUserDays: ' + str(totaluserdays)])
			
			debug('Calculating Carries')
			[totalsec,totalmin,totalhrs]=timeCalc(totalsec,totalmin,totalhrs)
			while totaluserhrs > 23:
				debug('One day over')
				totaluserhrs = totaluserhrs - 24
				totaluserdays = totaluserdays + 1
				debug('One day added')
				
			debug(['TotalUserSeconds: ' + str(totalusersec),
				   'TotalUserMinutes: ' + str(totalusermin),
				   'TotalUserHours: ' + str(totaluserhrs),
				   'TotalUserDays: ' + str(totaluserdays)])

			debug('Inserting time data into json')
			writeToJson(['data','streamData',lvst,'secs'],totalusersec)
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



####################### print and input are not allowed above this line #######################



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
		print(list(user))
		print('')
	debug('Individual Check done')

def mainopen():
	times=0
	streamError=False
	clearscreen()
	print(optionsopen)
	service = input('What stream service? (Youtube or Twitch): ')
	if service.lower() == 'youtube' or service.lower() == 'twitch':
		clearscreen()
		print(optionsstream)
		debug('Service Recived ' + service)
		lvst = input('What stream?: ')
		if not lvst:
			print('\nNo Stream Entered')
			streamError = True
		else:
			audio=''
			if service.lower() == 'youtube':
				clearscreen()
				print(optionsopenaudio)
				if lvst[1:32] == 'https://www.youtube.com/watch?v=':
					audio = input('Do you want to do audio only?: ')
			lvsting=openstream(service,lvst,audio)
	elif not service:
		print('\nNo Stream Service Entered!')
		streamError = True
	else:
		print('\nStream service not supported!\n')
		streamError = True
		serviceErrorCnt = data['data']['errorLogs']['unsupportedServices']
		serviceErrorCnt = serviceErrorCnt + 1
		data['data']['errorLogs']['unsupportedServices'] = serviceErrorCnt
	
	if not streamError:
		clearscreen()
		print(optionsstreaming)
		print('Opening ' + lvst + "'s stream on " + service + ".\n")
		try:
			print('Total times ' + lvst + " has been played: " + str(data['data']['streamData'][lvst]['playCount']) + ".\n")
			print('Total ammount of time ' + lvst + " Has been played for: " + data['data']['streamData'][lvst]['totalTime'] + " \n")	
		except:
			pass
		times+=cmdwin(lvsting)
		#Prints the elapsed time
		debug('Setting ElapsedTime String')
		elapsedTime = str(timeh) + ':' + str(timem) + ':' + str(times)
		print('')
		print('Time elapsed: ' + elapsedTime)
		print('')
		stattracker(lvst,times)
	else:
		print('\nThere was a error opening the stream!')

def add(username='',statAdd=0):
	if username == '':
		input('Name of the user to add?: ')
	else:
		print('Adding user: '+username)
	while username=='':
		print('Please type in a user-name and not leave the line blank.')
		input('Name of the user to add?: ')
	allRecords=userAdd(username,statAdd)

	clearscreen()
	print(optionsadd)
	if allRecords < 1:
		print('\nThere are currently: no tracked users.' + '\n')
	elif allRecords == 1:
		print('\nThere is currently: 1 tracked user.' + '\n')
	else:
		print('\nThere are currently: ' + str(allRecords) + ' tracked users.' + '\n')

	isMusicStream = input('Is this stream a music stream? (Yes or No): ')
	if isMusicStream.lower() == 'yes':
		setUserMusic(username)

def stats():
	clearscreen()
	print(optionsstatscheck)
	statWhat = input('Which stat do you want to see? (User, Global, Error or Clear): ')
	statOpt=''
	statUser=''
	if statWhat.lower() == 'user':
		clearscreen()
		print(optionsstatscheck)
		statUser = input('Who do you want to check the stats of?: ')
		if statUser.lower() not in data['data']['streamData']:
			clearscreen()
			print(optionsstatscheck)
			print('\nThere are no stats for this user!\n')
			debug('Done')
			statAdd = ynQuestion('Whould you like to add this user to the tracked list?: ')
			if statAdd:
				add(statUser,statAdd)
		else:
			clearscreen()
			print(statCheck(statWhat,statOpt,statUser))
	elif statWhat.lower() == 'clear':
		clearscreen()
		print(optionsstatsclear)
		debug('Clear Stats Started')
		print('Do you want to clear global stats or the stats of a specific user?')
		statOpt = input('Or do you want to erase all tracked stats and users? (Global, User, Erase): ')
		if statOpt.lower()=='user':
			statUser = input('Whos stats do you want to clear?: ')
		clearscreen()
		print (statCheck(statWhat,statOpt,statUser))
	else:
		clearscreen()
		print (statCheck(statWhat,statOpt,statUser))

def ynQuestion(prompt,default=''):
	prompt=str(prompt)
	default=str(default)

	if default.lower() in ['y','yes','1']:
		answer = input(prompt+' [Yes/no]: ')
	elif default.lower() in ['n','no','0']:
		answer = input(prompt+' [yes/No]: ')
	else:
		answer = input(prompt+' [yes/no]: ')
	
	if answer=='':
		answer=default
	
	if answer.lower() in ['y','yes','1']:
		return 1
	elif answer.lower() in ['n','no','0']:
		return 0
	else:
		return ynQuestion(prompt,default)

#Main Starter
def menu():
	global restart
	global options

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
		clearscreen()
		print("This wight take a while...")
		print(lvstList())
	elif option.lower() == "open":
		mainopen()
	elif option.lower() == "add":
		clearscreen()
		add()
	elif option.lower() == "stats":
		stats()
	elif option.lower() == "debug":
		if data['data']['errorLogs']['debug'] == 'True':
			debug('Logging disabled')
			debug('--End--')
			data['data']['errorLogs']['debug'] = "False"
			print('Debug Set to False')
		else:#if data['data']['errorLogs']['debug'] == 'False':
			data['data']['errorLogs']['debug'] = "True"
			debug('--Start--')
			debug('Logging enabled')
			print('Debug set to True')

	elif not option:
		print('No command Entered!')
	else:
		debug('unrecgonized command: '+option)
		#unrecgonizedCmd = data['data']['errorLogs']['unRecgonizedCmds']
		#unrecgonizedCmd = unrecgonizedCmd + 1
		#data['data']['errorLogs']['unRecgonizedCmds'] = unrecgonizedCmd
		data['data']['errorLogs']['unRecgonizedCmds']+=1
		print("\n\n----------\nOption Not Recgonized\n-----------\n\n")
		
	print('')
	restart = input('Restart the Script?: ')
	debug('Main menu end')
	return restart

def init():
	global data
	global jsonTemplate
	jsonTemplate =  {"data": {"errorLogs": {"timesInterrupted": 0, "unRecgonizedCmds": 0, "unknownError": 0, "unsupportedServices": 0}, "logs": {"streamNum": 0, "timesRestarted": 0, "timesStarted": 0, "totalPlay": 0}, "streamData": {"streamTemplate": {"days": 0, "hours": 0, "mins": 0, "musicStream": "true", "playCount": 0, "secs": 0, "totalTime": "0 Days 0:0:0"}}}, "streams": []}
	
	clearscreen()
	
	#Opens the json file for the list of tracked streamers
	with open('list.json') as data_file:
		data = json.load(data_file)
		data_file.close()

	debug('--Start--')
	streamDataTemp = data['data']['streamData']['streamTemplate']
	startCount = data['data']['logs']['timesStarted']
	startCount = startCount + 1
	writeToJson(['data','logs','timesStarted'],startCount)
	debug('Start Count Added Onto')

	#Menu Prompts
	if 1:
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

def terminate():
	#Script end confirmation
	print('')
	input("Press Enter to continue...")

	debug('Terminating')
	debug('--End--')

	#write To the json file
	with open('list.json', "w") as write_file:
		write_file.write(json.dumps(data, sort_keys=True, indent=4, separators=(',', ': ')))

def main():
	init()
	
	restart = 'yes'
	#Restarts the script
	while restart.lower() in ["yes","y"]:
		try:
			debug('Restarting Script')
			restart=menu()
			if restart.lower() in ["yes","y"]:
				clearscreen()
				
		except KeyboardInterrupt:
			debug('Ending Script')
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
			debug([str(sys.exc_info()), str(traceback.extract_stack())],1)
			
		if restart.lower() in ["yes","y"]:
			debug('Restart Count Updating')
			timesRestarted = data['data']['logs']['timesRestarted']
			timesRestarted = timesRestarted + 1
			data['data']['logs']['timesRestarted'] = timesRestarted
			debug('Restart Count updated')

	terminate()

def tests():
	pass
	#put tests here

main()
