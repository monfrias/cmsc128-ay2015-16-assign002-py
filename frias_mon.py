import sys

def getHammingDistance(str1, str2):	#function that counts the number of different characters in two strings given at specified indices
	res = 0
	if len(str1) == len(str2):	#checks if two strings have the same length
		for i in range(0, len(str1)):	#for loop in string1
		 	if str1[i] != str2[i]:	#checks if two strings have different character at specified index i
		 		res += 1	#increment res
		return res
	else:
		return "Error! String lengths are not equal!"

def countSubstrPattern(original, pattern):	#function that counts the number of times a pattern is found in a string
	res = 0
	for i in range(0, (len(original)-len(pattern)+1)):	#for loop with edited range (to avoid index out of bounds)
		if original[i:(i + len(pattern))] == pattern:	#if a substring in a string is the same as the pattern
			res += 1	#increment res
	return res

def isValidString(str, alphabet):	#function that validates a string given a set of alphabets
	isFound = False
	for i in range(0, len(str)):	#for loop in string
		for j in range(0, len(alphabet)):	#for loop in alphabet
			if str[i] == alphabet[j]:	#checks if string and alphabet is the same character at specified index i
				isFound = True
				break	#go to next string index
			else:	#otherwise (not the same)
				isFound = False
	return isFound	#if all characters in string is found in the alphabet, this should be returning True. Otherwise, return False

def getSkew(str, n):	#function that returns the number of Gs subtracted to number of Cs in n number of nucleotides
	if(len(str) > 0):
		if(n>0):
			numberOfG = 0;	#counter for Gs
			numberOfC = 0;	#counter for Cs
			for i in range(0, len(str)):	#for loop in str
				if(str[i] == "G"):	#if character found is G
					numberOfG += 1 	#increment numberOfG
				elif(str[i] == "C"):#else if character found is C
					numberOfC += 1 	#increment numberOfC
				if(i == n-1):	#checks if number of nucleotides traversed is reached
					break
			return (numberOfG - numberOfC)	#returns the answer for G-C

		else:
			return "Invalid Input! Number of nucleotides must be greater than zero!"
	else:
		return "Invalid input! String must not be null!"

def getMaxSkewN(str, n):	#function that returns the MAX number of Gs subtracted to number of Cs in n number of nucleotides
	if(len(str) > 0):
		if(n>0):
			if(n > len(str)):	#checks if number of nucleotides is greater than the length of String, then ERROR
				return "Invalid Input! N is larger than String length!"
			listOfAnswers = []
			count = 0
			numberOfG = 0	#counter for Gs
			numberOfC = 0	#counter for Cs
			for a in range(0, len(str)):	#for loop for str
				listOfAnswers.insert(a, 0)	#initialize a list with value 0
				if(a == n-1):	#checks if number of nucleotides traversed is reached
					break
			while (count < n):	#while number of nucleotides traversed is not reached
				if(str[count] == "G"):	#if character found is G
					numberOfG += 1 	#increment numberOfG
				elif(str[count] == "C"):#else if character found is C
					numberOfC += 1 	#increment numberOfC
				listOfAnswers[count] = (numberOfG - numberOfC)	#replace the ith value of list with the skewed value
				count += 1 	#increment count
			listOfAnswers.sort()	#sort the list of answers in ascending form
			return listOfAnswers[len(listOfAnswers)-1]	#return the value in the last index (MAX VALUE)
		else:
			return "Invalid Input! Number of nucleotides must be greater than zero!"
	else:
		return "Invalid input! String must not be null!"

def getMinSkewN(str, n):	#function that returns the MIN number of Gs subtracted to number of Cs in n number of nucleotides
	if(len(str) > 0):
		if(n>0):
			if(n > len(str)):	#checks if number of nucleotides is greater than the length of String, then ERROR
				return "Invalid Input! N is larger than String length!"
			listOfAnswers = []
			count = 0
			numberOfG = 0	#counter for Gs
			numberOfC = 0	#counter for Cs
			for a in range(0, len(str)):	#for loop for str
				listOfAnswers.insert(a, 0)	#initialize a list with value 0
				if(a == n-1):	#checks if number of nucleotides traversed is reached
					break
			while (count < n):	#while number of nucleotides traversed is not reached
				if(str[count] == "G"):	#if character found is G
					numberOfG += 1 	#increment numberOfG
				elif(str[count] == "C"):#else if character found is C
					numberOfC += 1 	#increment numberOfC
				listOfAnswers[count] = (numberOfG - numberOfC)	#replace the ith value of list with the skewed value
				count += 1 	#increment count
			listOfAnswers.sort()	#sort the list of answers in ascending form
			return listOfAnswers[0]	#return the value in the first index (MIN VALUE)
		else:
			return "Invalid Input! Number of nucleotides must be greater than zero!"
	else:
		return "Invalid input! String must not be null!"



# --- TEST CASES ---
# print(getHammingDistance("AACCTTA", "GGCCTTA"))
# print(countSubstrPattern("AATATATAGG", "ATA"))
# print(isValidString("AAGGCTATGC", "ACGT"))
# print(getSkew("GGCCAC", 1))
# print(getMaxSkewN("GGCCAC", 6))
# print(getMinSkewN("GGCCAC", 6))