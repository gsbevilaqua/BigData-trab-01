import matplotlib.pyplot as plt
import numpy as np

data = []

arq = open('character-deaths.csv', 'r')
arq.readline()

#Coloca as informações dos personagens em data
for line in arq.readlines():
	data.append(line.split(","))

#Coloca em newdata apenas os personagens da Night's Watch
newdata = []
for i in range(0, len(data)):
	if (data[i][1] == "Night's Watch"):
		newdata.append(data[i])

#Coloca em dyears todos os anos de morte de personagens da Night's Watch
dyears = []
for i in range(0, len(newdata)):
	if(newdata[i][2] == ''):
		pass
	else:
		year = int(newdata[i][2])
		dyears.append(year)

#Plota um histograma da quantidade de mortes dos personagens da Night's Watch por Ano
n, bins, patches = plt.hist(dyears, 10)

plt.axis([296, 301, 0, 35])
plt.grid(True)
plt.xticks(range(297, 301, 1))
plt.show()