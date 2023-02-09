#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 09:12:55 2023

I dette skriptet skal vi laste inn en tekstfil med en with-blokk.

Vi skal også bruke .readlines() for å hente ut linjene i dokumentet.

@author: m
"""

with open("testfil.txt", mode = "r") as fil:
    # filen "testfil.txt" er åpen inne i denne blokken
    # og er lagt i en variabel fil 
    innhold = fil.read() 
    
#innhold2 = fil.read()  # dette funker ikke! filen er lukket!

with open("testfil.txt", mode = "r") as fil:
    linjer = fil.readlines() 
    

for linje in linjer:
    print(linje.strip()) # hver linje slutter med "\n" 
