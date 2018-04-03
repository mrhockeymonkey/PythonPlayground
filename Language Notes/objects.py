"""
Variables
"""
my_var = 'Hello' # assingment
id(my_var) # address in memory?
del(my_var) # remove variable to save memory but garbage collector does this for you
del my_var # also works becuase its a statement not a function maybe??

# variables are references to object in memory
a = b = 20
a is b # will be True becuase they both reference the same object

val = 1 # augmented assignment
val += 1 # can also do - * / %

locals() # prints variables

# Conventions
_private_to_module = 1 # one underscore prefix for modules
__private_to_class = 2 # two underscore prefix for classes
__special__ = 3 # double-under


"""
Methods
"""
my_var.upper() # example method
dir(my_var) # to find methods
help(str) # to see methods for type str

