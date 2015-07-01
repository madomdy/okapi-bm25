import requests
from bs4 import BeautifulSoup

def get_text_url(url):
	page = requests.get(url)
	soup = BeautifulSoup(page.text)
	for script in soup(["script", "style"]):
		script.extract()
	pageText = soup.get_text()
	return pageText

def make_text_humanable(pageText):
	lines = (line.strip() for line in pageText.splitlines())
	# break multi-headlines into a line each
	chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
	# drop blank lines
	return '\n'.join(chunk for chunk in chunks if chunk)

def get_url_text(url):
	pageText = get_text_url(url)
	nicePageText = make_text_humanable(pageText)
	return nicePageText

if __name__ == "__main__":
	testQuery = 'http://www.thegeekstuff.com/2010/03/30-things-to-do-when-you-are-bored-and-have-a-computer/'
	pageText = get_url_text(testQuery)
	print(pageText[:100], '\n')