#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 10:30:38 2023

I dette scriptet høyden til en kar Gunnar, som en funksjon av hans alder. 
I tillegg skal vi lagre figuren vi ender opp med.

@author: m
"""

from pylab import plot, show, xlabel, ylabel, savefig 

with open("hoyde_alder.txt", mode = "r") as fil:
    linjer = fil.readlines() 
    
høyde = []
alder = [] 

for linje in linjer[1:]:
    hoyde_alder = linje.split(" ") # første element i hoyde_alder er høyden
    # andre element er alder
    
    høyde.append(float(hoyde_alder[0])) 
    alder.append(float(hoyde_alder[1]))
    
plot(alder, høyde) 
xlabel("Alder [år] ")
ylabel("Høyde [cm]") 

savefig("hoydekurve_gunnar.png")