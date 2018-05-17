import subprocess,whois,os,re

def deleteContent(pfile):
	pfile.seek(0)
	pfile.truncate()

codes = open("Country Codes")
r = open("ccTLD","a+")
j = 0
for line in codes:
	j += 1
	print(str(round((j*100/54),0)) + "% (" +(str(j) + "/54)").rstrip(), end = "\r")
	f = open("my_tmp","a+")
	deleteContent(f)
	print(line.strip(), file = r)
	args = ['whois', '-h', 'whois.iana.org', line.strip()]
	subprocess.call(args, stdout = f)
	pattern = re.compile(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}[^0-9]")
	with open('my_tmp') as f:
		for line1 in f:
			if pattern.search(line1):
				print(pattern.search(line1).group().strip(), file = r)
		print("".rstrip(), file = r)
os.remove("my_tmp")
