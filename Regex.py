import re

# Find an 11 digit phone number in a sentance
phone_num_regex = re.compile(r'\d{11}') # Compile the regex
mo = phone_num_regex.search('My phone number is 07745556677!') # Search will find the first match
print('Phone number found: ' + mo.group()) # grou() will return the matched text

# Matching and picking groups
ps_cmdlet_regex = re.compile(r'(\w+)\-(\w+)')
mo = ps_cmdlet_regex.search('Use Get-ChildItem to see files')
# By picking out specific group
print('Cmdlet: ' + mo.group()) # group() will return the entire match
print('Verb: ' + mo.group(1)) # group(1) will return the first group, i.e. bracketed match
print('Noun: ' + mo.group(2)) # group(s) will return the second group
# Or by assigning all groups
verb, noun = mo.groups() # groups() will return a list of each matched group, not the entire match
print('Verb is ' + verb + ', noun is ' + noun)

# Greedy and non greedy regex 
greedy_regex = re.compile(r'(ha){3,5}') # By default regex is greedy
mo1 = greedy_regex.search('hahahahaha')
nongreedy_regex = re.compile(r'(ha){3,5}?') # Adding '?' on the end makes this not greedy
mo2 = nongreedy_regex.search('hahahahaha')
print('Greedy: ' + mo1.group())
print('Non-Greedy: ' + mo2.group())

# FindAll 
common_pet_regex = re.compile(r'cat|dog|fish')
mo1 = common_pet_regex.findall("I have a dog and a fish and a dragon") # findall() returns a list of all matches
print(mo1)

# FindAll with groups
common_pet_regex = re.compile(r'(Get)-(Command)')
mo1 = common_pet_regex.findall("To see a list of command use Get-Command") # findall() returns a list of tuples for each matche
print(mo1)

# Ignore case
pet_regex = re.compile(r'cat|dog', re.IGNORECASE)
mo1 = pet_regex.findall("My cat loves my dog")
mo2 = pet_regex.findall("My CAT loves my DOG")

# Substitue strings
sensitive_regex = re.compile(r'Password: \w+')
sensitive_regex.sub('CENSORED', 'Username: Administrator, Password: SecretPass')

# Verbose mode for complicated regex's
phrase = 'My email address is scott@contoso.com'
email_regex = re.compile(r'''(
	([a-zA-Z0-9._%+-]+) # The username
	(\@)                # The 'at' symbol
	(.+)                # The domain name
	(\.)                # The 'dot'
	(.+)                # The root domain name
)''', re.VERBOSE)
mo = email_regex.findall(phrase)