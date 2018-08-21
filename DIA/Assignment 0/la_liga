from urllib import urlopen
from bs4 import BeautifulSoup
# specify the url
quote_page = ‘http://www.bloomberg.com/quote/SPX:IND'
# query the website and return the html to the variable ‘page’
page = urllib2.urlopen(quote_page)
# parse the html using beautiful soup and store in variable `soup`
soup = BeautifulSoup(page, ‘html.parser’)