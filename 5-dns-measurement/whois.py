import subprocess
import whois
import os,sys
import re

#execution time : 34 seconds

#function to delete a file
def deleteContent(pfile):
	pfile.seek(0)
	pfile.truncate()

codes = open("Country Codes") #open file
for code in codes: #for all country codes
	r = open("ccTLD","a+") #file where IPs of authoritative DNS servers will be stored
	for i in codes:
		f = open("my_tmp","a+") #temporary file
		deleteContent(f) #to prevent scrolling previously fetched data
		print(i.rstrip(), file = r)
		args = ['whois', '-h', 'whois.iana.org', i] #whois command
		subprocess.call(args, stdout = f)
		pattern = re.compile(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}[^0-9]") #IP address pattern in regular expression
		with open('my_tmp') as f:
			for line in f:
				if pattern.search(line): #find IP in each line
					match = pattern.search(line)
					ip = ""
					for x in range(match.start(), match.end()): #get full ip in a string
						ip += line[x]
					print(ip.rstrip(), file = r) #print ip
		print('\n', file = r)
	os.remove("my_tmp")
