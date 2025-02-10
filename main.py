# variables
num_var = 0
str_var = "chien" # str_var = 'chien' # since ' and " are interchangable
bool_var = True # or False, must be capitalized, python is case sensitive
doc_string = """
chien
	animal
Michel
""" # docstrings is a variable type that is a multiline string

# iterables
""" 
	iterables are variables you can iterate over
"""
## List
"""
	lists are arrays, they are mutable (can be changed afer initialiszation) and ordered (each item in the list is retreavable by it's postion in the list). This index is handles by python and can't be handled by the user.
""" 
list_var = [] # you can also define and initialize a list that contains data like list_var = ["chien", "chat", "michel"]
list_var.append("chien") # => list.append adds an item to the en of the list.
first_item = list_var.pop() # => removes and returns the first item of the list (treats the list as fifo)
list_var.append("chat")
list_var.append("michel")
last_item = list_var[-1] # retreives the last item of the list
list_var[0] = "chienchatmichel" # replaces the first item of the list

# loops
## for loops

for i in list_var:
	print(i)

# iterates over the iterable list_var

for i in range(len(list_var)): # len is a function you can use to get the length of an iterable
	print(i) # prints the current list index
	print(list_var[i]) # prints the list item at current i index

"""
	range(i,j,step) is a funtion that will return a list of integers between i and j with each item being i+step till it reaches j.
	If you only give one param, that param will be j, in that case i will be 0 and step will be 1
"""


## while loops

while condition:
	if ignoring_condition: # passes to next iteration
		continue
	if breaking_condition: # exits the loop
		break 
	if exiting_condition: # exits the program 
		exit() # or sys.exit() => this requires the import of the sys package

	print('chien')


""" 
	In this example, each of these condition vars are boleans. 
	they could be defined before hand as ternaries or defined on the go
"""


# imports 

import time # imports the time module
from time import time # imports the time object from the time module 
import time as michels_time # imports the time module with the alias michels_time



# classes

class Animal:
	def __init__(self, name, weight, height, width, length):
		self.name = name
		self.weight = weight
		self.height = height
		self.width = width
		self.length = length

	def get_density()(self):
		return self.weight / (self.height*self.widt*self.length)


class Chien(Animal):
	def __init__(self, breed, name, weight, height, width, length):
		super().__init__(name, weight, height, width, length) # initializes the parent class
		self.breed = breed

	def describe(self):
		return f"I am a Chien of the {self.breed} breed, my density is {self.get_density()}"


