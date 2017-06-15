import requests

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')

#Show the type of response
print(type(res))

#Check response code
print(res.status_code == requests.codes.ok)

#show the response text
print(res.text[:250])

#write content to file
file = open('RomeoAndJuliet.txt', 'wb')
for chunk in res.iter_content(100000): #iter_content() returns chunks of response data, 100000 is the size of each chunk
	file.write(chunk)
file.close()

#Raise an issue
res = requests.get('http://inventwithpython.com/page_that_does_not_exists')
try:
	res.raise_for_status() #should always call to verify no issue
except Exception as e:
	print('There was a problem but ignoring: %s' % (e))



