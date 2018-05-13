import matplotlib.pyplot as plt, numpy as np, plotly.plotly as py, os, re, sys, pandas as pd, pathlib as path

df = pd.DataFrame(columns = ['IP','Value'])
f = open("./Results/"+sys.argv[1])
valuepattern = re.compile(r'[0-9]{1,5}')
ippattern = re.compile(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}[^0-9]")
datepattern = re.compile(r'[0-9]{4}(-)[0-9]{2}(-)[0-9]{2}')
ip = ""
i=0
for line in f:
	if (datepattern.search(line)):
		continue
	if (ippattern.search(line)):
		ip = line.rstrip()	
	elif (valuepattern.search(line)):
		df.loc[i] = [ip, int(line.rstrip())]
	i+=1
df.Value = df.Value.astype(int)
print(df.groupby('IP')['Value'].agg(np.mean))
print(df.groupby('IP')['Value'].agg(np.std))
df.boxplot('Value', 'IP')
plt.show()
