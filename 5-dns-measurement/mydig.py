import subprocess, os, shlex, re, datetime, pathlib as path

def deleteContent(pfile):
	pfile.seek(0)
	pfile.truncate()

code = ""
i = 0
h = 'file'
mytmp = open("mytmp","a+")
countries = open("ccTLD")
pattern = re.compile(r'[0-9]{1,5}( msec)')
for x in countries:
	if len(x.rstrip()) == 3:
		i = i + 1
		code = x.rstrip()
		h = open("./Results/"+code[1]+code[2],"a+")
		print(datetime.datetime.now(), file = h)
		subprocess.call("clear")
		print(str(round((i*100/54),0)) + " % (" +(str(i) + " / 54)").rstrip())
	elif len(x.rstrip()) > 3:
		print(x.rstrip(), file = h)
		deleteContent(mytmp)
		cmd = "time dig @" + x.rstrip() + " -f " + ("./Sites/"+code[1]+code[2]).rstrip() +".bat"
		#print(cmd)
		proc = subprocess.Popen(shlex.split(cmd), stdout = mytmp)
		out,err=proc.communicate()
		with open('mytmp') as file:
			for line in file:
				if pattern.search(line):
					print(pattern.search(line).group().split(" ")[0].rstrip(), file = h)
os.remove("mytmp")
