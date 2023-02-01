#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Vi har en liste med fotballspillere og en liste med draktnummere.
Vi vil lage et program som tildeler tilfeldige draktnummere til spillerene.
"""
from random import shuffle

personer = ["Terje", "Jonas", "Emil", "Maja", "Silje", "Aida",
            "Frederik"]

draktnummere = [8, 11, 27, 29, 40, 66, 71, 83, 90, 98]

shuffle(personer)
shuffle(draktnummere)

index = 0
while index < len(personer):
    print(f"{personer[index]} skal få draktnummer {draktnummere[index]}.")
    index = index + 1

print("De ubrukte draktnummerene er:")
while index < len(draktnummere):
    print(draktnummere[index])
    index = index + 1