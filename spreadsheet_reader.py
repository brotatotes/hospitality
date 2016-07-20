from hospitality import *
import csv,sys


def read_csv(filename):
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
		if j == 'FIRST NAME':
			first_i = csv_data[0].index(i)
		if j == 'LAST NAME':
			last_i = csv_data[0].index(i)
		if j == 'GENDER':
			gender_i = csv_data[0].index(i)
		if j == 'AGE':
			age_i = csv_data[0].index(i)
		if j == 'PREFERENCES':
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