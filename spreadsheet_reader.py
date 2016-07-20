from hospitality import *
import csv,sys

def read_people(filename):
	"""
	Extracts .csv for list of attendees and relevant data.
	CSV file must be formatted correctly.
	"""
	people = []
	csv_data = []
	f = open(filename, 'rb')

	reader = csv.reader(f)
	for row in reader:
		csv_data.append(row)

	for i in csv_data[0]:
		j = i.upper().strip(' ') 
		if j == 'LOCALITY':
			locality_i = csv_data[0].index(i)
		elif j == 'FIRST NAME':
			first_i = csv_data[0].index(i)
		elif j == 'LAST NAME':
			last_i = csv_data[0].index(i)
		elif j == 'GENDER':
			gender_i = csv_data[0].index(i)
		elif j == 'AGE':
			age_i = csv_data[0].index(i)
		elif j == 'PREFERENCES':
			preferences_i = csv_data[0].index(i)

	data = csv_data[1:]

	for k in data:
		if k[age_i] == '':
			k[age_i] = -1
		people.append(Person(k[first_i],k[last_i],k[gender_i],k[age_i],k[locality_i],k[preferences_i]))
		# how to include preferences?
		
	# for i in people:
	# 	print i.first,i.last,i.gender,i.age,i.locality, i.preferences
	return people

def read_hosts(filename):
	"""
	Extracts .csv for list of hosts and relevant data.
	CSV file must be formatted correctly.
	"""
	hosts = []
	csv_data = []
	f = open(filename, 'rb')

	reader = csv.reader(f)
	for row in reader:
		csv_data.append(row)

	for i in csv_data[0]:
		j = i.upper().strip(' ')
		if 'NAME' in j:
			if 'name_i' not in locals():
				name_i = csv_data[0].index(i)
			else:
				name_i2 = csv_data[0].index(i)
		elif 'SPACES' in j or 'SLEEP' in j or 'PLACES' in j:
			spaces_i = csv_data[0].index(i)
		elif j == 'PREFERENCES':
			preferences_i = csv_data[0].index(i)

	data = csv_data[1:]

	if 'name_i2' not in locals():
		for k in data:
			hosts.append(Host(k[name_i],k[spaces_i],k[preferences_i]))
	else:
		for k in data:
			hosts.append(Host(k[name_i]+", "+k[name_i2],k[spaces_i],k[preferences_i]))


	return hosts
