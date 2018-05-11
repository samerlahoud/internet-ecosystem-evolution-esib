from bs4 import BeautifulSoup
import urllib.request
import re, os

def deleteContent(pfile):
	pfile.seek(0)
	pfile.truncate()

c = open("Codes")
for i in c:
	res = open(i.rstrip()+".bat","a+")
	websource = urllib.request.urlopen("https://www.alexa.com/topsites/countries/"+i.upper())
	soup = BeautifulSoup(websource.read(), "html.parser")
	r = open("results", "a+")
	deleteContent(r)
	pattern = re.compile(r'(([\w]+.[a-z]+))(\.)('+i+')')
	print (soup.get_text(), file = r)
	with open('results') as r:
		for line in r:
			if pattern.search(line):
				match = pattern.search(line)
				print(match.group().rstrip(), file = res)
os.remove("results")
