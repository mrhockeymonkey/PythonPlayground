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


#example for wrapping an api nicely
    def _api_call(self, api_path, method, params=None, data=None, json_data=None):
        url = urlparse.urljoin(self.api_base_url, api_path)
        try:
            # look up the given method in the requests package and execute with given params
            method = method.lower()
            r = getattr(requests, method)(url, params=params, data=data, json=json_data, auth=self._auth)
            r.raise_for_status()
            return r
        except requests.exceptions.HTTPError as err:
            raise
