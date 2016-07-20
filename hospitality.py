valid_gender = ['M','F','MALE','FEMALE','']
valid_locality = ['ANN ARBOR','BUFFALO','CHICAGO','CHINA','CLEVELAND','CLEVELAND HEIGHTS','COLUMBUS','DETROIT','EVANSTON','INDIANAPOLIS','KALAMAZOO','LORAIN','MISSISSAUGA','MONTREAL','NAPERVILLE','PITTSBURGH','TEMPLE CITY','TORONTO','WILLOUGHBY','']
recognized_preferences = ['COT','FLOOR','BED']

class Person:
	def __init__(self, first, last, gender, age, locality, preferences = []):
		"""
		first = String describing first name
		last = String describing last name
		gender = single character or String, 'm' or 'f'. 'M' and 'F' is okay. 
			'male' and 'female' in upper or lower case is okay.
		age = integer, ex: 27. String okay too, ex: "27".
		locality = string, upper or lower case anywhere is okay, but must be spelled correctly.
		preferences = List describing preferences, any subset of: ['floor', 'cot', 'bed']. (FOR NOW)
		"""
		error = ''
		if not (type(first) is str and type(last) is str):
			error += "WARNING: first AND last ARE NOT STRINGS: " + str(first) + ", " + str(last) + "\n"
		self.first = str(first)
		self.last = str(last)
		self.age = int(age)
		if gender.upper() not in valid_gender:
			error += "ERROR: INVALID GENDER INPUT: " + str(gender) + "\n"
		self.gender = gender.upper()
		if locality.upper() not in valid_locality:
			error += "WARNING: UNRECOGNIZED locality INPUT: " + str(locality) + "\n"
			error += "Ignore if input is spelled correctly and valid." + "\n"
		self.locality = locality.upper()
		if preferences == '':
			preferences = []
		elif type(preferences) is str:
			temp = []
			for p in preferences.split(','):
				if p.upper().strip(' ') not in recognized_preferences:
					error += "WARNING: UNRECOGNIZED PREFERENCE: " + p + "\n"
				temp.append(p)
			preferences = temp
		self.preferences = preferences

		if len(error) > 0:
			print error

	def __repr__(self):
		if self.age == -1:
			age = '?'
		else:
			age = self.age
		return "Person: " + str(age) + " year old " + str(self.gender) + " from " + str(self.locality) + " with preferences: " + str(self.preferences) + "\n"

	def first(self):
		return self.first

	def last(self):
		return self.last

	def age(self):
		return self.age

	def gender(self):
		if self.gender == 'MALE':
			return 'M'
		if self.gender == 'FEMALE':
			return 'F'
		return self.gender

	def locality(self):
		return self.locality

	def preferences(self):
		return self.preferences

	def label(self):
		if self.age == -1:
			age = '?'
		else:
			age = self.age
		return str(self.first) + " " + str(self.last) + ", " + str(age)


class Host:
	def __init__(self,name,spaces,preferences):
		"""
		name = String representing host's name
		spaces = list of sleeping places.
			Length of list represents number of sleeping places. 
			Each sleeping place requires a type (cot, floor, bed), with
			optional descritions. Ex: ['cot','floor','floor']
		preferences = list of sleeping place preferences matching 
			the indices of sleeping places. Ex: ['male only','male only','']
		"""
		self.space_types = ['COT','FLOOR','BED']

		error = ''
		if type(name) is not str:
			error += "WARNING: name IS NOT A STRING: " + str(name) + "\n"
		self.name = str(name)
		if type(spaces) is not list:
			error += "ERROR: INVALID INPUT FOR SLEEPING PLACES IS NOT LIST: " + str(spaces) + "\n"
		if type(preferences) is not list:
			error += "ERROR: INVALID INPUT FOR SLEEPING PLACES PREFERENCES IS NOT LIST: " + str(preferences) + "\n"
		for i in spaces:
			if i.upper() not in self.space_types:
				error += "ERROR: INVALID SLEEPING SPACE TYPE: " + str(i) + "\n"
		self.spaces = spaces
		self.preferences = preferences

		if len(error) > 0:
			print error

	def __repr__(self):
		return "Host: " + str(self.first) + " " + str(self.last) + ", with " + str(len(self.spaces)) + " spaces: " + str(self.spaces) + " with preferences: " + str(self.preferences)

	def first(self):
		return self.first

	def last(self):
		return self.last

	def spaces(self):
		return self.spaces

	def preferences(self):
		return self.preferences

