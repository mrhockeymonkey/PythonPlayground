
# List
# Collection of objects, you can add or remove elements of a list (Mutable)
list = ['one', 'two', 'three'] # define a list
list[x] # get xth index element
list[x:y] # get a slice of list from x up to y (not inv y)
del list[3] # remove the third element fom the list
'one' in list # returns true if element is in list
'one' not in list # returns true is NOT in list
num1, num2, num3 = list # assign each of the variables to each element of list in order
list.index('two') # find what index a given element is.
list.appened('four') # add element at the end
list.insert(1,'onepointfive') # add element at specified index
list.sort(reverse=True) # sort
tuple(list) # convert list to tuple
list1 = copy.copy(list) # use copy module to make a new list object instead list1 referencing the same underlying object as list
list1 = copy.deepcopy(list) # use of the list you wish to copy contains lists

# Tuple
# Collection of objects, you cannot add or remove elements of a tuple (Immutable)
tuple = (1,2,3)
list(tuple) # convert tuple to list

# Dictionary
# Collection of Key-Vale pairs, equivalent to a powershell hashtable
dict = {Key1: "Value1", Key2: "Value2"}
dict.keys() # list of all keys
dict.values() # list of all values
dict.items() # returns a list of each key-value pair. each item is returned as a list
dict.get(key,'?') # get value of key, or return '?' is key not found
dict.setdefault(key,0) # add element with default value if not already present, ignored if is present

# String
str = 'Hello Wolrd'
r'hello\nworld' # raw string ignores escape chars
str.upper() # uppercase the string
str.islower() # check all chars lowercase
str.isX() # lots of different checks, alpha,num,decimal,title etc
str.startswith()
', '.join(list) # join a list int a string using the spacer ', '
str.rjust(width, fillchar) # eg: *********str. can also ljust and center
str.strip() # remove whitespace from left and right. can also rstrip & lstrip

# Here-String (Multi-line string)
herestring = """
	some string
"""
