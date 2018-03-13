#!/usr/bin/python
from __future__ import print_function
class Node:
	'''It creates a node contains data and object of next node'''
	def __init__(self,data):
		self.data=data
		self.next=None

class LL:
	'''This class will be helpful in connecting the created nodes'''
	def __init__(self):
		self.head=None

	def print_list(self):
		'''Traverse the entire list and prints the data value of each node'''		
		temp=self.head
		while temp:
			print(temp.data)
			temp=temp.next

	def at_first(self,data):
		'''Inserting the new node at the beginning of Linked list'''	
		new_node=Node(data)
	
		if self.head is None:
			self.head=new_node
		else:
			new_node.next=self.head
			self.head=new_node

	def at_loc(self,prev,data):
		'''Inserting the new node next to the node of given value'''		
		temp=self.head
		while temp:
			if temp.data is prev:
				new_node=Node(data)
				new_node.next=temp.next
				temp.next=new_node
				break
			temp=temp.next
		else:
			print("previous node must be in LinkedList")

		
	def at_last(self,data):
		'''Inserting the new node at the last of the Linked list'''			
		new_node=Node(data)
		if self.head is None:
			self.head=new_node
		else:
			temp=self.head
			while temp.next:
				temp=temp.next
			temp.next=new_node

	
if __name__=='__main__': #if __name__ is equals to __main__ then this module acts as main program 

	LL1=LL()
	LL1.head=Node(1) #creating the head node of the Linkedlist
	'''second=Node(2)
	#third=Node(3)

	LL1.head.next=second
	second.next=third'''
	LL1.at_first(2)
	LL1.at_first(3)
	LL1.at_loc(2,4)
	LL1.at_loc(5,6)  #Will print the message as Previous node must be in linked list
	LL1.at_last(5)
	LL1.print_list()
	
