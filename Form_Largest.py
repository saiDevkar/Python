#!/usr/bin/python
'''input: 3,9,1,7 output: 9731
   input: 99,5,68,44,10 output: 996854410'''
from __future__ import print_function

def form_largest(list1):
	'''It will form the possible largest number from the given number list'''
	firstdigit=[]
	finallist=[]
	finalstr=''	
		
	for x in list1:                                        #finding first difgit of every int and store in new list(in our case firstdigit)
		firstdigit.append(int(str(x)[0]))
	
	firstdigitsize=len(firstdigit)
	
	for _ in range(firstdigitsize):				#finding max number in firstdigit and storing its related value of list1 in finallist 
		maxindex=firstdigit.index(max(firstdigit))
		finallist.append(list1[maxindex])
		del firstdigit[maxindex]
		del list1[maxindex] 

	for x in finallist:
		finalstr+=str(x)

	return int(finalstr)

size=input('Enter the size of the List\n')
list1=[input() for _ in range(size)]
max_=form_largest(list1)
print('Max number from given Integers is :',max_)
