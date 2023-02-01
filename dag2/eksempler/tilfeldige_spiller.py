#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Her lager vi først en liste med navn. Denne stokker vi om på å skriver
ut i tilfeldig rekkefølge.
"""
from random import shuffle

personer = ["Terje", "Jonas", "Emil", "Maja", "Silje", "Aida",
            "Frederik"]

print(personer)

personer.sort()

print(personer)

shuffle(personer)

print(personer)

index = 0
while index < len(personer):
    print(f"Spiller nummer {index+1} er {personer[index]}.")
    index = index + 1

#vi kan bytte ut while-løkken med en for-løkke:
nr = 1
for navn in personer:
    print(f"Spiller nummer {nr} er {navn}.")
    nr = nr + 1