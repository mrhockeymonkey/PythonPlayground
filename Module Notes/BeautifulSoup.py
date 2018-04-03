"""
beautiful soup is a module that allows you to scrape web pages
"""

import requests, bs4

res = requests.get('https://tfl.gov.uk/tube-dlr-overground/status/')
res.raise_for_status()
tfl_soup = bs4.BeautifulSoup(res.text)

example_file = open('etc/example.html')
example_soup = bs4.BeautifulSoup(example_file, "html.parser")

#Can select elemts using CSS selectors:
"""
CSS Selectors
soup.select('p')  All elements named <p>
soup.select('#title') all elements with id="title"
soup.select('.table') all elements with class="table"
soup.select('div span') all <span> elemtns that are within a <div> element
soup.select('div > span') all <span> elements that are directly within a <div>, i.e. no other elements between
soup.select('input[name]') all <input> elements that have a name attribute of any value
soup.select('input[type="button"]') all <input> elements that have an attribute type="button"
"""

#Select all <p> elements, print the element and inner text
p_elems = example_soup.select('p')
print(str(p_elems[0]))
print(p_elems[0].getText())

#Select all elements with class 'author', print element, inner text, attributes
author_elems = example_soup.select('#author')
print(author_elems[0])
print(author_elems[0].getText())
print(author_elems[0].attrs)
print(author_elems[0].get('id'))

example_file.close()


