#!/usr/bin/python
from __future__ import print_function
import random
import string

Password=''
Source=string.letters
Source+=string.digits
Source+=string.punctuation
Length=input('Enter the length of Password: ')
z=random.sample(Source,Length)

for x in z:
	Password+=x
print ('Your Password is\n'+Password)
