"""
an example of two patterns i have used to interface with an api that requires ntlm authentication
the main issue being that you need to create an auth object that needs to somehow be shared
"""

# Package style
# helps to seperate complicated apis into a package for clarity but requires the use of a global instance of api shared
# shop
# -- __init_.py
# -- api.py  <-- in here we can have a global instace of api the user can create woith .connect()
# -- chips.py <-- different categries of api are handlined in submodules
# -- fish.py

import shop
shop.connect('user','pass')
shop.fish.get('cod')

# Instance style
# imagine an api that has different categories; fish & chips
# here we make an instance of the api so could support multiple shop

class MrsTs:
    def __init__(self, username, password):
        pass
        
    def fish(self):
        return Fish(self)
        
    def chips(self):
        return Chips(self)

class Fish(object):
    def __init__(self, API):
        self._api = API

    def get(self, query):
        return serlf._api.do_query(query)
        
class Chips(object):
    def __init__(self, API):
        self._api = API

    def get(self, query):
        return serlf._api.do_query(query)

shop = Shop('user', 'pass')
fish = shop.chips()
fish.get('cod')
