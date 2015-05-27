def writeToData(location,val):
	def i(loc):
		if loc==[]:
			return data
		return i(loc[:-1])[loc[-1]]
	i(location)=val
	#print i(location)
	jsonWrite()

def writeToData(location,val,d=data,top=1):
	if location==[]:
		d=val
		return d
	else:
		d[location[0]]=writeToData(location[1:],val,d[location[0]],0)
		return d
		if top:
			jsonWrite()

def jsonWrite():
	with open('list.json', "w") as write_file:
		write_file.write(json.dumps(data, sort_keys=True, indent=4, separators=(',', ': ')))