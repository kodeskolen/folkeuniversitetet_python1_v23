#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Vi ser på en liste med temperaturer. 
Klarer vi å finne klokkeslettet det var varmest?
"""

temperaturer = [-15.5,  -18.0,  -17.4,  -18.5,  -19.9,  -20.9,
                -21.5,  -22.0,  -20.5,  -18.6,  -15.6,  -13.5,
                -10.5,   -9.0,   -7.9,   -7.1,   -9.1,  -12.2,
                -14.8,  -16.5,  -16.8,  -15.3,  -17.6,  -19.7]

maks_temperatur = temperaturer[0]
kl_når_det_er_varmest = 0

for kl in range(24):
    temp = temperaturer[kl]
    if temp > maks_temperatur:
        maks_temperatur = temp
        kl_når_det_er_varmest = kl

print(f"Klokka {kl_når_det_er_varmest} var det varmest ({maks_temperatur} grader)")

# Hva var gjennomsnittstemperaturen ila dagen?
gj_snitt = 0

for temperatur in temperaturer:
    gj_snitt = gj_snitt + temperatur

gj_snitt = gj_snitt/len(temperaturer)

print(f"Den gjennomsnittlige temperaturen var: {gj_snitt:.2f} grader")

#Hva var median temperaturen?
temperaturer.sort()
median_temperatur = temperaturer[len(temperaturer)//2]
print(f"Median temperaturen var: {median_temperatur} grader")