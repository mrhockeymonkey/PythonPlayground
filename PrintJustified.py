"""
Given a dictionary of final fantasy items print a menu using justification
"""

# Define function to print items using justification
def printinventory(items_dict, left_width, right_width) :
	# Print heading centered to cover the entire width specified
	print('INVENTORY'.center(left_width + right_width, '='))
	# Get all items from the dictionary and assign k to the key and v to the value on the fly
	for k, v in items_dict.items() :
		# Print each key justified with '.' and the each value justified with ' '
		print(k.ljust(left_width, '.') + v.rjust(right_width, ' '))


items = { 'potion':'5' , 'elixir':'10', 'tent':'2', 'soft':'67' }
printinventory(items, 20, 10)