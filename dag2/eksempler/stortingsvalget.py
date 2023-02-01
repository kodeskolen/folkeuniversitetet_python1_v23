#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Hvilke år er det stortingsvalg?
Hvis vi husker at 2021 var et valgår, kan vi bruke
for-løkker til å finne de tidligere valgårene?
"""
print("Alle valgårene mellom 2021 og 1960 er:")
for år in range(2021, 1960, -4):
    print(år)

print("De fremtidige valgårene er:")
for år in range(2021, 2050, 4):
    print(år)

#Var 1985 et valgår?
if 1985 in range(2021,1960,-4):
    print("1985 var et valgår!")
else:
    print("1985 var ikke et valgår")