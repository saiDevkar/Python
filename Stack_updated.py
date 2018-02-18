#!/usr/bin/python
from __future__ import print_function
import sys

class Stack:
	'''This is a class implements the Stack operations'''
	def __init__(self,size):
		'''Initialise the set to empty and defining size of stack'''
		self.data=[]
		self.size=size
		

	def push(self):
		'''add's value to Stack'''
		if self.is_full():
			 print('***Cannot insert List is Full***\n')
		else:
			
			self.data.append(int(input('Enter value\n')))	
			#return 'value added'+value
			self.print_stack()
	
	def pop(self):
		'''remove's value from stack'''
		if self.is_empty():
			print('*** Stack is Empty***\n')
		else:
			 self.data.pop()
			 self.print_stack()
			
			

	def is_empty(self):
		'''Checks whether the stack is empty'''
		if self.data.__len__()==0:
			return True
		else:
			return False


	def is_full(self):
		'''Checks whether the stack is full'''
		if self.data.__len__()==self.size:
			return True
		else:
			return False

	def print_stack(self):
		print(self.data,end='\n\n')


def func_return():
	sys.exit(0)


size=int(input('Enter the size of stack\n'))
s1=Stack(size)
func={1: s1.push,
      2: s1.pop,
      3: s1.print_stack, 
      4: func_return
} #Dictionary used for switch-case purpose
x=1
while x!=4:
	x=int(input('Enter your choice\n1.Push\n2.Pop\n3.Dispay\n4.Exit\n'))
	func[x]()

			

