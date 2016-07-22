valid_gender = ['M','F','MALE','FEMALE','']
valid_locality = ['ANN ARBOR','BUFFALO','CHICAGO','CHINA','CLEVELAND','CLEVELAND HEIGHTS','COLUMBUS','DETROIT','EVANSTON','INDIANAPOLIS','KALAMAZOO','LORAIN','MISSISSAUGA','MONTREAL','NAPERVILLE','PITTSBURGH','TEMPLE CITY','TORONTO','WILLOUGHBY','']
recognized_preferences = ['COT','FLOOR','BED']

class Person:
	def __init__(self, first, last, gender, age, locality, preferences, assigned = False):
		"""
		first = String describing first name
		last = String describing last name
		gender = single character or String, 'm' or 'f'. 'M' and 'F' is okay. 
			'male' and 'female' in upper or lower case is okay.
		age = integer, ex: 27. String okay too, ex: "27".
		locality = string, upper or lower case anywhere is okay, but must be spelled correctly.
		preferences = Dictionary describing preferences: {'sleeping_space': ['floor', 'cot', 'bed']}. (FOR NOW)
		assigned = Boolean describing if this person has been assigned to a host.
		"""
		error = ''

		# set first and last names
		# check if they are strings and output a warning if they are not. Either way, try to set them.
		if not (type(first) is str and type(last) is str):
			error += "WARNING: first AND last ARE NOT STRINGS: " + str(first) + ", " + str(last) + "\n"
		self.first = str(first)
		self.last = str(last)
		
		# gender
		# check if valid input, and for final value to be 'M' or 'F'
		if gender.upper() not in valid_gender:
			error += "WARNING: UNRECOGNIZED GENDER INPUT: " + str(gender) + "\n"
		self.gender = gender.upper()
		if gender.upper() == 'MALE':
			self.gender = 'M'
		if gender.upper() == 'FEMALE':
			self.gender = 'F'

		# set age
		# allows for string input if it can be converted into an integer
		# check if age doesn't make sense (like negatives)
		# -1 means the age is missing or unknown
		self.age = int(age)
		if self.age < -1:
			error += "WARNING: NEGATIVE AGE INPUT: " + str(self.age)+ ", SETTING AGE TO -1 (MISSING)" + "\n"
			self.age = -1

		# set locality
		# check if locality is recognized
		# TODO: ASK USER IF LOCALITY IS VALID AND ADD TO RECOGNIZED LOCALITIES
		# assumes that locality is a string
		if locality.upper() not in valid_locality:
			error += "WARNING: UNRECOGNIZED locality INPUT: " + str(locality) + "\n"
			error += "Ignore if input is spelled correctly and valid." + "\n"
		self.locality = locality.upper()


		if preferences == '':
			preferences = {'sleeping_space':['floor','cot','bed']}
		elif type(preferences) is str:
			temp = {'sleeping_space':[]}
			for p in preferences.split(','):
				if p.upper().strip(' ') not in recognized_preferences:
					error += "WARNING: UNRECOGNIZED PREFERENCE: " + p + "\n"
				temp['sleeping_space'].append(p)
			preferences = temp
		self.preferences = preferences
		self.assigned = assigned

		if len(error) > 0:
			print error

	def __repr__(self):
		if self.age == -1:
			age = '?'
		else:
			age = self.age

		return self.first + " " + self.last + ": " + str(age) + " year old " + str(self.gender) + " from " + str(self.locality) + " with preferences: " + str(self.preferences) + ", assigned: " + str(self.assigned) + "\n"

	def first(self):
		return self.first

	def last(self):
		return self.last

	def age(self):
		return self.age

	def gender(self):
		return self.gender

	def locality(self):
		return self.locality

	def preferences(self):
		return self.preferences

	def assigned(self):
		return self.assigned

	def set_assigned(self,b):
		self.assigned = b

	def label(self):
		"""
		Concise label for the Person, just name and age.
		"""
		if self.age == -1:
			age = '?'
		else:
			age = self.age
		return str(self.first) + " " + str(self.last) + ", " + str(age)


class Host:
	def __init__(self,name,spaces,preferences):
		"""
		name = String representing host's name
		spaces = String of sleeping places to be processed into Dictionary. 
			Each sleeping place requires a type (cot, floor, bed), with
			number of spaces. Ex: '4 cot, 8 floor, 1 bed'
		preferences = Dictionary of preferences: {'gender':'male','age':'>40'} (NONE IMPLEMENTED YET)
		people = people this host is hosting
		"""
		self.space_types = ['COT','FLOOR','BED']

		error = ''

		# name
		# check if str, then set regardless
		if type(name) is not str:
			error += "WARNING: name IS NOT A STRING: " + str(name) + "\n"
		self.name = str(name)

		# spaces
		# process spaces and store in dictionary
		if type(spaces) is not str:
			error += "ERROR: INVALID INPUT FOR SLEEPING SPACES IS NOT STRING: " + str(spaces) + "\n"
		self.spaces = {'cot':0,'floor':0,'bed':0}
		for i in spaces.split(','):
			k = i.strip(' ').split(' ')
			if k[1].upper().strip(' ') not in self.space_types:
				error += "WARNING: UNRECOGNIZED SLEEPING SPACES INPUT: " + str(i) + ", IGNORED" "\n"
			else:
				self.spaces[k[1].lower()] += int(k[0])

		# preferences (NOT IMPLEMENTED YET)
		if type(preferences) is not str:
			error += "ERROR: INVALID INPUT FOR PREFERENCES IS NOT STRING: " + str(preferences) + "\n"
		self.preferences = preferences

		# list of people the host will be hosting
		self.people = [] # A newly initialized host is not hosting anyone

		if len(error) > 0:
			print error

	def __repr__(self):
		if self.preferences == '':	
			return "Host: " + str(self.name) + ", with " + str(sum(self.spaces.values())) + " spaces: " + str(self.spaces) + " with no preferences\n"
		else:
			return "Host: " + str(self.name) + ", with " + str(sum(self.spaces.values())) + " spaces: " + str(self.spaces) + " with preferences: " + str(self.preferences) + "\n"

	def name(self):
		return self.name

	def spaces(self):
		return self.spaces

	def preferences(self):
		return self.preferences

	def people(self):
		return self.people

	def assign(self,person):
		for i in person.preferences['sleeping_space']:
			if self.spaces[i] > 0:
				self.spaces[i] -= 1
				person.set_assigned(True)
				self.people.append(person)
				return True
		return False

	def label(self):
		return str(self.name) + ": " + str(self.spaces)

