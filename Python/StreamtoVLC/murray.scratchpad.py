def wright_to_thingy(location,thing_to_wright):
	def i(loc):
		if loc==[]:
			return data
		return i(loc[1:])loc[1]
	i(location)=thing_to_wright
	function_that_updates_json()

def function_that_updates_json():
	with open('list.json', "w") as write_file:
		write_file.write(json.dumps(data, sort_keys=True, indent=4, separators=(',', ': ')))