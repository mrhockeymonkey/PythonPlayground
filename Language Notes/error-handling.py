import os
import traceback

# To catch an exception
try :
	5 // 0
except Exception as err : # Exception is the base of all error type, as err stores the error message in variable 'err'
	print(err)

# To Catch Specific exception
try :
	5 // 0 
except ZeroDivisionError as err : # Catch a specific type of error
	print('Did you try to divide by 0?')

# Raise your own error
try :
	if (os.path.exists('C:\\SomeFakeFile.txt')) :
		print('found you file')
	else :
		raise Exception('Wheres that file?') # raise is like throw
except Exception as err :
	print(err)

# Assert 
# You should not handle asserts with try try,except. If an assert fails you should fail the program
