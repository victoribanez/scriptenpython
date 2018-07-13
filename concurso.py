#! /usr/bin/python

import random, csv

participantes = []
with open('participantes.csv', 'rb') as csvfile:
	p = csv.reader(csvfile)
	for row in p:
		participantes.append(row[1])

#Al agua 1
print "El/la primero(a) al agua es: ", participantes[random.randint(0, 101)]
raw_input()

#Al agua 2
print "El/la segundo(a) al agua es: ", participantes[random.randint(0, 101)]
raw_input()

#Al agua 3
print "El/la tercero(a) al agua es: ", participantes[random.randint(0, 101)]
raw_input()

#Ganador
print "Y el/la ganador(a) es...", participantes[random.randint(0, 101)]
raw_input()
