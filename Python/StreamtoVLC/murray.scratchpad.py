def writeToData(location,val):
	def i(loc):
		if loc==[]:
			return data
		return i(loc[:-1])[loc[-1]]
	i(location)=val
	#print i(location)
	jsonWrite()

def writeToData(location,val,d=data):
	if location==[]:
		d=val
		jsonWrite()
	else:
		writeToData(location[:-1],val,d[location[-1]])

def jsonWrite():
	with open('list.json', "w") as write_file:
		write_file.write(json.dumps(data, sort_keys=True, indent=4, separators=(',', ': ')))