#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dette programmet viser hvordan vi kan legge til elementer i
en liste ved hjelp av "append" og "input"
"""
from random import shuffle

personer = []

navn = input("Skriv inn et navn (eller skriv 'slutt'): ")

while navn != "slutt":
    personer.append(navn)
    print(personer)
    navn = input("Skriv inn et navn (eller skriv 'slutt'): ")


shuffle(personer)

index = 0
while index < len(personer):
    print(f"Spiller nummer {index+1} er {personer[index]}.")
    index = index + 1

person = "Georg"
print(f"Personen {person} er i listen: {person in personer}")
