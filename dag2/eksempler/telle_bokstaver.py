#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Her bruker vi først en for-løkke til å iterere over et navn
"""

#Eksempel 1:
navn = "Andreas"

for bokstav in navn:
    print(bokstav)
print(f"I navnet {navn} er det {len(navn)} bokstaver.")

#Eksempel 2:
navn = "Anne Mari"
antall_bokstaver = 0
for tegn in navn:
    if tegn != " ":
        antall_bokstaver = antall_bokstaver + 1

print(f"I navnet {navn} er det {antall_bokstaver} bokstav.")

#Eksempel 3:
navn = "Anne-Mari Jensen"
bokstaver = "ABCDEFGHIJKLMNOPQRSTUVWXYZÆØÅabcdefghijklmnopqrstuvwxyzæøå"

antall_bokstaver = 0
for tegn in navn:
    if tegn in bokstaver:
        antall_bokstaver = antall_bokstaver + 1
print(f"Du har {antall_bokstaver} i navnet ditt, {navn}.")
