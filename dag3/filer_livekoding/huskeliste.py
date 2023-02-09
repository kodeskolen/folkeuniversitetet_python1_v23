#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 09:23:11 2023

I dette scriptet skal vi lagre en huskeliste i en ny fil. 

@author: m
"""

huskeliste = ["Vaske bilen", "Rydde huset", "Kjøpe middag"] 
tidsbruk = [3, 10, 1] # hvor lang tid hvert gjoremaal tar

# NB "w" overskriver (SLETTER) alt som evt. er i filen fra før 
with open("huskeliste.txt", mode = "w") as fil: 
    
    fil.write("Gjøremål, Tid\n") # skriver Gjøremål, Tid til filen "huskeliste.txt"
    
    for i in range(len(huskeliste)):
        fil.write(f"{huskeliste[i]}, {tidsbruk[i]}\n")

