
from selenium import webdriver

#For chrome you need to have downloaded the chromium driver
#See: https://sites.google.com/a/chromium.org/chromedriver/getting-started
browser = webdriver.Chrome('C:/Temp/chromedriver_win32/chromedriver.exe')
browser.get('http://inventwithpython.com')

#Finding elements
"""
find_element_* will get the first match
find_elements_* will get all matches

_by_class_name(name) = by CSS class, eg ".title"
_by_css_selector(selector) = See BeautifulSoup notes for CSS selectors
_by_id(id) = obvious
_by_link_text
_by_partial_link_text
_by_name(name) = element with an attribute called name, eg <a name="blah"></a>
_by_tag_name = by tag, eg <a>

WebElement Attributes:
tag_name
get_attribute(name)
text
clear() = clears the text value on that page
click() = simulates a click on that element
is_displayed() = Returns true or False is visibale or not
is_enabled()
is_selected() 

"""

elem = browser.find_element_by_id('sidebar')
print("Found <%s> element with class name sidebar" % elem.tag_name)

links = browser.find_elements_by_tag_name('a')
for l in links[:5]:
	print("Found <a> tag with href: %s" % l.get_attribute('href'))


#Clicking the page
links[1].click()

#Clickingbrowser buttons
browser.back() #Also: forward(), refresh(), quit()

#Sending keys
from selenium.webdriver.common.keys import Keys

html_elem = browser.find_element_by_tag_name('html')
html_elem.send_keys(Keys.END)
html_elem.send_keys(Keys.HOME)

#This can also be used for sending keyboad input to an element