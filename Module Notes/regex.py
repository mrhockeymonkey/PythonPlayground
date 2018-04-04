import re

str1 = "The telephone number was 07712345678 or 07787654321"

m = re.search(r'\d{11}', str1) # search for pattern. will only find the first thing that matches
m.group(0) # retreive the first match

re.findall(r'\d{11}', str1) # search and returns all patterns
re.findall(r'\d{11}', str1, flags=re.IGNORECASE) # can use flags to modify behaviour. Can find with dir(re)

re.match('The', str1) # will search from the beginning of string. I.e. ^ is used for you. 

str2 = "bacon and eggs"
r = re.sub(r'and', '&', str2) # substitute 
r = re.sub(r'(\w+) and (\w+)', r'\2 & \1', str2) # substitute using captured refs

str3 = "foo :: bar :: bla"
re.split('::', str3) # split a string by a pattern

#flags
re.search(r'pattern', str1, flags=re.DOTALL|re.MULTILINE)
# DOTALL will make \n matchable??
# VERBOSE can write pretty regex

search = r"""
\w{3}   # match three word chads
/       # match forward slash
\d$     # match digit at end
"""

# named capturing groups
m = re.search(r'(?P<first>a)(?P<second>b)(?P<third>c)', "abc") # capture using names
m.groups() # to see all captures
m.group('second') # to retreive named captures