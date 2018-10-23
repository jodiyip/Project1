import os
import filecmp
from dateutil.relativedelta import *
from datetime import date


def getData(file):
	"""This function takes in a file and returns a list of dictionary objects
	with keys first name, last name, email, class and dob. The values are 
	individual data found in the columns"""
	inFile = open(file, "r")
	lines = inFile.readlines()
	# inFile.close()
	lst = list()
	lineSlice = lines[1:]
	for line in lineSlice:
		# creates a dictionary and adds the first name, 
		# last name, email, class, and date of birth
		dictionary = dict()
		finalWords = line.split(",")
		dictionary['First'] = finalWords[0]
		dictionary['Last'] = finalWords[1]
		dictionary['Email'] = finalWords[2]
		dictionary['Class'] = finalWords[3]
		dictionary['DOB'] = finalWords[4]
		# each person is a dicionary
		# adds each item of the dictionary into a list
		lst.append(dictionary)
	return lst
# get a list of dictionary objects from the file
#Input: file name
#Ouput: return a list of dictionary objects where
#the keys are from the first row in the data. and the values are each of the other rows


def mySort(data,col):
	"""This function alphabetically sorts either the first name column or the last name 
	column. It returns the first and last name of the first item after sorting as a string.
	"""
	# alphabatizes the column col
	sort = sorted(data, key = lambda k:k[col])
	# gets and returns the first and last name on the first row
	sortFirst = sort[0]
	return sortFirst['First'] + ' ' + sortFirst['Last']

# Sort based on  key/column
#Input: list of dictionaries and col (key) to sort on
#Output: Return the first item in the sorted list as a string of just: firstName lastName


def classSizes(data):
	"""This function counts the number of students in each class 
	and lists them in descending order
	"""
	freshman = 0
	sophomore = 0
	junior = 0
	senior = 0
	# increases individual class count and adds number into tuple
	for person in data:
		if person['Class'] == "Freshman":
			freshman += 1
			freshmanTuple = ('Freshman', freshman)
		if person['Class'] == "Sophomore":
			sophomore += 1
			sophomoreTuple = ('Sophomore', sophomore)
		if person['Class'] == "Junior":
			junior += 1
			juniorTuple = ('Junior', junior)
		if person['Class'] == "Senior":
			senior += 1
			seniorTuple = ('Senior', senior)
	# adds individual class tuple into a list and sorts 
	# number of students in that class in descending order
	lst = [freshmanTuple, sophomoreTuple, juniorTuple, seniorTuple]
	lst.sort(key=lambda tup:tup[1], reverse=True)
	return(lst)
# Create a histogram
# Input: list of dictionaries
# Output: Return a list of tuples sorted by the number of students in that class in
# descending order
# [('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)]



def findMonth(a):
	""" This function finds and returns the most common month in the data"""
	counts = dict()
	for person in a:
		# person is a dictionary 
		birthday = person['DOB'].split("/")
		# indexes to the month of dob and increases count by 1 when 
		# month matches value in dictionary
		for date in birthday:
			month = birthday[0]
			if month not in counts:
				counts[month] = 1
			else:
				counts[month] += 1
	# finds largest count and returns the month key associated
	maxCount = max(counts.values())
	for key in counts.keys():
		if counts[key] == maxCount:
			return int(key)
		
# Find the most common birth month form this data
# Input: list of dictionaries
# Output: Return the month (1-12) that had the most births in the data



def mySortPrint(a,col,fileName):
	"""This function sorts the data by column and saves data 
	into a csv file by first name, last name, and email
	"""
	# opens file and sorts column alphabetically 
	outfile = open(fileName, 'w')
	sort = sorted(a, key = lambda k: k[col])
	# saves and writes each person individually by first, last and email into csv file
	for student in sort:
		firstName = student['First']
		lastName = student['Last']
		email = student['Email']
		outfile.write("{},{},{}\n".format(firstName, lastName, email))
	outfile.close()

#Similar to mySort, but instead of returning single
#Student, the sorted data is saved to a csv file.
# as fist,last,email
#Input: list of dictionaries, col (key) to sort by and output file name
#Output: No return value, but the file is written


def findAge(a):
	"""This function returns the average age of students by using the 
	student's birthday and current date in years
	"""
	lst = list()
	# find each student's dob and subtracts it from current year(2018)
	for person in a:
		birthday = person['DOB'].split("/")
		year = birthday[2]
		yearCut = int(year[0:4])
		age = 2018 - yearCut
		lst.append(age)
	# finds average by dividing sum of values in list by number of digits in list
	average = sum(lst) / len(lst)
	return round(average)

# def findAge(a):
# Input: list of dictionaries
# Output: Return the average age of the students and round that age to the nearest
# integer.  You will need to work with the DOB and the current date to find the current
# age in years.
		

################################################################
## DO NOT MODIFY ANY CODE BELOW THIS
################################################################

## We have provided simple test() function used in main() to print what each function returns vs. what it's supposed to return.
def test(got, expected, pts):
  score = 0;
  if got == expected:
    score = pts
    print(" OK ", end=" ")
  else:
    print (" XX ", end=" ")
  print("Got: ",got, "Expected: ",expected)
  return score


# Provided main() calls the above functions with interesting inputs, using test() to check if each result is correct or not.
def main():
	getData('P1DataA.csv')
	total = 0
	print("Read in Test data and store as a list of dictionaries")
	data = getData('P1DataA.csv')
	data2 = getData('P1DataB.csv')
	total += test(type(data),type([]),50)

	print()
	print("First student sorted by First name:")
	total += test(mySort(data,'First'),'Abbot Le',25)
	total += test(mySort(data2,'First'),'Adam Rocha',25)

	print("First student sorted by Last name:")
	total += test(mySort(data,'Last'),'Elijah Adams',25)
	total += test(mySort(data2,'Last'),'Elijah Adams',25)

	print("First student sorted by Email:")
	total += test(mySort(data,'Email'),'Hope Craft',25)
	total += test(mySort(data2,'Email'),'Orli Humphrey',25)

	print("\nEach grade ordered by size:")
	total += test(classSizes(data),[('Junior', 28), ('Senior', 27), ('Freshman', 23), ('Sophomore', 22)],25)
	total += test(classSizes(data2),[('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)],25)

	print("\nThe most common month of the year to be born is:")
	total += test(findMonth(data),3,15)
	total += test(findMonth(data2),3,15)

	print("\nSuccessful sort and print to file:")
	mySortPrint(data,'Last','results.csv')
	if os.path.exists('results.csv'):
		total += test(filecmp.cmp('outfile.csv', 'results.csv'),True,20)

	print("\nTest of extra credit: Calcuate average age")
	total += test(findAge(data), 40, 5)
	total += test(findAge(data2), 42, 5)

	print("Your final score is " + str(total))

# Standard boilerplate to call the main() function that tests all your code
if __name__ == '__main__':
    main()
