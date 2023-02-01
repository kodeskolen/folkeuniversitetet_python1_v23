#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Eksempel på nøsta liste:
"""
#møbler er en liste der elementene også selv er lister.
#hvert element inneholder navnet på møbelet og prisen.
møbler = [[ "Leselampe", 159],
[ "Baderomsmatte", 89],
[ "Parasoll", 399],
[ "Speil med hylle", 239],
[ "Taklampe", 549],
[ "Liten vase", 129],
[ "Spisestuestol", 564],
[ "Grå puff", 449],
[ "Pledd", 235],
[ "Speilbrett", 390],
[ "Skoskap", 999],
[ "Bordklokke", 129],
[ "Boules sett", 299],
[ "Hylleseksjon", 1135],
[ "Benk", 799],
[ "Henger til dør", 109]]

print(f"Det første møbelet i listen er {møbler[0][0]}, som koster {møbler[0][1]} kr.")

#Hva koster møblene til sammen?
summen = 0
for møbel in møbler:
    summen = summen + møbel[1]

print(f"Møblene koster til sammen {summen} kr.")

