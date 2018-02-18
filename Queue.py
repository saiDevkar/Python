#!/usr/bin/python
from __future__ import print_function
import sys

class Queue:

	def __init__(self,size):
		'''Initialize the queue and defining size'''
		self.data=[]
		self.size=size
		pass

	def enque(self):
		'''Inserting item into Queue'''
		if self.is_full():
			print('***Queue is Full***\n')
		else:
			
			self.data.insert(0,int(input('Enter value\n')))
			self.display_queue()
		pass

	def deque(self):
		'''Removing item from queue'''
		if self.is_empty():
			print('***Queue is Empty***\n')
		else:
			self.data.pop()
			self.display_queue()

	def is_empty(self):
		'''Checking if Queue is empty'''
		if self.data.__len__()==0:
			return True
		else:
			return False

	def is_full(self):
		'''Checking if Queue is full'''
		if self.data.__len__()==size:
			return True
		else:
			return False
		

	def display_queue(self):
		'''Displays the queue'''
		print(self.data,end='\n')

def exit_func():
	'''Terminating the loop'''
	sys.exit(0)

size=int(input('Enter the size of Queue\n'))
q1=Queue(size)
func={1: q1.enque,
      2: q1.deque,
      3: q1.display_queue, 
      4: exit_func
} #Dictionary used for switch-case purpose
x=1
while x!=4:
	x=int(input('Enter your choice\n1.Enque\n2.Deque\n3.Dispay\n4.Exit\n'))
	func[x]()


