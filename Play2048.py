"""

"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Game2048():
	def __init__(self):
		self.url = 'https://gabrielecirulli.github.io/2048/'
		self.chromedriver = 'C:/Temp/chromedriver_win32/chromedriver.exe'
		self.body = self.open2048()

		#self.play2048(Keys.UP)
		#self.play2048(Keys.UP)
		#self.play2048(Keys.DOWN)
		#self.play2048(Keys.UP)

	def open2048(self):
		browser = webdriver.Chrome(self.chromedriver)
		browser.get(self.url)
		body = browser.find_element_by_tag_name('body')
		return body

	def play2048(self, direction):
		self.body.send_keys(direction)



if __name__ == '__main__':
	game = Game2048()
	tactic = [
		Keys.RIGHT,
		Keys.RIGHT,
		Keys.RIGHT,
		Keys.DOWN,
		Keys.DOWN,
		Keys.RIGHT,
		Keys.RIGHT,
		Keys.RIGHT,
		Keys.DOWN,
		Keys.DOWN,
		Keys.DOWN, 
		Keys.UP,
		Keys.DOWN
	]

	while True:
		for t in tactic:
			game.play2048(t) 
		









#html_elem.send_keys(Keys.UP)
#html_elem.send_keys(Keys.UP)
#html_elem.send_keys(Keys.DOWN)
#html_elem.send_keys(Keys.DOWN)
#html_elem.send_keys(Keys.UP)