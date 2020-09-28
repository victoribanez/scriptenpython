#!/usr/bin/python
import random
import csv

participantes = []
with open('participantes.csv', 'r') as csvfile:
	p = csv.reader(csvfile)
	for row in p:
		participantes.append(row[1])

texto = ["El/la primere al agua: ", "El/la segunde al agua: ", 
	"El/la tercere al agua: ", "El/la afortunade es... "]

# Tres al agua y el ganador
for i in range(4):
	print("%s %s" % (texto[i], participantes[random.randint(0, len(participantes))]))
	input()
