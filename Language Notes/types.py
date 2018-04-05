"""
Misc
"""
type(var) # find type
int('999') # explicitly convert types
int('0xFF', 16) # fun with hex, comes out as 255 as an int

# when using mutable objects like lists 
list1 = list2 # these are both refs to the same object in memory which may be bad
list2 = list1[:] # copies all element but if an element is another list we have just moved the problem
list2 = copy.deepcopy(list1) # copy the whole structure as a new object in memory

"""
List
"""
# Collection of objects, you can add or remove elements of a list (Mutable)
l1 = ['one', 'two', 'three'] # define a list
l1[x] # get xth index element
l1[x:y] # get a slice of list from x up to y (not inv y)
del l1[3] # remove the third element fom the list
'one' in list # returns true if element is in list
'one' not in list # returns true is NOT in list
num1, num2, num3 = list # assign each of the variables to each element of list in order
l1.index('two') # find what index a given element is.
l1.appened('four') # add element at the end
l1.insert(1,'onepointfive') # add element at specified index

l1 = [2, 3]
l1[:0] = [1] # adds to the begining of a list but only iterable objects
l1.extend([4]) # same but at the end
l1.sort(reverse=True) # sort
tuple(list) # convert list to tuple
l1 = copy.copy(list) # use copy module to make a new list object instead list1 referencing the same underlying object as list
l1 = copy.deepcopy(list) # use of the list you wish to copy contains lists

# rmeove elems
l1.pop(n) # removeby index
l1.remove('blue') # rmeove by value

l1.sort() # in memory sort
sorted(l1) # create new sorted object
sorted(l1, key=len) # sorts by apply the function len, i.e. size. or str.lower by lowcase etc. 

zip(l1, l2) # interlace two lists, returns a list of tuples. 

dict1 = {'one':1, 'two':2}
[i for i in dict1] # generator that returns ['one', 'two']

list1 = [1, 2, 3, 4, 5, 6, 7, 8]
[i for i in list1 if not i%2] # generator with condition statement that retusn even numbers
['even' if not i%2 else 'odd' for i in list1]

"""
Tuple
"""
# Collection of objects, you cannot add or remove elements of a tuple (Immutable)
t1 = (1,2,3)
list(t1) # convert tuple to list

"""
Dictionary
"""
# Collection of Key-Vale pairs, equivalent to a powershell hashtable
d1 = {'k1': 1, 'k2': 2}
d1.keys() # list of all keys
d1.values() # list of all values
d1.items() # returns a list of each key-value pair. each item is returned as a list
d1.get('k1','?') # get value of key, or return '?' is key not found
d1.setdefault('k1',0) # add element with default value if not already present, ignored if is present

d2 = {'k1': 99, 'k3':99}
d1.update(d2) # updates the dict. updates values if key already present and add new keys
# Frozen Dict is an immutable version of dict if required

dict(zip(l1, l2)) # can make a dict from twolists by first zippig them

# unpacking
my_list = [1 , 2 , 3 , 4]
x, y, *z = my_list # gives 1 2 [3, 4]

# comprehension
numbers = ['zero','wun','two','tree','fower','fife','six','seven','ait','niner']
codes = {str(i):name for i,name in enumerate(numbers)}  # result dict with ints as keys and number in list as value

{k:v for k,*v in ('key', 'val1','val2')} # nice syntactically. makes dict with value a list of val1 and val2 courtesy of packing *v

"""
String
"""
str = 'Hello Wolrd'

str[1:7] # selct chars from 1 - 6
str[10::-1] # seect chars starting form ten but stepping -1 (ie. rveser from char 10)
str.upper() # uppercase the string
str.islower() # check all chars lowercase
str.isX() # lots of different checks, alpha,num,decimal,title etc
str.startswith()
', '.join(list) # join a list int a string using the spacer ', '
str.rjust(width, fillchar) # eg: *********str. can also ljust and center
str.strip() # remove whitespace from left and right. can also rstrip & lstrip
str = "hello" + "world" # concat string
str = "Hello {0}".format('World') # add words to strings using format()
str = "{h}, {w}".format(h='Hello', w='World') # add words by variable for more complex strings

print("hello\nworld") # unicode so newline is added
print(r"hello\nworld") # raw string so special chars ignored

vals = ['foo', 'bar'] # new in 3.6
f'value is {vals[0]}' # powershell like string sub
chr(0x03B1) # to display special characters
u'\u03B1' # spciel chars by two-byte unicode
'\u03B1' # works too?

# Here-String (Multi-line string)
herestring = """
	some string
"""


"""
Sets
"""
s1 = {'foo','bar'} # in sets elements must be unique and are unordered
s2 = {'foo', 'bar', 'foo'} # will become {'foo', 'bar'}
s1 == s2 # will be true becuase duplicate value got scrubbed

s1.intersection(s2) # find the intersection of sets (think Venn diagram)
s1 & s2 # same but with operator

s1.union(s2) # find the union. 
s1 | s2 # same butwith operator

s1.difference(s2) # items s1 but not in s2
s1 - s2  

s1.symmetric_difference(s2) # items only in one set. Opposite of intersection
s1 ^ s2

list(set(l1)) # way of getting only unique values in a list

#set comprehension
sentence = 'The quick brown fox jumps over the lazy dog.'
letters = { char.lower() for char in sentence if char.isalpha() } # get all unique alphabetic letters in string