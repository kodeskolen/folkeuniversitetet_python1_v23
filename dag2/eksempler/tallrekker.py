#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Eksempler som viser hvordan for-løkker fungerer vha. tallrekker:
"""

#om du bare bruker ett argument/tall i range-funksjonen starter vi på 0
#da iterer vi fra null til (men ikke med) det tall i funksjonen
print("Den første tallrekka er:")
for tall in range(10):
    print(tall)

#Dersom vi gir range to tall, starter vi på det første tallet og går 
#til (men ikke med) det siste tallet.
print("Den andre tallrekka er:")
for tall in range(5, 11):
    print(tall)

#Dersom vi gir range tre tall, starter vi på det første tallet og 
#går til (men ikke med) det siste tallet, med hopp lik det tredje tallet
print("Den tredje tallrekka er:")
for tall in range(1, 11, 2):
    print(tall)


#Hva er summen av tallene fra 1 til 10?
summen = 0
for tall in range(1, 11):
    summen = summen + tall

print("Summen av tallene fra 1 til 10 er:")
print(summen)